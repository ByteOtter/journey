#!/usr/bin/env python3

import os
import sys
import argparse
from datetime import datetime
import re

PROJECT_DIR = "content/projects"

def slugify(value):
    value = value.lower()
    value = re.sub(r'[â-z0-9_]+', '-', value)
    return value.strip('-')


def exit_with_error(msg):
    print(f"Error: {msg}")
    sys.exit(1)


def write_front_matter(path, title, date, tags=None, categories=None, summary=None):
    with open(path, 'w') as f:
        f.write("---\n")
        f.write(f'title: "{title}"\n')
        f.write(f'date: {date}\n')
        f.write("draft: true\n")
        if summary:
            f.write(f'summary: "{summary}"\n')
        if tags:
            f.write(f"tags: [{', '.join(tags)}]\n")
        if categories:
            f.write(f"categories: [{', '.join(categories)}]\n")
        f.write("---\n")


def main():
    parser = argparse.ArgumentParser(description="Create a new Hugo project.")
    parser.add_argument('--title', required=True, help="Project title")
    parser.add_argument('--filename', required=True, help="Project folder name (slug)")
    parser.add_argument('--type', choices=['simple', 'multi'], default='simple', help="Project type: simple or multi")
    parser.add_argument('--tags', help="Comma-separated tags")
    parser.add_argument('--categories', help="Comma-separated categories")
    parser.add_argument('--summary', help="Project summary (used only for multi-type)")

    args = parser.parse_args()

    if not args.title.strip():
        exit_with_error("Missing or empty --title")
    if not args.filename.strip():
        exit_with_error("Missing or empty --filename")

    title = args.title.strip()
    slug = args.filename.strip()
    proj_type = args.type
    summary = args.summary.strip() if args.summary else None
    tags = [t.strip() for t in args.tags.split(',')] if args.tags else None
    categories = [c.strip() for c in args.categories.split(',')] if args.categories else None

    date = datetime.now().strftime("%Y-%m-%d")
    project_path = os.path.join(PROJECT_DIR, slug)

    if os.path.exists(project_path):
        exit_with_error(f"Project already exists at {project_path}")

    os.makedirs(project_path)

    if proj_type == 'simple':
        md_path = os.path.join(project_path, "index.md")
        write_front_matter(md_path, title, date, tags, categories)
        print(f"✅ Created simple project at {md_path}")
    else:
        md_path = os.path.join(project_path, "_index.md")
        write_front_matter(md_path, title, date, tags, categories, summary)
        print(f"✅ Created multi-project at {md_path}")
        print("ℹ️  You can now add sub-posts under this directory.")

if __name__ == "__main__":
    main()