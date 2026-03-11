#!/usr/bin/env python3
"""
Fix broken GitHub URLs by finding correct ones or removing them.
"""

import re
from pathlib import Path

def fix_broken_github_urls():
    """Fix broken GitHub URLs"""
    base_dir = Path("/workspace/docs/dependencies")
    
    # Broken URLs and their replacements
    url_fixes = {
        # These GitHub repos don't exist, so we'll remove the links
        "https://github.com/agis/sd_notify": "https://rubygems.org/gems/sd_notify",
        "https://github.com/crowdin/crowdin-ruby-sdk": "https://rubygems.org/gems/crowdin-api",
        "https://github.com/mailjet/mailjet-ruby": "https://rubygems.org/gems/mailjet",
        "https://github.com/localhost/localhost": "https://rubygems.org/gems/localhost",
    }
    
    # Find all markdown files
    markdown_files = list(base_dir.glob("**/*.md"))
    markdown_files = [f for f in markdown_files if f.name not in ['README.md', 'agent-prompts.md']]
    
    fixes_applied = 0
    
    for file_path in markdown_files:
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
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
    fix_broken_github_urls()