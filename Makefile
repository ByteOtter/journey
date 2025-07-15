HUGO=hugo
POST_DIR=content/posts
CACHE_DIR=$(shell $(HUGO) env | grep HugoCacheDir | cut -d '=' -f2 | tr -d '"')

help:
	@echo ""
	@echo "Available targets:"
	@echo "  help                This help screen"
	@echo "  build               Build the site normally"
	@echo "  serve               Start local dev server with drafts"
	@echo "  build-nocache       Build site while ignoring Hugo's cache"
	@echo "  submodules-init     Initialize and update git submodules"
	@echo "  submodules-update   Pull latest changes for submodules"
	@echo "  clear-cache         Clear Hugo cache and generated resources"
	@echo "  new-post            Create a new draft blog post"
	@echo ""
	@echo "Examples:"
	@echo "  make new-post title=my-awesome-post"
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
	@if [ -z "$(title)" ]; then \
		echo "Error: Please provide a title. Usage: make new-post title=your-title"; exit 1;\
	fi
	@date=$$(date +%Y-%m-%d); \
	filename="$(POST_DIR)/$$date-$(title).md"; \
	if [ -f "$$filename" ]; then \
		echo "Post already exists: $$filename"; exit 1; \
	fi; \
	echo "---" > $$filename; \
	echo "title: \"$(slug)\"" >> $$filename; \
	echo "date: $$date" >> $$filename; \
	echo "draft: true" >> $$filename; \
	echo "---" >> $$filename; \
	echo "Created new post at $$filename"

.PHONY: help build serve build-nocache submodules-init submodules-update clear-cache new-post
