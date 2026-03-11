#!/usr/bin/env python3
"""
Script to fix remaining broken links in dependency documentation.

This script handles:
1. External URLs that return 404 (fix master -> main branch)
2. Local files that don't exist (find alternatives or remove)
3. Update documentation with correct links
"""

import os
import re
import glob
from pathlib import Path
import requests
import time

class RemainingLinkFixer:
    def __init__(self, base_dir="/workspace"):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs" / "dependencies"
        self.fixes_applied = 0
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Code.org Link Fixer 1.0'
        })
        
    def rate_limit(self):
        """Simple rate limiting"""
        time.sleep(0.5)
    
    def fix_external_urls(self, content):
        """Fix external URLs that return 404"""
        fixes = {
            # Fix master -> main branch URLs
            "https://github.com/google/blockly-samples/tree/master/": "https://github.com/google/blockly-samples/tree/main/",
            "https://github.com/google/blockly-samples/tree/master/plugins/": "https://github.com/google/blockly-samples/tree/main/plugins/",
            "https://github.com/google/blockly-samples/tree/master/plugins/keyboard-navigation": "https://github.com/google/blockly-samples/tree/main/plugins/keyboard-navigation",
            "https://github.com/google/blockly-samples/tree/master/plugins/theme": "https://github.com/google/blockly-samples/tree/main/plugins/theme",
            "https://github.com/google/blockly-samples/tree/master/plugins/dev-tools": "https://github.com/google/blockly-samples/tree/main/plugins/dev-tools",
            "https://github.com/google/blockly-samples/tree/master/plugins/workspace-search": "https://github.com/google/blockly-samples/tree/main/plugins/workspace-search",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-date": "https://github.com/google/blockly-samples/tree/main/plugins/field-date",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-slider": "https://github.com/google/blockly-samples/tree/main/plugins/field-slider",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-colour": "https://github.com/google/blockly-samples/tree/main/plugins/field-colour",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-multilineinput": "https://github.com/google/blockly-samples/tree/main/plugins/field-multilineinput",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-grid-dropdown": "https://github.com/google/blockly-samples/tree/main/plugins/field-grid-dropdown",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-parameter": "https://github.com/google/blockly-samples/tree/main/plugins/field-parameter",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-textarea": "https://github.com/google/blockly-samples/tree/main/plugins/field-textarea",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-variable": "https://github.com/google/blockly-samples/tree/main/plugins/field-variable",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-image": "https://github.com/google/blockly-samples/tree/main/plugins/field-image",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-button": "https://github.com/google/blockly-samples/tree/main/plugins/field-button",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-dropdown": "https://github.com/google/blockly-samples/tree/main/plugins/field-dropdown",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-number": "https://github.com/google/blockly-samples/tree/main/plugins/field-number",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-textinput": "https://github.com/google/blockly-samples/tree/main/plugins/field-textinput",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-checkbox": "https://github.com/google/blockly-samples/tree/main/plugins/field-checkbox",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-angle": "https://github.com/google/blockly-samples/tree/main/plugins/field-angle",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-label": "https://github.com/google/blockly-samples/tree/main/plugins/field-label",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-toggle": "https://github.com/google/blockly-samples/tree/main/plugins/field-toggle",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-vertical-separator": "https://github.com/google/blockly-samples/tree/main/plugins/field-vertical-separator",
            "https://github.com/google/blockly-samples/tree/master/plugins/field-horizontal-separator": "https://github.com/google/blockly-samples/tree/main/plugins/field-horizontal-separator",
            "https://github.com/google/blockly-samples/tree/master/plugins/block-shareable-procedures": "https://github.com/google/blockly-samples/tree/main/plugins/block-shareable-procedures",
            "https://github.com/google/blockly-samples/tree/master/plugins/block-shareable-procedures": "https://github.com/google/blockly-samples/tree/main/plugins/block-shareable-procedures",
        }
        
        for old_url, new_url in fixes.items():
            if old_url in content:
                content = content.replace(old_url, new_url)
                self.fixes_applied += 1
                print(f"  🔗 Fixed URL: {old_url} -> {new_url}")
        
        return content
    
    def find_alternative_file(self, missing_file):
        """Find an alternative file when the original doesn't exist"""
        filename = Path(missing_file).name
        base_name = filename.split('.')[0]
        
        # Search for similar files
        search_dirs = [
            self.base_dir / "apps" / "src",
            self.base_dir / "dashboard",
            self.base_dir / "pegasus",
            self.base_dir / "lib"
        ]
        
        for search_dir in search_dirs:
            if search_dir.exists():
                # Look for files with similar names
                pattern = f"**/*{base_name}*"
                matches = list(search_dir.glob(pattern))
                if matches:
                    return matches[0]
        
        return None
    
    def fix_local_files(self, content, file_path):
        """Fix local file references that don't exist"""
        file_path_obj = Path(file_path)
        
        # Pattern to match local file links
        local_pattern = r'\[([^\]]+)\]\(\.\.\/\.\.\/([^#)]+)(#[^)]+)?\)'
        
        def fix_local_link(match):
            link_text = match.group(1)
            file_path_part = match.group(2)
            anchor_part = match.group(3) or ""
            
            # Check if file exists
            full_path = self.base_dir / file_path_part
            if not full_path.exists():
                # Try to find alternative
                alternative = self.find_alternative_file(file_path_part)
                if alternative:
                    relative_path = alternative.relative_to(self.base_dir)
                    print(f"  📁 Found alternative: {file_path_part} -> {relative_path}")
                    return f"[{link_text}](../../{relative_path}{anchor_part})"
                else:
                    # Remove the link if no alternative found
                    print(f"  ❌ No alternative found for: {file_path_part}")
                    return link_text  # Return just the text without link
            else:
                return match.group(0)  # Keep original if file exists
        
        return re.sub(local_pattern, fix_local_link, content)
    
    def fix_markdown_file(self, file_path):
        """Fix broken links in a markdown file"""
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
            
            # Count fixes
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✅ Applied fixes to {file_path}")
            else:
                print(f"  ⏭️  No fixes needed")
                
        except Exception as e:
            print(f"  ❌ Error fixing {file_path}: {e}")
    
    def run_fixes(self):
        """Run fixes on all markdown files"""
        print("🔧 Starting remaining link fixes...")
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
    fixer = RemainingLinkFixer()
    fixer.run_fixes()

if __name__ == "__main__":
    main()