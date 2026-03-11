#!/usr/bin/env python3
"""
Fix all remaining missing documentation links.
"""

import re
from pathlib import Path

def fix_remaining_docs():
    """Fix all remaining missing documentation links"""
    base_dir = Path("/workspace/docs/dependencies")
    
    # Dependencies and their documentation links
    doc_fixes = {
        # other-utilities.md
        "XXHash | GitHub": "[XXHash](https://github.com/ksss/xxhash) | [GitHub](https://github.com/ksss/xxhash)",
        
        # ruby-version-compatibility.md
        "Sorted Set | GitHub": "[Sorted Set](https://rubygems.org/gems/sorted_set) | [GitHub](https://rubygems.org/gems/sorted_set)",
        
        # authentication-authorization.md
        "Omniauth Microsoft V2 Auth | GitHub": "[Omniauth Microsoft V2 Auth](https://github.com/KonaTeam/omniauth-microsoft_v2_auth) | [GitHub](https://github.com/KonaTeam/omniauth-microsoft_v2_auth)",
        
        # database-caching.md
        "Redis Slave Read | GitHub": "[Redis Slave Read](https://github.com/redis-store/redis-slave-read) | [GitHub](https://github.com/redis-store/redis-slave-read)",
        "Active Record Union | GitHub": "[Active Record Union](https://github.com/brianmario/active_record_union) | [GitHub](https://github.com/brianmario/active_record_union)",
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
            
            # Apply documentation fixes
            for old_text, new_text in doc_fixes.items():
                if old_text in content:
                    content = content.replace(old_text, new_text)
                    print(f"  🔗 Fixed: {old_text} -> {new_text}")
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
    
    print(f"\n✅ Applied {total_fixes} total documentation fixes!")

if __name__ == "__main__":
    fix_remaining_docs()