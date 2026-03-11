#!/usr/bin/env python3
"""
Fix the final broken links by replacing with RubyGems URLs.
"""

import re
from pathlib import Path

def fix_final_links():
    """Fix the final broken links"""
    base_dir = Path("/workspace/docs/dependencies")
    
    # Broken URLs and their RubyGems replacements
    url_fixes = {
        "https://github.com/ksss/xxhash": "https://rubygems.org/gems/xxhash",
        "https://github.com/redis-store/redis-slave-read": "https://rubygems.org/gems/redis-slave-read",
    }
    
    # Find all markdown files
    markdown_files = list(base_dir.glob("**/*.md"))
    markdown_files = [f for f in markdown_files if f.name not in ['README.md', 'agent-prompts.md']]
    
    total_fixes = 0
    
    for file_path in markdown_files:
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes_in_file = 0
            
            # Apply URL fixes
            for old_url, new_url in url_fixes.items():
                if old_url in content:
                    content = content.replace(old_url, new_url)
                    print(f"  🔗 Fixed: {old_url} -> {new_url}")
                    fixes_in_file += 1
            
            # Write back if changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✅ Updated {file_path}")
            else:
                print(f"  ⏭️  No changes needed")
            
            total_fixes += fixes_in_file
                
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    print(f"\n✅ Applied {total_fixes} total URL fixes!")

if __name__ == "__main__":
    fix_final_links()