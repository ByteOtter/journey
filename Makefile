HUGO=hugo
POST_DIR=content/posts
CACHE_DIR=$(shell $(HUGO) env | grep HugoCacheDir | cut -d '=' -f2 | tr -d '"')

help:
	@echo ""
	@echo "Available targets:"
	@echo ""
	@echo "Development:"
	@echo "============"
	@echo "    help                Show this help screen"
	@echo "    build               Build the site normally"
	@echo "    build-nocache       Build site while ignoring Hugo's cache"
	@echo "    serve               Start local server"
	@echo "    serve-dev           Start dev server with automatic rebuild on change"
	@echo "    serve-dev-nocache   Start dev server, but ignore any cache (Can help debug shortcodes)"
	@echo "    clear-cache         Clear Hugo cache and generated resources"
	@echo ""
	@echo "Themes/Dependencies:"
	@echo "===================="
	@echo "    submodules-init     Initialize and update git submodules"
	@echo "    submodules-update   Pull latest changes for submodules"
	@echo ""
	@echo "Content:"
	@echo "========"
	@echo "    new-post            Create a new draft blog post"
	@echo "    new-project         Create a new project section (simple or multi-page)"
	@echo ""
	@echo "Navigation/Config:"
	@echo "==========="
	@echo "    add-project-menu    Add a project entry to the 'Projects' menu"
	@echo ""
	@echo "Examples:"
	@echo "---------"
	@echo "  make new-post title='My New Post' filename='my_new_post' tags=post"
	@echo "  make new-project title='My Project' name='my_project' type=simple"
	@echo "  make new-project title='Complex Project' name='complex_project' type=multi summary='A project overview'"
	@echo "  make add-project-menu pre=python name='The Otter Den' pageRef=projects/otter_den weight=10"
	@echo ""


# Build normally
build:
	$(HUGO) build

build-nocache:
	$(HUGO) --ignoreCache

serve:
	$(HUGO) server

serve-dev:
	$(HUGO) server -D

serve-dev-nocache:
	$(HUGO) server --ignoreCache -D

submodules-init:
	git submodule init
	git submodule update

# Update submodules
submodules-update:
	$(shell ./update_blowfish.sh)

clear-cache:
	rm $(CACHE_DIR)/*

new-post:
	python3 scripts/new_post.py --title "$(title)" --filename "$(filename)" --tags "$(tags)" --categories "$(categories)"

new-project:
	python3 scripts/new_project.py --title "$(title)" --filename "$(filename)" --type "$(type)" --tags "$(tags)" --categories "$(categories)" --summary "$(summary)"

add-project-menu:
	python3 scripts/add_project_to_menu.py --pre "$(pre)" --name "$(name)" --pageRef "$(pageRef)" --weight "$(weight)"

.PHONY: help build serve build-nocache submodules-init submodules-update clear-cache new-post new-project add-project-menu
