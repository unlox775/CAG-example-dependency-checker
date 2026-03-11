#!/usr/bin/env python3
"""
Explore the Blockly samples repository structure.
"""

import requests
import re
import time

def explore_blockly_repo():
    """Explore the Blockly samples repository to find the correct structure"""
    try:
        # Get the main repository page
        response = requests.get("https://github.com/google/blockly-samples", timeout=10)
        if response.status_code != 200:
            print(f"Failed to access main repo: {response.status_code}")
            return
        
        content = response.text
        
        # Look for directory links
        dir_pattern = r'<a[^>]*href="[^"]*tree/main/([^"]*)"[^>]*>([^<]*)</a>'
        matches = re.findall(dir_pattern, content)
        
        print("Found directories in blockly-samples:")
        print("=" * 50)
        
        directories = []
        for href, name in matches:
            if name and not name.startswith('.'):
                directories.append((href, name))
                print(f"  {name}: {href}")
        
        # Test some common patterns
        print("\nTesting common patterns:")
        print("=" * 50)
        
        test_patterns = [
            "https://github.com/google/blockly-samples/tree/main/plugins",
            "https://github.com/google/blockly-samples/tree/main/examples", 
            "https://github.com/google/blockly-samples/tree/main/packages",
            "https://github.com/google/blockly-samples/tree/main/src"
        ]
        
        for pattern in test_patterns:
            try:
                resp = requests.get(pattern, timeout=5)
                print(f"  {pattern}: {resp.status_code}")
                time.sleep(0.5)
            except Exception as e:
                print(f"  {pattern}: Error - {e}")
        
    except Exception as e:
        print(f"Error exploring repository: {e}")

if __name__ == "__main__":
    explore_blockly_repo()