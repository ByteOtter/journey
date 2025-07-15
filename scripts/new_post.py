#!/usr/bin/env python3
import os
import sys
import argparse
from datetime import datetime
import re

POST_DIR = "content/posts"

def slugify(value):
    value = value.lower()
    value = re.sub(r'[^a-z0-9_]+', '-', value)
    return value.strip('-')

def exit_with_error(msg):
    print(f"Error: {msg}")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Create a new Hugo post.")
    parser.add_argument('--title', required=True, help="Post title (non-empty)")
    parser.add_argument('--filename', help="Post directory name (slug). If not provided, derived from title")
    parser.add_argument('--tags', help="Comma-separated tags")
    parser.add_argument('--categories', help="Comma-separated categories")

    args = parser.parse_args()

    # Strong validation for required args
    if not args.title.strip():
        exit_with_error("Missing or empty --title argument")
    if args.filename is not None and not args.filename.strip():
        exit_with_error("--filename provided but empty")

    title = args.title.strip()
    slug = args.filename.strip() if args.filename else slugify(title)
    post_dir = os.path.join(POST_DIR, slug)
    post_path = os.path.join(post_dir, "index.md")

    if os.path.exists(post_path):
        exit_with_error(f"Post already exists at {post_path}")

    os.makedirs(post_dir, exist_ok=True)
    with open(post_path, 'w') as f:
        f.write("---\n")
        f.write(f'title: "{title}"\n')
        f.write(f'date: {datetime.now().strftime("%Y-%m-%d")}\n')
        f.write("draft: true\n")
        if args.tags and args.tags.strip():
            tags = [tag.strip() for tag in args.tags.split(',')]
            f.write(f"tags: [{', '.join(tags)}]\n")
        if args.categories and args.categories.strip():
            cats = [cat.strip() for cat in args.categories.split(',')]
            f.write(f"categories: [{', '.join(cats)}]\n")
        f.write("---\n")

    print(f"Success: Created new post at {post_path}")

if __name__ == "__main__":
    main()
