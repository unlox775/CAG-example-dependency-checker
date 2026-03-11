#!/usr/bin/env python3
"""
Replace broken Blockly GitHub URLs with npm package URLs.
"""

import re
from pathlib import Path

def fix_blockly_to_npm():
    """Replace Blockly GitHub URLs with npm package URLs"""
    base_dir = Path("/workspace/docs/dependencies")
    
    # Mapping from GitHub URLs to npm package URLs
    url_mappings = {
        "https://github.com/google/blockly-samples/tree/main/plugins/block-shareable-procedures": "https://www.npmjs.com/package/@blockly/block-shareable-procedures",
        "https://github.com/google/blockly-samples/tree/main/plugins/field-bitmap": "https://www.npmjs.com/package/@blockly/field-bitmap",
        "https://github.com/google/blockly-samples/tree/main/plugins/field-colour": "https://www.npmjs.com/package/@blockly/field-colour",
        "https://github.com/google/blockly-samples/tree/main/plugins/field-grid-dropdown": "https://www.npmjs.com/package/@blockly/field-grid-dropdown",
        "https://github.com/google/blockly-samples/tree/main/plugins/keyboard-navigation": "https://www.npmjs.com/package/@blockly/keyboard-navigation",
        "https://github.com/google/blockly-samples/tree/main/plugins/cross-tab-copy-paste": "https://www.npmjs.com/package/@blockly/cross-tab-copy-paste",
        "https://github.com/google/blockly-samples/tree/main/plugins/scroll-options": "https://www.npmjs.com/package/@blockly/scroll-options",
        "https://github.com/google/blockly-samples/tree/main/plugins/theme-dark": "https://www.npmjs.com/package/@blockly/theme-dark",
        "https://github.com/google/blockly-samples/tree/main/plugins/theme-highcontrast": "https://www.npmjs.com/package/@blockly/theme-highcontrast",
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
            
            # Apply URL mappings
            for old_url, new_url in url_mappings.items():
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
    fix_blockly_to_npm()