#!/usr/bin/env python3
"""
Script to make key locations in dependency documentation clickable.

This script converts file paths in the format:
- `dashboard/app/models/user.rb:1` - User model

To clickable markdown links:
- [`dashboard/app/models/user.rb:1`](../../dashboard/app/models/user.rb#L1) - User model
"""

import os
import re
import glob
from pathlib import Path

def make_paths_clickable(content, base_path=""):
    """
    Convert file paths to clickable markdown links.
    
    Args:
        content: The markdown content to process
        base_path: Base path for relative links (default: empty for workspace root)
    
    Returns:
        Updated content with clickable links
    """
    # Pattern to match file paths with line numbers
    # Matches: `path/to/file.rb:123` or `path/to/file.rb:1-5`
    pattern = r'`([^`]+\.(?:rb|js|jsx|ts|tsx|py|yml|yaml|json|md|html|haml|scss|css|sql|sh|yml|erb)):(\d+(?:-\d+)?)`'
    
    def replace_path(match):
        file_path = match.group(1)
        line_ref = match.group(2)
        
        # Create relative path from docs/dependencies to the file
        if base_path:
            relative_path = f"../../{file_path}"
        else:
            relative_path = f"../../{file_path}"
        
        # Handle line ranges (e.g., 1-5 becomes #L1-L5)
        if '-' in line_ref:
            start_line, end_line = line_ref.split('-')
            anchor = f"#L{start_line}-L{end_line}"
        else:
            anchor = f"#L{line_ref}"
        
        # Return clickable markdown link
        return f"[`{file_path}:{line_ref}`]({relative_path}{anchor})"
    
    return re.sub(pattern, replace_path, content)

def process_markdown_file(file_path):
    """
    Process a single markdown file to make paths clickable.
    
    Args:
        file_path: Path to the markdown file
    """
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Make paths clickable
        updated_content = make_paths_clickable(content)
        
        # Only write if content changed
        if content != updated_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"  ✅ Updated {file_path}")
        else:
            print(f"  ⏭️  No changes needed for {file_path}")
            
    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")

def main():
    """Main function to process all markdown files in the dependencies directory."""
    dependencies_dir = Path("docs/dependencies")
    
    if not dependencies_dir.exists():
        print(f"Error: {dependencies_dir} does not exist")
        return
    
    # Find all markdown files in the dependencies directory
    markdown_files = list(dependencies_dir.glob("**/*.md"))
    
    # Filter out README.md and agent-prompts.md as requested
    markdown_files = [f for f in markdown_files if f.name not in ['README.md', 'agent-prompts.md']]
    
    print(f"Found {len(markdown_files)} markdown files to process")
    print()
    
    for file_path in markdown_files:
        process_markdown_file(file_path)
    
    print()
    print("✅ All files processed!")

if __name__ == "__main__":
    main()