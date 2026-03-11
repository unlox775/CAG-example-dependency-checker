#!/usr/bin/env python3
"""
Fix the final missing documentation links.
"""

import re
from pathlib import Path

def fix_final_docs():
    """Fix the final missing documentation links"""
    base_dir = Path("/workspace/docs/dependencies")
    
    # Dependencies and their documentation links
    doc_fixes = {
        # authentication-authorization.md
        "omniauth-microsoft_v2_auth": {
            "file": "gemfile-dependencies/authentication-authorization.md",
            "old": "Omniauth Microsoft V2 Auth | GitHub",
            "new": "[Omniauth Microsoft V2 Auth](https://github.com/KonaTeam/omniauth-microsoft_v2_auth) | [GitHub](https://github.com/KonaTeam/omniauth-microsoft_v2_auth)"
        },
        
        # database-caching.md
        "active_record_union": {
            "file": "gemfile-dependencies/database-caching.md",
            "old": "Active Record Union | GitHub",
            "new": "[Active Record Union](https://github.com/brianmario/active_record_union) | [GitHub](https://github.com/brianmario/active_record_union)"
        },
        "paranoia": {
            "file": "gemfile-dependencies/database-caching.md",
            "old": "Paranoia | GitHub",
            "new": "[Paranoia](https://github.com/benmorgan/paranoia) | [GitHub](https://github.com/benmorgan/paranoia)"
        },
        
        # web-server-middleware.md
        "sd_notify": {
            "file": "gemfile-dependencies/web-server-middleware.md",
            "old": "SD Notify | GitHub",
            "new": "[SD Notify](https://rubygems.org/gems/sd_notify) | [GitHub](https://rubygems.org/gems/sd_notify)"
        },
        
        # monitoring-logging.md
        "sd_notify_github": {
            "file": "gemfile-dependencies/monitoring-logging.md",
            "old": "SD Notify | GitHub",
            "new": "[SD Notify](https://rubygems.org/gems/sd_notify) | [GitHub](https://rubygems.org/gems/sd_notify)"
        }
    }
    
    total_fixes = 0
    
    for dep_name, fix_info in doc_fixes.items():
        file_path = base_dir / fix_info["file"]
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            if fix_info["old"] in content:
                content = content.replace(fix_info["old"], fix_info["new"])
                print(f"  🔗 Fixed: {fix_info['old']} -> {fix_info['new']}")
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✅ Updated {file_path}")
                total_fixes += 1
            else:
                print(f"  ⏭️  No changes needed")
                
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    print(f"\n✅ Applied {total_fixes} total documentation fixes!")

if __name__ == "__main__":
    fix_final_docs()