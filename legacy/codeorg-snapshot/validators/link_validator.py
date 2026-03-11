#!/usr/bin/env python3
"""
Link Validator for Dependency Documentation

This script validates all links in the dependency documentation:
1. Local links: Verifies files exist and line numbers are valid
2. External links: Checks URLs are accessible and contain expected package names
3. Generates a comprehensive report of broken links and issues
"""

import os
import re
import requests
import time
from pathlib import Path
from urllib.parse import urlparse, urljoin
from datetime import datetime
import json

class LinkValidator:
    def __init__(self, base_dir="/workspace"):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs" / "dependencies"
        self.results = {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Code.org Link Validator 1.0'
        })
        # Rate limiting
        self.request_delay = 0.5
        self.last_request_time = 0
        
    def rate_limit(self):
        """Simple rate limiting to be respectful to external sites"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < self.request_delay:
            time.sleep(self.request_delay - time_since_last)
        self.last_request_time = time.time()
    
    def extract_links_from_content(self, content, file_path):
        """Extract all markdown links from content"""
        links = []
        
        # Pattern for markdown links: [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        for match in re.finditer(link_pattern, content):
            link_text = match.group(1)
            link_url = match.group(2)
            line_number = content[:match.start()].count('\n') + 1
            
            links.append({
                'text': link_text,
                'url': link_url,
                'line': line_number,
                'type': self.classify_link(link_url, file_path)
            })
        
        return links
    
    def classify_link(self, url, file_path):
        """Classify link as local or external"""
        if url.startswith('http://') or url.startswith('https://'):
            return 'external'
        elif url.startswith('#'):
            return 'anchor'
        elif url.startswith('mailto:'):
            return 'email'
        else:
            return 'local'
    
    def validate_local_link(self, link, file_path):
        """Validate local file links"""
        url = link['url']
        file_path_obj = Path(file_path)
        
        # Extract file path and anchor separately
        if '#' in url:
            file_part, anchor_part = url.split('#', 1)
        else:
            file_part = url
            anchor_part = None
        
        # Handle relative paths
        if file_part.startswith('../../'):
            # Remove ../../ prefix and resolve
            relative_path = file_part[6:]  # Remove ../../ prefix
            target_path = self.base_dir / relative_path
        elif file_part.startswith('../'):
            # Handle single ../ prefix
            relative_path = file_part[3:]
            target_path = file_path_obj.parent / relative_path
        elif file_part.startswith('./'):
            # Handle ./ prefix
            relative_path = file_part[2:]
            target_path = file_path_obj.parent / relative_path
        else:
            # Assume relative to current file
            target_path = file_path_obj.parent / file_part
        
        # Check if file exists
        if not target_path.exists():
            return {
                'status': 'broken',
                'error': f"File does not exist: {target_path}",
                'suggestion': f"Check if file path is correct"
            }
        
        # Check for line number reference
        if anchor_part and anchor_part.startswith('L'):
            try:
                line_number = int(anchor_part[1:])
                return self.validate_line_number(target_path, line_number)
            except ValueError:
                return {
                    'status': 'warning',
                    'error': f"Invalid line number format: {anchor_part}",
                    'suggestion': "Line numbers should be in format #L123"
                }
        
        return {'status': 'valid', 'error': None}
    
    def validate_line_number(self, file_path, line_number):
        """Validate that line number exists in file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            if line_number > len(lines):
                return {
                    'status': 'broken',
                    'error': f"Line {line_number} does not exist (file has {len(lines)} lines)",
                    'suggestion': f"Check if line number is correct (max: {len(lines)})"
                }
            elif line_number < 1:
                return {
                    'status': 'broken',
                    'error': f"Invalid line number: {line_number}",
                    'suggestion': "Line numbers must be >= 1"
                }
            else:
                return {'status': 'valid', 'error': None}
                
        except Exception as e:
            return {
                'status': 'error',
                'error': f"Could not read file: {e}",
                'suggestion': "Check file permissions and encoding"
            }
    
    def validate_external_link(self, link):
        """Validate external URLs"""
        url = link['url']
        
        try:
            self.rate_limit()
            response = self.session.get(url, timeout=10, allow_redirects=True)
            
            if response.status_code == 200:
                # Check if page contains expected package name
                package_name = self.extract_package_name_from_url(url)
                if package_name:
                    content = response.text.lower()
                    if package_name.lower() not in content:
                        return {
                            'status': 'warning',
                            'error': f"Package name '{package_name}' not found on page",
                            'suggestion': f"Verify this is the correct URL for {package_name}",
                            'status_code': response.status_code
                        }
                
                return {
                    'status': 'valid',
                    'error': None,
                    'status_code': response.status_code
                }
            else:
                return {
                    'status': 'broken',
                    'error': f"HTTP {response.status_code}",
                    'suggestion': "Check if URL is correct and accessible",
                    'status_code': response.status_code
                }
                
        except requests.exceptions.Timeout:
            return {
                'status': 'error',
                'error': "Request timeout",
                'suggestion': "URL may be slow or unreachable"
            }
        except requests.exceptions.ConnectionError:
            return {
                'status': 'error',
                'error': "Connection error",
                'suggestion': "Check internet connection and URL"
            }
        except Exception as e:
            return {
                'status': 'error',
                'error': f"Unexpected error: {e}",
                'suggestion': "Check URL format and accessibility"
            }
    
    def extract_package_name_from_url(self, url):
        """Extract package name from URL for validation"""
        # Common patterns for package URLs
        patterns = [
            r'github\.com/[^/]+/([^/]+)',  # github.com/user/repo
            r'pypi\.org/project/([^/]+)',  # pypi.org/project/package
            r'rubygems\.org/gems/([^/]+)',  # rubygems.org/gems/gem
            r'npmjs\.com/package/([^/]+)',  # npmjs.com/package/package
            r'([^/]+)\.dev',  # package.dev
            r'([^/]+)\.io',   # package.io
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def validate_anchor_link(self, link, file_path):
        """Validate anchor links within the same file"""
        url = link['url']
        anchor = url[1:]  # Remove # prefix
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for markdown headers that could be anchors
            header_pattern = r'^#+\s+(.+)$'
            headers = re.findall(header_pattern, content, re.MULTILINE)
            
            # Convert headers to potential anchor text
            potential_anchors = []
            for header in headers:
                # Convert to anchor format (lowercase, replace spaces with hyphens)
                anchor_text = re.sub(r'[^\w\s-]', '', header.lower())
                anchor_text = re.sub(r'[-\s]+', '-', anchor_text)
                potential_anchors.append(anchor_text)
            
            if anchor in potential_anchors:
                return {'status': 'valid', 'error': None}
            else:
                return {
                    'status': 'broken',
                    'error': f"Anchor '#{anchor}' not found",
                    'suggestion': f"Available anchors: {', '.join(potential_anchors[:5])}"
                }
                
        except Exception as e:
            return {
                'status': 'error',
                'error': f"Could not read file: {e}",
                'suggestion': "Check file permissions and encoding"
            }
    
    def validate_link(self, link, file_path):
        """Validate a single link"""
        if link['type'] == 'local':
            return self.validate_local_link(link, file_path)
        elif link['type'] == 'external':
            return self.validate_external_link(link)
        elif link['type'] == 'anchor':
            return self.validate_anchor_link(link, file_path)
        elif link['type'] == 'email':
            return {'status': 'valid', 'error': None}  # Skip email validation
        else:
            return {
                'status': 'warning',
                'error': f"Unknown link type: {link['type']}",
                'suggestion': "Check link format"
            }
    
    def process_file(self, file_path):
        """Process a single markdown file"""
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            links = self.extract_links_from_content(content, file_path)
            file_results = {
                'file': str(file_path),
                'total_links': len(links),
                'valid_links': 0,
                'broken_links': 0,
                'warning_links': 0,
                'error_links': 0,
                'links': []
            }
            
            for link in links:
                validation_result = self.validate_link(link, file_path)
                
                link_result = {
                    'text': link['text'],
                    'url': link['url'],
                    'line': link['line'],
                    'type': link['type'],
                    'status': validation_result['status'],
                    'error': validation_result.get('error'),
                    'suggestion': validation_result.get('suggestion'),
                    'status_code': validation_result.get('status_code')
                }
                
                file_results['links'].append(link_result)
                
                # Count by status
                if validation_result['status'] == 'valid':
                    file_results['valid_links'] += 1
                elif validation_result['status'] == 'broken':
                    file_results['broken_links'] += 1
                elif validation_result['status'] == 'warning':
                    file_results['warning_links'] += 1
                elif validation_result['status'] == 'error':
                    file_results['error_links'] += 1
            
            return file_results
            
        except Exception as e:
            return {
                'file': str(file_path),
                'total_links': 0,
                'valid_links': 0,
                'broken_links': 0,
                'warning_links': 0,
                'error_links': 0,
                'links': [],
                'error': f"Could not process file: {e}"
            }
    
    def run_validation(self):
        """Run validation on all markdown files"""
        print("🔍 Starting link validation...")
        print(f"📁 Scanning directory: {self.docs_dir}")
        print()
        
        # Find all markdown files
        markdown_files = list(self.docs_dir.glob("**/*.md"))
        
        # Filter out README.md and agent-prompts.md as requested
        markdown_files = [f for f in markdown_files if f.name not in ['README.md', 'agent-prompts.md']]
        
        print(f"📄 Found {len(markdown_files)} markdown files to process")
        print()
        
        for file_path in markdown_files:
            file_results = self.process_file(file_path)
            self.results[str(file_path)] = file_results
        
        return self.results
    
    def generate_report(self):
        """Generate a comprehensive report"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = []
        report.append("# Link Validation Report")
        report.append(f"**Generated:** {timestamp}")
        report.append(f"**Base Directory:** {self.base_dir}")
        report.append("")
        
        # Summary statistics
        total_files = len(self.results)
        total_links = sum(r['total_links'] for r in self.results.values())
        total_valid = sum(r['valid_links'] for r in self.results.values())
        total_broken = sum(r['broken_links'] for r in self.results.values())
        total_warnings = sum(r['warning_links'] for r in self.results.values())
        total_errors = sum(r['error_links'] for r in self.results.values())
        
        report.append("## 📊 Summary")
        report.append(f"- **Files processed:** {total_files}")
        report.append(f"- **Total links:** {total_links}")
        report.append(f"- **✅ Valid links:** {total_valid}")
        report.append(f"- **❌ Broken links:** {total_broken}")
        report.append(f"- **⚠️ Warning links:** {total_warnings}")
        report.append(f"- **🚫 Error links:** {total_errors}")
        report.append("")
        
        # Files with issues
        files_with_issues = {k: v for k, v in self.results.items() 
                           if v['broken_links'] > 0 or v['warning_links'] > 0 or v['error_links'] > 0}
        
        if files_with_issues:
            report.append("## 🚨 Files with Issues")
            report.append("")
            
            for file_path, file_results in files_with_issues.items():
                relative_path = Path(file_path).relative_to(self.base_dir)
                report.append(f"### {relative_path}")
                report.append(f"- **Total links:** {file_results['total_links']}")
                report.append(f"- **✅ Valid:** {file_results['valid_links']}")
                report.append(f"- **❌ Broken:** {file_results['broken_links']}")
                report.append(f"- **⚠️ Warnings:** {file_results['warning_links']}")
                report.append(f"- **🚫 Errors:** {file_results['error_links']}")
                report.append("")
                
                # List problematic links
                problematic_links = [l for l in file_results['links'] 
                                   if l['status'] in ['broken', 'warning', 'error']]
                
                if problematic_links:
                    report.append("**Issues:**")
                    for link in problematic_links:
                        status_emoji = {
                            'broken': '❌',
                            'warning': '⚠️',
                            'error': '🚫'
                        }.get(link['status'], '❓')
                        
                        report.append(f"- {status_emoji} **Line {link['line']}:** `{link['text']}` → `{link['url']}`")
                        if link['error']:
                            report.append(f"  - **Error:** {link['error']}")
                        if link['suggestion']:
                            report.append(f"  - **Suggestion:** {link['suggestion']}")
                        if link.get('status_code'):
                            report.append(f"  - **HTTP Status:** {link['status_code']}")
                        report.append("")
                report.append("")
        else:
            report.append("## ✅ All Links Valid!")
            report.append("No broken, warning, or error links found.")
            report.append("")
        
        # All files summary
        report.append("## 📋 All Files Summary")
        report.append("")
        
        for file_path, file_results in sorted(self.results.items()):
            relative_path = Path(file_path).relative_to(self.base_dir)
            status_emoji = "✅" if file_results['broken_links'] == 0 and file_results['warning_links'] == 0 and file_results['error_links'] == 0 else "⚠️"
            
            report.append(f"- {status_emoji} **{relative_path}**")
            report.append(f"  - Links: {file_results['total_links']} (✅{file_results['valid_links']} ❌{file_results['broken_links']} ⚠️{file_results['warning_links']} 🚫{file_results['error_links']})")
        
        return "\n".join(report)
    
    def save_report(self, report):
        """Save report to file"""
        timestamp = datetime.now().strftime("%Y-%m-%d")
        filename = f"link-validation-report-{timestamp}.md"
        filepath = self.docs_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📄 Report saved to: {filepath}")
        return filepath

def main():
    """Main function"""
    validator = LinkValidator()
    
    # Run validation
    results = validator.run_validation()
    
    # Generate and save report
    report = validator.generate_report()
    report_file = validator.save_report(report)
    
    # Print summary
    print("\n" + "="*60)
    print("📊 VALIDATION COMPLETE")
    print("="*60)
    
    total_files = len(results)
    total_links = sum(r['total_links'] for r in results.values())
    total_valid = sum(r['valid_links'] for r in results.values())
    total_broken = sum(r['broken_links'] for r in results.values())
    total_warnings = sum(r['warning_links'] for r in results.values())
    total_errors = sum(r['error_links'] for r in results.values())
    
    print(f"📁 Files processed: {total_files}")
    print(f"🔗 Total links: {total_links}")
    print(f"✅ Valid links: {total_valid}")
    print(f"❌ Broken links: {total_broken}")
    print(f"⚠️ Warning links: {total_warnings}")
    print(f"🚫 Error links: {total_errors}")
    print(f"📄 Report saved: {report_file}")
    
    if total_broken > 0 or total_warnings > 0 or total_errors > 0:
        print("\n⚠️ Some links need attention! Check the report for details.")
        return 1
    else:
        print("\n🎉 All links are valid!")
        return 0

if __name__ == "__main__":
    exit(main())