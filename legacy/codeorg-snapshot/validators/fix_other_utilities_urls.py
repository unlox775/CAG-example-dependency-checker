#!/usr/bin/env python3
"""
Fix broken GitHub URLs in other-utilities.md by replacing with RubyGems URLs.
"""

import re
from pathlib import Path

def fix_other_utilities_urls():
    """Fix broken GitHub URLs in other-utilities.md"""
    file_path = Path("/workspace/docs/dependencies/gemfile-dependencies/other-utilities.md")
    
    # Broken URLs and their RubyGems replacements
    url_fixes = {
        "https://github.com/berk/full-name-splitter": "https://rubygems.org/gems/full-name-splitter",
        "https://github.com/berk/sort_alphabetical": "https://rubygems.org/gems/sort_alphabetical",
        "https://github.com/perfectline/validate_url": "https://rubygems.org/gems/validate_url",
        "https://github.com/oivoodoo/retryable": "https://rubygems.org/gems/retryable",
        "https://github.com/renstrom/jumphash": "https://rubygems.org/gems/jumphash",
    }
    
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes_applied = 0
        
        # Apply URL fixes
        for old_url, new_url in url_fixes.items():
            if old_url in content:
                content = content.replace(old_url, new_url)
                print(f"  🔗 Fixed: {old_url} -> {new_url}")
                fixes_applied += 1
        
        # Write back if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Updated {file_path}")
        else:
            print(f"  ⏭️  No changes needed")
            
    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")
    
    print(f"\n✅ Applied {fixes_applied} URL fixes!")

if __name__ == "__main__":
    fix_other_utilities_urls()