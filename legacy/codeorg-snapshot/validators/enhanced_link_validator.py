#!/usr/bin/env python3
"""
Enhanced Link Validator with Google Search and Agentic Prompts

This script validates all links in the dependency documentation and provides
agentic prompts for fixing broken links with Google search results.
"""

import os
import re
import requests
import time
import json
from pathlib import Path
from urllib.parse import urlparse, quote_plus
from datetime import datetime
from difflib import SequenceMatcher
import glob

class EnhancedLinkValidator:
    def __init__(self, base_dir="/workspace"):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs" / "dependencies"
        self.validators_dir = self.docs_dir / "validators"
        self.results_dir = self.docs_dir / "results"
        self.results_dir.mkdir(exist_ok=True)
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Code.org Enhanced Link Validator 2.0'
        })
        
        # Rate limiting
        self.request_delay = 0.5
        self.last_request_time = 0
        
        # Results storage
        self.results = {}
        self.broken_links = []
        self.missing_docs = []
        self.missing_github = []
        
    def rate_limit(self):
        """Simple rate limiting"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < self.request_delay:
            time.sleep(self.request_delay - time_since_last)
        self.last_request_time = time.time()
    
    def google_search(self, query, num_results=5):
        """Perform Google search and return results"""
        try:
            self.rate_limit()
            
            # Use a simple web search approach
            search_url = f"https://www.google.com/search?q={quote_plus(query)}&num={num_results}"
            
            response = self.session.get(search_url, timeout=10)
            if response.status_code != 200:
                return []
            
            # Parse Google results (simplified)
            content = response.text
            
            # Extract titles and URLs from Google results
            results = []
            
            # Look for result patterns in Google's HTML
            title_pattern = r'<h3[^>]*><a[^>]*href="([^"]*)"[^>]*>([^<]*)</a></h3>'
            matches = re.findall(title_pattern, content)
            
            for url, title in matches[:num_results]:
                if url.startswith('/url?q='):
                    url = url.split('/url?q=')[1].split('&')[0]
                if url.startswith('http'):
                    results.append({
                        'title': title[:50] + '...' if len(title) > 50 else title,
                        'url': url
                    })
            
            return results
            
        except Exception as e:
            print(f"  ⚠️ Google search failed for '{query}': {e}")
            return []
    
    def find_local_files(self, filename, max_results=5):
        """Find local files by name with Levenshtein distance"""
        search_dirs = [
            self.base_dir / "apps" / "src",
            self.base_dir / "dashboard",
            self.base_dir / "pegasus",
            self.base_dir / "lib",
            self.base_dir / "python"
        ]
        
        all_files = []
        for search_dir in search_dirs:
            if search_dir.exists():
                pattern = f"**/*{filename}*"
                matches = list(search_dir.glob(pattern))
                all_files.extend(matches)
        
        # Calculate Levenshtein distance and sort
        file_scores = []
        for file_path in all_files:
            distance = self.levenshtein_distance(filename.lower(), file_path.name.lower())
            file_scores.append((distance, file_path))
        
        # Sort by distance (lower is better)
        file_scores.sort(key=lambda x: x[0])
        
        results = []
        for distance, file_path in file_scores[:max_results]:
            relative_path = file_path.relative_to(self.base_dir)
            results.append({
                'path': str(relative_path),
                'distance': distance,
                'filename': file_path.name
            })
        
        return results
    
    def levenshtein_distance(self, s1, s2):
        """Calculate Levenshtein distance between two strings"""
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = list(range(len(s2) + 1))
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
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
            relative_path = file_part[6:]  # Remove ../../ prefix
            target_path = self.base_dir / relative_path
        elif file_part.startswith('../'):
            relative_path = file_part[3:]
            target_path = file_path_obj.parent / relative_path
        elif file_part.startswith('./'):
            relative_path = file_part[2:]
            target_path = file_path_obj.parent / relative_path
        else:
            target_path = file_path_obj.parent / file_part
        
        # Check if file exists
        if not target_path.exists():
            return {
                'status': 'broken',
                'error': f"File does not exist: {target_path}",
                'error_type': 'missing_file',
                'filename': Path(file_part).name,
                'suggestion': f"Check if file path is correct"
            }
        
        # Check if it's a directory
        if target_path.is_dir():
            return {
                'status': 'broken',
                'error': f"Path is a directory: {target_path}",
                'error_type': 'directory_reference',
                'filename': Path(file_part).name,
                'suggestion': f"Find actual file in directory"
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
                    'error_type': 'invalid_line_number',
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
                    'error_type': 'line_number_too_high',
                    'suggestion': f"Check if line number is correct (max: {len(lines)})"
                }
            elif line_number < 1:
                return {
                    'status': 'broken',
                    'error': f"Invalid line number: {line_number}",
                    'error_type': 'invalid_line_number',
                    'suggestion': "Line numbers must be >= 1"
                }
            else:
                return {'status': 'valid', 'error': None}
                
        except Exception as e:
            return {
                'status': 'error',
                'error': f"Could not read file: {e}",
                'error_type': 'file_read_error',
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
                            'error_type': 'package_name_missing',
                            'http_status': response.status_code,
                            'suggestion': f"Verify this is the correct URL for {package_name}"
                        }
                
                return {
                    'status': 'valid',
                    'error': None,
                    'http_status': response.status_code
                }
            else:
                return {
                    'status': 'broken',
                    'error': f"HTTP {response.status_code}",
                    'error_type': f'http_{response.status_code}',
                    'http_status': response.status_code,
                    'suggestion': "Check if URL is correct and accessible"
                }
                
        except requests.exceptions.Timeout:
            return {
                'status': 'error',
                'error': "Request timeout",
                'error_type': 'timeout',
                'suggestion': "URL may be slow or unreachable"
            }
        except requests.exceptions.ConnectionError:
            return {
                'status': 'error',
                'error': "Connection error",
                'error_type': 'connection_error',
                'suggestion': "Check internet connection and URL"
            }
        except Exception as e:
            return {
                'status': 'error',
                'error': f"Unexpected error: {e}",
                'error_type': 'unexpected_error',
                'suggestion': "Check URL format and accessibility"
            }
    
    def extract_package_name_from_url(self, url):
        """Extract package name from URL for validation"""
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
    
    def check_documentation_links(self, content, file_path):
        """Check if documentation has required links"""
        issues = []
        
        # Look for dependency entries
        dependency_pattern = r'- \[x\] \*\*([^*]+)\*\* \([^)]+\)'
        dependencies = re.findall(dependency_pattern, content)
        
        for dep in dependencies:
            dep_name = dep.strip()
            
            # Check if this dependency has documentation and GitHub links
            dep_section = self.extract_dependency_section(content, dep_name)
            if dep_section:
                if not self.has_documentation_link(dep_section):
                    issues.append({
                        'type': 'missing_documentation',
                        'dependency': dep_name,
                        'file': file_path,
                        'suggestion': f"Add documentation link for {dep_name}"
                    })
                
                if not self.has_github_link(dep_section):
                    issues.append({
                        'type': 'missing_github',
                        'dependency': dep_name,
                        'file': file_path,
                        'suggestion': f"Add GitHub link for {dep_name}"
                    })
        
        return issues
    
    def extract_dependency_section(self, content, dep_name):
        """Extract the section for a specific dependency"""
        # Find the dependency entry
        dep_pattern = rf'- \[x\] \*\*{re.escape(dep_name)}\*\* \([^)]+\)'
        match = re.search(dep_pattern, content)
        if not match:
            return None
        
        start = match.start()
        
        # Find the next dependency or end of content
        next_dep_pattern = r'- \[x\] \*\*[^*]+\*\* \([^)]+\)'
        next_match = re.search(next_dep_pattern, content[start + 1:])
        
        if next_match:
            end = start + 1 + next_match.start()
        else:
            end = len(content)
        
        return content[start:end]
    
    def has_documentation_link(self, section):
        """Check if section has documentation link"""
        doc_patterns = [
            r'Documentation.*?\[([^\]]+)\]\(([^)]+)\)',
            r'Docs.*?\[([^\]]+)\]\(([^)]+)\)',
            r'https://[^\\s]+docs[^\\s]*',
            r'https://[^\\s]+documentation[^\\s]*'
        ]
        
        for pattern in doc_patterns:
            if re.search(pattern, section, re.IGNORECASE):
                return True
        return False
    
    def has_github_link(self, section):
        """Check if section has GitHub link"""
        github_patterns = [
            r'GitHub.*?\[([^\]]+)\]\(([^)]+)\)',
            r'https://github\.com/[^\\s]+',
            r'\[([^\]]+)\]\(https://github\.com/[^)]+\)'
        ]
        
        for pattern in github_patterns:
            if re.search(pattern, section, re.IGNORECASE):
                return True
        return False
    
    def process_file(self, file_path):
        """Process a single markdown file"""
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            links = self.extract_links_from_content(content, file_path)
            doc_issues = self.check_documentation_links(content, file_path)
            
            file_results = {
                'file': str(file_path),
                'total_links': len(links),
                'valid_links': 0,
                'broken_links': 0,
                'warning_links': 0,
                'error_links': 0,
                'doc_issues': len(doc_issues),
                'links': [],
                'documentation_issues': doc_issues
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
                    'error_type': validation_result.get('error_type'),
                    'suggestion': validation_result.get('suggestion'),
                    'http_status': validation_result.get('http_status')
                }
                
                file_results['links'].append(link_result)
                
                # Count by status
                if validation_result['status'] == 'valid':
                    file_results['valid_links'] += 1
                elif validation_result['status'] == 'broken':
                    file_results['broken_links'] += 1
                    self.broken_links.append(link_result)
                elif validation_result['status'] == 'warning':
                    file_results['warning_links'] += 1
                elif validation_result['status'] == 'error':
                    file_results['error_links'] += 1
            
            # Add documentation issues
            for issue in doc_issues:
                if issue['type'] == 'missing_documentation':
                    self.missing_docs.append(issue)
                elif issue['type'] == 'missing_github':
                    self.missing_github.append(issue)
            
            return file_results
            
        except Exception as e:
            return {
                'file': str(file_path),
                'total_links': 0,
                'valid_links': 0,
                'broken_links': 0,
                'warning_links': 0,
                'error_links': 0,
                'doc_issues': 0,
                'links': [],
                'documentation_issues': [],
                'error': f"Could not process file: {e}"
            }
    
    def validate_link(self, link, file_path):
        """Validate a single link"""
        if link['type'] == 'local':
            return self.validate_local_link(link, file_path)
        elif link['type'] == 'external':
            return self.validate_external_link(link)
        elif link['type'] == 'anchor':
            return {'status': 'valid', 'error': None}  # Skip anchor validation for now
        elif link['type'] == 'email':
            return {'status': 'valid', 'error': None}  # Skip email validation
        else:
            return {
                'status': 'warning',
                'error': f"Unknown link type: {link['type']}",
                'error_type': 'unknown_type',
                'suggestion': "Check link format"
            }
    
    def run_validation(self):
        """Run validation on all markdown files"""
        print("🔍 Starting enhanced link validation...")
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
    
    def generate_agentic_prompt(self):
        """Generate agentic prompt with Google search results"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get top 5 broken links
        top_issues = []
        
        # Add broken links
        for link in self.broken_links[:5]:
            issue = {
                'type': 'broken_link',
                'text': link['text'],
                'url': link['url'],
                'error': link['error'],
                'error_type': link['error_type'],
                'http_status': link.get('http_status'),
                'suggestions': []
            }
            
            # Generate suggestions based on error type
            if link['error_type'] == 'missing_file':
                # Search for local files
                filename = link.get('filename', '')
                if filename:
                    local_results = self.find_local_files(filename)
                    issue['suggestions'] = local_results[:5]
            elif link['error_type'] in ['http_404', 'http_500', 'http_403']:
                # Search Google for the package
                package_name = self.extract_package_name_from_url(link['url'])
                if package_name:
                    search_results = self.google_search(f"{package_name} documentation")
                    issue['suggestions'] = search_results
                else:
                    search_results = self.google_search(f"{link['text']} documentation")
                    issue['suggestions'] = search_results
            elif link['error_type'] == 'directory_reference':
                # Search for files in the directory
                filename = link.get('filename', '')
                if filename:
                    local_results = self.find_local_files(filename)
                    issue['suggestions'] = local_results[:5]
            
            top_issues.append(issue)
        
        # Add missing documentation issues
        for issue in self.missing_docs[:5-len(top_issues)]:
            search_results = self.google_search(f"{issue['dependency']} documentation")
            issue['suggestions'] = search_results
            top_issues.append(issue)
        
        # Add missing GitHub issues
        for issue in self.missing_github[:5-len(top_issues)]:
            search_results = self.google_search(f"{issue['dependency']} github")
            issue['suggestions'] = search_results
            top_issues.append(issue)
        
        # Generate prompt
        prompt_lines = [
            f"# Agentic Link Fixing Prompt - {timestamp}",
            "",
            "## Instructions",
            "Fix the following broken links and missing documentation. Use the provided suggestions or search for alternatives.",
            "",
            "## Top 5 Issues to Fix:",
            ""
        ]
        
        for i, issue in enumerate(top_issues[:5], 1):
            prompt_lines.append(f"### {i}. {issue['type'].replace('_', ' ').title()}")
            
            if issue['type'] == 'broken_link':
                prompt_lines.append(f"- **Text**: {issue['text']}")
                prompt_lines.append(f"- **URL**: {issue['url']}")
                prompt_lines.append(f"- **Error**: {issue['error']}")
                if issue.get('http_status'):
                    prompt_lines.append(f"- **HTTP Status**: {issue['http_status']}")
            elif issue['type'] == 'missing_documentation':
                prompt_lines.append(f"- **Dependency**: {issue['dependency']}")
                prompt_lines.append(f"- **File**: {issue['file']}")
                prompt_lines.append(f"- **Issue**: Missing documentation link")
            elif issue['type'] == 'missing_github':
                prompt_lines.append(f"- **Dependency**: {issue['dependency']}")
                prompt_lines.append(f"- **File**: {issue['file']}")
                prompt_lines.append(f"- **Issue**: Missing GitHub link")
            
            if issue['suggestions']:
                prompt_lines.append("- **Suggestions**:")
                for j, suggestion in enumerate(issue['suggestions'][:5], 1):
                    if isinstance(suggestion, dict):
                        if 'title' in suggestion and 'url' in suggestion:
                            prompt_lines.append(f"  {j}. {suggestion['title']} - {suggestion['url']}")
                        elif 'path' in suggestion:
                            distance = suggestion.get('distance', 0)
                            prompt_lines.append(f"  {j}. {suggestion['path']} (distance: {distance})")
                        else:
                            prompt_lines.append(f"  {j}. {str(suggestion)}")
                    else:
                        prompt_lines.append(f"  {j}. {str(suggestion)}")
            else:
                prompt_lines.append("- **Suggestions**: None found")
            
            prompt_lines.append("")
        
        return "\n".join(prompt_lines)
    
    def generate_summary_report(self):
        """Generate summary report for console output"""
        total_files = len(self.results)
        total_links = sum(r['total_links'] for r in self.results.values())
        total_valid = sum(r['valid_links'] for r in self.results.values())
        total_broken = sum(r['broken_links'] for r in self.results.values())
        total_warnings = sum(r['warning_links'] for r in self.results.values())
        total_errors = sum(r['error_links'] for r in self.results.values())
        total_doc_issues = sum(r['doc_issues'] for r in self.results.values())
        
        summary = f"""
📊 LINK VALIDATION SUMMARY
========================
📁 Files processed: {total_files}
🔗 Total links: {total_links}
✅ Valid links: {total_valid}
❌ Broken links: {total_broken}
⚠️ Warning links: {total_warnings}
🚫 Error links: {total_errors}
📄 Documentation issues: {total_doc_issues}
"""
        
        return summary
    
    def save_results(self):
        """Save results to files"""
        timestamp = datetime.now().strftime("%Y-%m-%d")
        
        # Clean up old results
        for old_file in self.results_dir.glob("*.txt"):
            old_file.unlink()
        
        # Save agentic prompt
        prompt = self.generate_agentic_prompt()
        prompt_file = self.results_dir / f"agentic-prompt-{timestamp}.txt"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
        
        # Save full report
        report = self.generate_full_report()
        report_file = self.results_dir / f"full-report-{timestamp}.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📄 Results saved to: {self.results_dir}")
        return prompt_file, report_file
    
    def generate_full_report(self):
        """Generate full detailed report"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report_lines = [
            f"# Enhanced Link Validation Report - {timestamp}",
            f"**Base Directory:** {self.base_dir}",
            "",
            "## 📊 Summary"
        ]
        
        total_files = len(self.results)
        total_links = sum(r['total_links'] for r in self.results.values())
        total_valid = sum(r['valid_links'] for r in self.results.values())
        total_broken = sum(r['broken_links'] for r in self.results.values())
        total_warnings = sum(r['warning_links'] for r in self.results.values())
        total_errors = sum(r['error_links'] for r in self.results.values())
        total_doc_issues = sum(r['doc_issues'] for r in self.results.values())
        
        report_lines.extend([
            f"- **Files processed:** {total_files}",
            f"- **Total links:** {total_links}",
            f"- **✅ Valid links:** {total_valid}",
            f"- **❌ Broken links:** {total_broken}",
            f"- **⚠️ Warning links:** {total_warnings}",
            f"- **🚫 Error links:** {total_errors}",
            f"- **📄 Documentation issues:** {total_doc_issues}",
            ""
        ])
        
        # Add detailed results for each file
        for file_path, file_results in self.results.items():
            if file_results['broken_links'] > 0 or file_results['error_links'] > 0 or file_results['doc_issues'] > 0:
                relative_path = Path(file_path).relative_to(self.base_dir)
                report_lines.extend([
                    f"## {relative_path}",
                    f"- **Total links:** {file_results['total_links']}",
                    f"- **✅ Valid:** {file_results['valid_links']}",
                    f"- **❌ Broken:** {file_results['broken_links']}",
                    f"- **⚠️ Warnings:** {file_results['warning_links']}",
                    f"- **🚫 Errors:** {file_results['error_links']}",
                    f"- **📄 Doc issues:** {file_results['doc_issues']}",
                    ""
                ])
                
                # Add broken links
                broken_links = [l for l in file_results['links'] if l['status'] == 'broken']
                if broken_links:
                    report_lines.append("**Broken Links:**")
                    for link in broken_links:
                        report_lines.append(f"- **Line {link['line']}:** `{link['text']}` → `{link['url']}`")
                        report_lines.append(f"  - **Error:** {link['error']}")
                        if link.get('http_status'):
                            report_lines.append(f"  - **HTTP Status:** {link['http_status']}")
                        report_lines.append("")
                
                # Add documentation issues
                if file_results['documentation_issues']:
                    report_lines.append("**Documentation Issues:**")
                    for issue in file_results['documentation_issues']:
                        report_lines.append(f"- **{issue['type']}:** {issue['dependency']}")
                        report_lines.append(f"  - **Suggestion:** {issue['suggestion']}")
                        report_lines.append("")
        
        return "\n".join(report_lines)

def main():
    """Main function"""
    validator = EnhancedLinkValidator()
    
    # Run validation
    results = validator.run_validation()
    
    # Generate and save results
    prompt_file, report_file = validator.save_results()
    
    # Print summary
    summary = validator.generate_summary_report()
    print(summary)
    
    # Print agentic prompt
    print("\n" + "="*60)
    print("🤖 AGENTIC PROMPT")
    print("="*60)
    with open(prompt_file, 'r', encoding='utf-8') as f:
        print(f.read())
    
    # Check if we need to create blocked file
    total_issues = len(validator.broken_links) + len(validator.missing_docs) + len(validator.missing_github)
    if total_issues > 0:
        return 1
    else:
        print("\n🎉 All links are valid!")
        return 0

if __name__ == "__main__":
    exit(main())