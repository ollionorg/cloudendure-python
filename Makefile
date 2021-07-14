.PHONY: help
help: ## print out this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: generator-help
generator-help: ## openapi-generator help generate | less
	openapi-generator help generate | less

.PHONY: init
init:
	poetry init

.PHONY: install
install:
	poetry install

.PHONY: test
test: ## execute pytest in the poetry environment
	#poetry run pytest
	#poetry run python my-test.py


.PHONY: isort
isort: ## run isort (order import statements) on our py code
	poetry run isort -rc test/ cloudendure/

.PHONY: isort-test
isort-test: ## run isort to test import linting
	poetry run isort -rc --check-only --quiet test/ cloudendure/

.PHONY: black
black: ## run black (linter) agaist our python code
	poetry run black test/ cloudendure/

.PHONY: black-test
black-test: ## run black to test linting 
	poetry run black --check test/ cloudendure/

.PHONY: lint
lint: isort black ## run isort and black against our python code

.PHONY: rebuild-api
rebuild-api: pull-api fix-api-definition regenerate-api fix-generated-code lint ## regenerates the client code (deletes old code): pull fix-json delete gen fix-code and lint

.PHONY: build-api
build-api: pull-api fix-api-definition generate-api fix-generated-code lint ## does the whole shebang: pull fix-json gen fix-code and lint

.PHONY: generate-api
generate-api:  ## builds the cloudendure api code from the fixed openapi definition stored in ./build
	openapi-generator generate -i build/cloudendure-api-fixed.json -g python --package-name cloudendure --git-host 'github.com' --git-repo-id '2ndWatch/python-cloudendure' --git-user-id craigmonson -t openapi-generator/templates

.PHONY: regenerate-api
regenerate-api: generate-delete generate-api ## deletes generated code: README.md, cloudendure/, docs/, setup.py, test/, test-requirements.txt

.PHONY: pull-api
pull-api: ## pull and store the api json in the build dir
	curl https://console.cloudendure.com/api_doc/apis.json > build/cloudendure-api.json

.PHONY: fix-api-definition
fix-api-definition: ## fix any problematic api defs from the cloudendure def if possible.
	cd build && python fix-api.py

.PHONY: fix-generated-code
fix-generated-code: ## There are some cases where the api def is wrong, and can't be fixed in the swagger def, so we can fix it in the code.
	cd build && python fix-generated-code.py

.PHONY: generate-missing-docs
generate-missing-docs: ## there's some top level docs missing... this will generate them.
	poetry run pydoc

.PHONY: generate-delete
generate-delete: clean-api ## delete all the generated code
	rm -rf README.md cloudendure docs test

.PHONY: clean-api
clean-api: ## get rid of unnecessary files
	rm -f git_push.sh requirements.txt setup.cfg setup.py test-requirements.txt tox.ini

.PHONY: build
build: ## build the packages
	poetry build

.PHONY: tag
tag: ## tag this repo with $TAG (and mark the pyproject version as the same)
	poetry version $(TAG)
	git commit -am "Bumping version to $(TAG)"
	git push
	git tag -a $(TAG) -m "Rebuilding and Retagging to $(TAG)"
	git push --tags
