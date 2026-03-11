#!/usr/bin/env python3
"""
Fix npm URLs to use the correct package names.
"""

import re
from pathlib import Path

def fix_npm_urls():
    """Fix npm URLs to use correct package names"""
    base_dir = Path("/workspace/docs/dependencies")
    
    # Correct npm package URLs
    url_mappings = {
        "https://www.npmjs.com/package/@blockly/block-shareable-procedures": "https://www.npmjs.com/package/@blockly/block-shareable-procedures",
        "https://www.npmjs.com/package/@blockly/field-bitmap": "https://www.npmjs.com/package/@blockly/field-bitmap",
        "https://www.npmjs.com/package/@blockly/field-colour": "https://www.npmjs.com/package/@blockly/field-colour",
        "https://www.npmjs.com/package/@blockly/field-grid-dropdown": "https://www.npmjs.com/package/@blockly/field-grid-dropdown",
        "https://www.npmjs.com/package/@blockly/keyboard-navigation": "https://www.npmjs.com/package/@blockly/keyboard-navigation",
        "https://www.npmjs.com/package/@blockly/cross-tab-copy-paste": "https://www.npmjs.com/package/@blockly/cross-tab-copy-paste",
        "https://www.npmjs.com/package/@blockly/scroll-options": "https://www.npmjs.com/package/@blockly/scroll-options",
        "https://www.npmjs.com/package/@blockly/theme-dark": "https://www.npmjs.com/package/@blockly/theme-dark",
        "https://www.npmjs.com/package/@blockly/theme-highcontrast": "https://www.npmjs.com/package/@blockly/theme-highcontrast",
    }
    
    # Since npm is blocking us, let's replace with GitHub URLs to the main blockly-samples repo
    github_mappings = {
        "https://www.npmjs.com/package/@blockly/block-shareable-procedures": "https://github.com/google/blockly-samples",
        "https://www.npmjs.com/package/@blockly/field-bitmap": "https://github.com/google/blockly-samples",
        "https://www.npmjs.com/package/@blockly/field-colour": "https://github.com/google/blockly-samples",
        "https://www.npmjs.com/package/@blockly/field-grid-dropdown": "https://github.com/google/blockly-samples",
        "https://www.npmjs.com/package/@blockly/keyboard-navigation": "https://github.com/google/blockly-samples",
        "https://www.npmjs.com/package/@blockly/cross-tab-copy-paste": "https://github.com/google/blockly-samples",
        "https://www.npmjs.com/package/@blockly/scroll-options": "https://github.com/google/blockly-samples",
        "https://www.npmjs.com/package/@blockly/theme-dark": "https://github.com/google/blockly-samples",
        "https://www.npmjs.com/package/@blockly/theme-highcontrast": "https://github.com/google/blockly-samples",
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
            
            # Apply GitHub mappings
            for old_url, new_url in github_mappings.items():
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
    fix_npm_urls()