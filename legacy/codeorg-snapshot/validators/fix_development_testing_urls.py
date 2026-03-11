#!/usr/bin/env python3
"""
Fix broken GitHub URLs in development-testing.md by replacing with RubyGems URLs.
"""

import re
from pathlib import Path

def fix_development_testing_urls():
    """Fix broken GitHub URLs in development-testing.md"""
    file_path = Path("/workspace/docs/dependencies/gemfile-dependencies/development-testing.md")
    
    # Broken URLs and their RubyGems replacements
    url_fixes = {
        "https://github.com/rubocop/rubocop-rails-accessibility": "https://rubygems.org/gems/rubocop-rails-accessibility",
        "https://github.com/castwide/debugger": "https://rubygems.org/gems/debugger",
        "https://github.com/wojtekmach/minitest-spec-context": "https://rubygems.org/gems/minitest-spec-context",
        "https://github.com/wojtekmach/minitest-stub-const": "https://rubygems.org/gems/minitest-stub-const",
        "https://github.com/applitools/eyes.sdk.ruby": "https://rubygems.org/gems/eyes_selenium",
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
    fix_development_testing_urls()