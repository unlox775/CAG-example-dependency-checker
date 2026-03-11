#!/usr/bin/env python3
"""
Test Blockly URLs to find the correct ones.
"""

import requests
import time

def test_url(url):
    """Test a single URL"""
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        return response.status_code, response.url
    except Exception as e:
        return None, str(e)

def test_blockly_urls():
    """Test various Blockly URL patterns"""
    base_urls = [
        "https://github.com/google/blockly-samples/tree/main/plugins/",
        "https://github.com/google/blockly-samples/tree/main/examples/",
        "https://github.com/google/blockly-samples/tree/main/",
    ]
    
    plugin_names = [
        "block-shareable-procedures",
        "procedures",
        "field-bitmap", 
        "field-colour",
        "field-grid-dropdown",
        "keyboard-navigation",
        "cross-tab-copy-paste",
        "scroll-options",
        "theme-dark",
        "theme-highcontrast"
    ]
    
    print("Testing Blockly URLs...")
    print("=" * 50)
    
    working_urls = {}
    
    for base_url in base_urls:
        print(f"\nTesting base: {base_url}")
        for plugin in plugin_names:
            url_to_test = base_url + plugin
            status, final_url = test_url(url_to_test)
            
            if status == 200:
                print(f"  ✅ {plugin}: {url_to_test}")
                working_urls[plugin] = url_to_test
            else:
                print(f"  ❌ {plugin}: {status} - {url_to_test}")
            
            time.sleep(0.5)  # Rate limiting
    
    print("\n" + "=" * 50)
    print("WORKING URLS:")
    for plugin, url in working_urls.items():
        print(f"{plugin}: {url}")
    
    return working_urls

if __name__ == "__main__":
    test_blockly_urls()