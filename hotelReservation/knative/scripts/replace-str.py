#!/usr/bin/env python3
import os
import argparse

def replace_in_file(file_path, old, new):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace(old, new)
        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
    except UnicodeDecodeError:
        # Skip binary files
        pass

def main():
    parser = argparse.ArgumentParser(description="Recursively replace a string in files.")
    parser.add_argument("directory", help="Directory to scan")
    parser.add_argument("old_string", help="String to replace")
    parser.add_argument("new_string", help="Replacement string")
    args = parser.parse_args()

    for root, dirs, files in os.walk(args.directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            replace_in_file(file_path, args.old_string, args.new_string)

if __name__ == "__main__":
    main()
