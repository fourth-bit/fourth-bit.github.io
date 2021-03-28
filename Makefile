CSS_DIR = ./css
CHARITIES_DIR = ./charities
ITEMS_DIR = ./items

.PHONY: css html dependencies

all: css html

dependencies:
	@echo "Checking Dependencies"
	python python/check_dependencies.py

css: dependencies
	@echo "CSS generation"
	[ -d $(CSS_DIR) ] || (mkdir -p $(CSS_DIR); echo "Created css directory")
	sassc scss/custom.scss css/bootstrap.css

html: dependencies
	@echo "HTML generation with python"
	[ -d $(CHARITIES_DIR) ] || (mkdir -p $(CHARITIES_DIR); echo "Created charities directory")
	[ -d $(ITEMS_DIR) ] || (mkdir -p $(ITEMS_DIR); echo "Created items directory")
	python python/verify_json.py
	python python/list_view.py charities.html $(CHARITIES_DIR)/index.html
	python python/detail_view.py $(CHARITIES_DIR)
	python python/items.py items.html $(ITEMS_DIR)