#!/usr/bin/env python3
import os
import json
import re
import sys

def detect_version(directory):
    # 1. Check package.json
    pkg_path = os.path.join(directory, 'package.json')
    if os.path.exists(pkg_path):
        try:
            with open(pkg_path, 'r') as f:
                data = json.load(f)
                deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                svelte_version = deps.get('svelte', '')
                if svelte_version:
                    # Clean version string (e.g. ^5.0.0 -> 5.0.0, ^4.2.0 -> 4.2.0)
                    version_match = re.search(r'(\d+)\.\d+\.\d+', svelte_version)
                    if version_match:
                        major = int(version_match.group(1))
                        if major >= 5:
                            return 5
                        else:
                            return 4
        except Exception:
            pass

    # 2. Check files in directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.svelte'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        
                        # Explicit overrides first
                        if '<!-- svelte-version: 4 -->' in content:
                            return 4
                        if '<!-- svelte-version: 5 -->' in content:
                            return 5
                            
                        # Runes detection
                        if any(rune in content for rune in ['$state(', '$derived(', '$effect(', '$props(']):
                            return 5
                        # Legacy detection
                        if '$:' in content or 'on:' in content or 'createEventDispatcher' in content:
                            return 4
                except Exception:
                    pass

    # Default
    return 5

def main():
    test_cases = {
        'tests/svelte4': 4,
        'tests/svelte5': 5,
        'tests/fallback-svelte4': 4,
        'tests/fallback-svelte5': 5
    }

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    success = True

    for rel_path, expected in test_cases.items():
        dir_path = os.path.join(base_dir, rel_path)
        detected = detect_version(dir_path)
        if detected == expected:
            print(f"✅ {rel_path}: Detected Svelte {detected} (Expected: {expected})")
        else:
            print(f"❌ {rel_path}: Detected Svelte {detected} (Expected: {expected})")
            success = False

    if not success:
        sys.exit(1)
    print("All detection tests passed successfully!")

if __name__ == '__main__':
    main()
