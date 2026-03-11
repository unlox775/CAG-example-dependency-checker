#!/usr/bin/env python3
"""
Check if we're blocked from making requests and create blocked file if needed.
"""

import requests
import time
from pathlib import Path

def check_blocked():
    """Check if we can make requests to external sites"""
    try:
        # Test with a simple request
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            print("✅ Not blocked - can make external requests")
            return False
        else:
            print(f"⚠️ Blocked - HTTP {response.status_code}")
            return True
    except Exception as e:
        print(f"❌ Blocked - {e}")
        return True

def create_blocked_file(reason):
    """Create blocked file with reason"""
    blocked_file = Path("/workspace/docs/dependencies/results/AA_I_AM_BLOCKED.txt")
    blocked_file.parent.mkdir(exist_ok=True)
    
    with open(blocked_file, 'w') as f:
        f.write(f"# Blocked from External Requests\n\n")
        f.write(f"**Reason:** {reason}\n")
        f.write(f"**Time:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("This means the link validator cannot check external URLs or perform Google searches.\n")
        f.write("Please check network connectivity and try again.\n")
    
    print(f"📄 Created blocked file: {blocked_file}")

if __name__ == "__main__":
    if check_blocked():
        create_blocked_file("Cannot make external requests")
    else:
        # Remove blocked file if it exists
        blocked_file = Path("/workspace/docs/dependencies/results/AA_I_AM_BLOCKED.txt")
        if blocked_file.exists():
            blocked_file.unlink()
            print("🗑️ Removed blocked file - requests working again")