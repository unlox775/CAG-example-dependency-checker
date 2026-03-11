#!/usr/bin/env python3
"""
Comprehensive link fixer to resolve all remaining broken links.

This script handles:
1. External URLs that return 404 (find correct URLs or remove)
2. Directory references instead of files (find actual files)
3. Missing documentation files (create or update references)
4. All other broken link types
"""

import os
import re
import glob
import requests
import time
from pathlib import Path

class ComprehensiveLinkFixer:
    def __init__(self, base_dir="/workspace"):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs" / "dependencies"
        self.fixes_applied = 0
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Code.org Link Fixer 2.0'
        })
        
    def rate_limit(self):
        """Simple rate limiting"""
        time.sleep(0.3)
    
    def find_correct_github_url(self, broken_url):
        """Find the correct GitHub URL for broken links"""
        # Common fixes for GitHub URLs
        url_fixes = {
            # Blockly samples fixes
            "https://github.com/google/blockly-samples/tree/main/plugins/block-shareable-procedures": "https://github.com/google/blockly-samples/tree/main/plugins/procedures",
            "https://github.com/google/blockly-samples/tree/main/plugins/field-bitmap": "https://github.com/google/blockly-samples/tree/main/plugins/field-bitmap",
            "https://github.com/google/blockly-samples/tree/main/plugins/field-colour": "https://github.com/google/blockly-samples/tree/main/plugins/field-colour",
            "https://github.com/google/blockly-samples/tree/main/plugins/field-grid-dropdown": "https://github.com/google/blockly-samples/tree/main/plugins/field-grid-dropdown",
            "https://github.com/google/blockly-samples/tree/main/plugins/keyboard-navigation": "https://github.com/google/blockly-samples/tree/main/plugins/keyboard-navigation",
            "https://github.com/google/blockly-samples/tree/main/plugins/cross-tab-copy-paste": "https://github.com/google/blockly-samples/tree/main/plugins/cross-tab-copy-paste",
            "https://github.com/google/blockly-samples/tree/main/plugins/scroll-options": "https://github.com/google/blockly-samples/tree/main/plugins/scroll-options",
            "https://github.com/google/blockly-samples/tree/main/plugins/theme-dark": "https://github.com/google/blockly-samples/tree/main/plugins/theme-dark",
            "https://github.com/google/blockly-samples/tree/main/plugins/theme-highcontrast": "https://github.com/google/blockly-samples/tree/main/plugins/theme-highcontrast",
            
            # CodeMirror fixes
            "https://github.com/codemirror/codemirror6": "https://github.com/codemirror/codemirror",
            
            # Other common fixes
            "https://coverage.readthedocs.io/": "https://coverage.readthedocs.io/en/latest/",
        }
        
        return url_fixes.get(broken_url, None)
    
    def find_actual_file(self, directory_path, filename_hint=None):
        """Find an actual file when given a directory path"""
        dir_path = self.base_dir / directory_path
        
        if not dir_path.exists():
            return None
        
        if dir_path.is_file():
            return dir_path
        
        # Look for common files in the directory
        common_files = [
            "index.js", "index.ts", "index.py", "index.rb",
            "main.js", "main.ts", "main.py", "main.rb",
            "app.js", "app.ts", "app.py", "app.rb",
            "README.md", "readme.md"
        ]
        
        if filename_hint:
            common_files.insert(0, filename_hint)
        
        for filename in common_files:
            file_path = dir_path / filename
            if file_path.exists() and file_path.is_file():
                return file_path
        
        # Look for any file in the directory
        try:
            files = [f for f in dir_path.iterdir() if f.is_file()]
            if files:
                return files[0]  # Return first file found
        except:
            pass
        
        return None
    
    def find_file_by_name(self, filename):
        """Find a file by name anywhere in the codebase"""
        search_dirs = [
            self.base_dir / "apps" / "src",
            self.base_dir / "dashboard",
            self.base_dir / "pegasus",
            self.base_dir / "lib",
            self.base_dir / "python"
        ]
        
        for search_dir in search_dirs:
            if search_dir.exists():
                pattern = f"**/{filename}"
                matches = list(search_dir.glob(pattern))
                if matches:
                    return matches[0]
        
        return None
    
    def fix_external_urls(self, content):
        """Fix external URLs that return 404"""
        fixes_applied = 0
        
        # Pattern to match external URLs
        url_pattern = r'\[([^\]]+)\]\((https://[^)]+)\)'
        
        def fix_url(match):
            link_text = match.group(1)
            url = match.group(2)
            
            # Check if this is a known broken URL
            correct_url = self.find_correct_github_url(url)
            if correct_url:
                print(f"  🔗 Fixing URL: {url} -> {correct_url}")
                return f"[{link_text}]({correct_url})"
            
            # For other URLs, try to verify them
            try:
                self.rate_limit()
                response = self.session.head(url, timeout=5, allow_redirects=True)
                if response.status_code == 200:
                    return match.group(0)  # Keep original if it works
                else:
                    print(f"  ❌ Removing broken URL: {url}")
                    return link_text  # Remove link if broken
            except:
                print(f"  ❌ Removing broken URL: {url}")
                return link_text  # Remove link if can't verify
        
        return re.sub(url_pattern, fix_url, content)
    
    def fix_local_files(self, content, file_path):
        """Fix local file references"""
        file_path_obj = Path(file_path)
        fixes_applied = 0
        
        # Pattern to match local file links
        local_pattern = r'\[([^\]]+)\]\(\.\.\/\.\.\/([^#)]+)(#[^)]+)?\)'
        
        def fix_local_link(match):
            link_text = match.group(1)
            file_path_part = match.group(2)
            anchor_part = match.group(3) or ""
            
            # Check if it's a directory reference
            full_path = self.base_dir / file_path_part
            if full_path.exists() and full_path.is_dir():
                # Find an actual file in the directory
                actual_file = self.find_actual_file(file_path_part)
                if actual_file:
                    relative_path = actual_file.relative_to(self.base_dir)
                    print(f"  📁 Directory -> File: {file_path_part} -> {relative_path}")
                    return f"[{link_text}](../../{relative_path}{anchor_part})"
                else:
                    print(f"  ❌ No file found in directory: {file_path_part}")
                    return link_text  # Remove link
            
            # Check if file exists
            if not full_path.exists():
                # Try to find alternative
                filename = Path(file_path_part).name
                alternative = self.find_file_by_name(filename)
                if alternative:
                    relative_path = alternative.relative_to(self.base_dir)
                    print(f"  📁 Found alternative: {file_path_part} -> {relative_path}")
                    return f"[{link_text}](../../{relative_path}{anchor_part})"
                else:
                    print(f"  ❌ No alternative found: {file_path_part}")
                    return link_text  # Remove link
            
            return match.group(0)  # Keep original if file exists
        
        return re.sub(local_pattern, fix_local_link, content)
    
    def fix_missing_docs(self, content, file_path):
        """Fix references to missing documentation files"""
        # Pattern to match local markdown file references
        doc_pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
        
        def fix_doc_link(match):
            link_text = match.group(1)
            doc_file = match.group(2)
            
            # Check if it's a relative reference
            if not doc_file.startswith('http'):
                doc_path = Path(file_path).parent / doc_file
                if not doc_path.exists():
                    print(f"  📄 Missing doc file: {doc_file}")
                    # Remove the link or replace with text
                    return link_text
        
            return match.group(0)
        
        return re.sub(doc_pattern, fix_doc_link, content)
    
    def fix_markdown_file(self, file_path):
        """Fix all broken links in a markdown file"""
        print(f"Fixing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes_in_file = 0
            
            # Fix external URLs
            content = self.fix_external_urls(content)
            
            # Fix local files
            content = self.fix_local_files(content, file_path)
            
            # Fix missing documentation files
            content = self.fix_missing_docs(content, file_path)
            
            # Count fixes
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✅ Applied fixes to {file_path}")
                self.fixes_applied += 1
            else:
                print(f"  ⏭️  No fixes needed")
                
        except Exception as e:
            print(f"  ❌ Error fixing {file_path}: {e}")
    
    def run_fixes(self):
        """Run fixes on all markdown files"""
        print("🔧 Starting comprehensive link fixes...")
        print(f"📁 Scanning directory: {self.docs_dir}")
        print()
        
        # Find all markdown files
        markdown_files = list(self.docs_dir.glob("**/*.md"))
        
        # Filter out README.md and agent-prompts.md as requested
        markdown_files = [f for f in markdown_files if f.name not in ['README.md', 'agent-prompts.md']]
        
        print(f"📄 Found {len(markdown_files)} markdown files to process")
        print()
        
        for file_path in markdown_files:
            self.fix_markdown_file(file_path)
        
        print()
        print(f"✅ Applied {self.fixes_applied} total fixes!")

def main():
    """Main function"""
    fixer = ComprehensiveLinkFixer()
    fixer.run_fixes()

if __name__ == "__main__":
    main()