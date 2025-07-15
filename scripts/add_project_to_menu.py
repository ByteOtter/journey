#!/usr/bin/env python3
import argparse
import os
import sys

MENU_PATH = "config/_default/menus.en.toml"

def exit_with_error(msg):
    print(f"Error: {msg}")
    sys.exit(1)

def append_menu_entry(pre, name, page_ref, weight):
    if not os.path.exists(MENU_PATH):
        exit_with_error(f"Menu file not found: {MENU_PATH}")

    entry = (
        "\n[[main]]\n"
        f'pre = "{pre}"\n'
        f'name = "{name}"\n'
        f'parent = "Projects"\n'
        f'pageRef = "{page_ref}"\n'
        f'weight = {weight}\n'
    )

    with open(MENU_PATH, "a") as f:
        f.write(entry)

    print(f"✅ Added menu entry for '{name}' to {MENU_PATH}")

def main():
    parser = argparse.ArgumentParser(description="Add a project to the Hugo menu.")
    parser.add_argument('--pre', required=True, help="Icon or prefix label")
    parser.add_argument('--name', required=True, help="Menu display name")
    parser.add_argument('--pageRef', required=True, help="Hugo page reference (e.g. projects/my_project)")
    parser.add_argument('--weight', type=int, default=10, help="Menu item weight (default: 10)")

    args = parser.parse_args()

    if not args.name.strip() or not args.pageRef.strip() or not args.pre.strip():
        exit_with_error("All of --pre, --name, and --pageRef must be non-empty")

    append_menu_entry(args.pre.strip(), args.name.strip(), args.pageRef.strip(), args.weight)

if __name__ == "__main__":
    main()
