#!/usr/bin/env python3
"""
Script to fix broken links in dependency documentation.

This script:
1. Reads the link validation report
2. Identifies broken local links
3. Searches for the actual files in the codebase
4. Updates the documentation with correct paths
"""

import os
import re
import glob
from pathlib import Path
import json

class LinkFixer:
    def __init__(self, base_dir="/workspace"):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs" / "dependencies"
        self.fixes_applied = 0
        
    def find_file_in_codebase(self, filename):
        """Find a file in the codebase by name"""
        # Search in common directories
        search_dirs = [
            self.base_dir / "apps" / "src",
            self.base_dir / "dashboard",
            self.base_dir / "pegasus",
            self.base_dir / "lib",
            self.base_dir / "bin"
        ]
        
        for search_dir in search_dirs:
            if search_dir.exists():
                # Use glob to find files with the same name
                pattern = f"**/{filename}"
                matches = list(search_dir.glob(pattern))
                if matches:
                    return matches[0]  # Return first match
        
        return None
    
    def find_file_by_partial_name(self, partial_name):
        """Find a file by partial name match"""
        search_dirs = [
            self.base_dir / "apps" / "src",
            self.base_dir / "dashboard",
            self.base_dir / "pegasus",
            self.base_dir / "lib"
        ]
        
        for search_dir in search_dirs:
            if search_dir.exists():
                # Search for files containing the partial name
                pattern = f"**/*{partial_name}*"
                matches = list(search_dir.glob(pattern))
                if matches:
                    return matches[0]
        
        return None
    
    def fix_file_path(self, broken_path, file_path):
        """Fix a broken file path by finding the actual file"""
        # Extract filename from broken path
        filename = Path(broken_path).name
        
        # Try to find the file
        actual_file = self.find_file_in_codebase(filename)
        
        if actual_file:
            # Calculate relative path from docs/dependencies to the actual file
            relative_path = actual_file.relative_to(self.base_dir)
            return f"../../{relative_path}"
        
        # If not found, try partial name matching
        partial_name = filename.split('.')[0]  # Remove extension
        actual_file = self.find_file_by_partial_name(partial_name)
        
        if actual_file:
            relative_path = actual_file.relative_to(self.base_dir)
            return f"../../{relative_path}"
        
        return None
    
    def fix_external_url(self, url):
        """Fix common broken external URLs"""
        fixes = {
            # Common GitHub URL fixes
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
        }
        
        return fixes.get(url, url)
    
    def fix_markdown_file(self, file_path):
        """Fix broken links in a markdown file"""
        print(f"Fixing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes_in_file = 0
            
            # Fix local file paths
            # Pattern: [text](../../path/to/file.ext#L123)
            local_pattern = r'\[([^\]]+)\]\(\.\.\/\.\.\/([^#)]+)(#[^)]+)?\)'
            
            def fix_local_link(match):
                link_text = match.group(1)
                file_path_part = match.group(2)
                anchor_part = match.group(3) or ""
                
                # Try to find the actual file
                fixed_path = self.fix_file_path(file_path_part, file_path)
                
                if fixed_path:
                    return f"[{link_text}]({fixed_path}{anchor_part})"
                else:
                    # If we can't find the file, try to find a similar one
                    filename = Path(file_path_part).name
                    similar_file = self.find_file_by_partial_name(filename.split('.')[0])
                    
                    if similar_file:
                        relative_path = similar_file.relative_to(self.base_dir)
                        return f"[{link_text}](../../{relative_path}{anchor_part})"
                    else:
                        return match.group(0)  # Keep original if can't fix
            
            content = re.sub(local_pattern, fix_local_link, content)
            
            # Fix external URLs
            # Pattern: [text](https://...)
            external_pattern = r'\[([^\]]+)\]\((https://[^)]+)\)'
            
            def fix_external_link(match):
                link_text = match.group(1)
                url = match.group(2)
                
                fixed_url = self.fix_external_url(url)
                if fixed_url != url:
                    return f"[{link_text}]({fixed_url})"
                else:
                    return match.group(0)
            
            content = re.sub(external_pattern, fix_external_link, content)
            
            # Count fixes
            if content != original_content:
                fixes_in_file = content.count('../../') - original_content.count('../../')
                if fixes_in_file > 0:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  ✅ Applied {fixes_in_file} fixes")
                    self.fixes_applied += fixes_in_file
                else:
                    print(f"  ⏭️  No fixes needed")
            else:
                print(f"  ⏭️  No fixes needed")
                
        except Exception as e:
            print(f"  ❌ Error fixing {file_path}: {e}")
    
    def run_fixes(self):
        """Run fixes on all markdown files"""
        print("🔧 Starting link fixes...")
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
    fixer = LinkFixer()
    fixer.run_fixes()

if __name__ == "__main__":
    main()