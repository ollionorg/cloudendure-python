# Define make entry and help functionality
.DEFAULT_GOAL := help

.PHONY: help

REPO_NAME := mbeacom/cloudendure-python
SHA1 := $$(git log -1 --pretty=%h)
CURRENT_BRANCH := $$(git symbolic-ref -q --short HEAD)
LATEST_TAG := ${REPO_NAME}:latest
GIT_TAG := ${REPO_NAME}:${SHA1}
VERSION := v0.3.5

info: ## Show information about the current git state.
	@echo "Github Project: https://github.com/${REPO_NAME}\nCurrent Branch: ${CURRENT_BRANCH}\nSHA1: ${SHA1}\n"

run-docker: ## Run the local development environment docker shell.
	@docker run -v $(pwd):/app --rm -it airproducts /bin/bash

build: ## Build the release docker image.
	@docker build \
		--stream \
		--pull \
		--build-arg BUILD_DATETIME=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
		--build-arg "SHA1=${SHA1}" \
		--build-arg "VERSION=${VERSION}" \
		-t "${GIT_TAG}" .
	@docker tag "${GIT_TAG}" "${LATEST_TAG}"
	@docker tag "${GIT_TAG}" "${VERSION}"

build_py38: ## Build the Python 3.8 docker image.
	@docker build \
		--stream \
		--pull \
		--build-arg BUILD_DATETIME=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
		--build-arg "SHA1=${SHA1}" \
		--build-arg "VERSION=${VERSION}" \
		-t "${GIT_TAG}-py38" --file Dockerfile-py38 .
	@docker tag "${GIT_TAG}-py38" "${LATEST_TAG}-py38"
	@docker tag "${GIT_TAG}-py38" "${VERSION}-py38"

gh_push: ## Push the release Docker image to Github.
	@docker tag ${GIT_TAG} docker.pkg.github.com/mbeacom/cloudendure-python/cloudendure:${VERSION}
	@docker push docker.pkg.github.com/mbeacom/cloudendure-python/cloudendure:${VERSION}

gh_push_py38: ## Push the Python 3.8  Docker image to Github.
	@docker tag ${GIT_TAG}-py38 docker.pkg.github.com/mbeacom/cloudendure-python/cloudendure:${VERSION}-py38
	@docker push docker.pkg.github.com/mbeacom/cloudendure-python/cloudendure:${VERSION}-py38

login: ## Login to Docker Hub.
	@docker login -u "${DOCKER_USER}" -p "${DOCKER_PASS}"

gh_login: ## Login to Docker Hub.
	@docker login docker.pkg.github.com -u "${DOCKER_GH_USER}" -p "${DOCKER_GH_TOKEN}"

push: ## Push the Docker image to the Docker Hub repository.
	@docker push "${REPO_NAME}"

docker: build build_py38 ## Build and publish Docker images.

lint: isort ## Lint the CloudEndure project with Black.
	@poetry run black .

update_prereqs: ## Update the local development pre-requisite packages.
	@pip install --upgrade wheel setuptools pip

install-py-deps: update_prereqs ## Install the Python dependencies specified in the Pipfile.lock.
	@echo "Installing Python project dependencies..."
	@poetry install
	@echo "Python dependencies installed!"

init: ## Initialize the project.
	@pip install --upgrade wheel setuptools pip
	@curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
	@source $HOME/.poetry/env
	@poetry install

ci: ## Run the CI specific tests.
	@poetry run py.test -n 8 --boxed --junitxml=report.xml

flake8: ## Run Flake8 against the project.
	@poetry run flake8 --ignore=E501,F401,E128,E402,E731,F821 cloudendure

yapf: ## Run YAPF against the project.
	@poetry run yapf cloudendure

isort: ## Run isort against the project.
	@poetry run isort -sp=setup.cfg -rc .

coverage: ## Generate a test coverage report.
	poetry run py.test --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=cloudendure tests

publish: ## Publish the package to PyPi.
	poetry build
	poetry publish

docs: ## Build the documentation.
	poetry run pydocmd build

update_fork: ## Update the current fork master branch with upstream master.
	@echo "Updating the current fork with the upstream master branch..."
	@git checkout master
	@git fetch upstream
	@git merge upstream/master
	@git push origin master
	@echo "Updated!"

gen_client: ## Generate the swagger client from the API config.
	@swagger-codegen generate -i https://console.cloudendure.com/api_doc/apis.json -l python --model-name-prefix CloudEndure --git-user-id mbeacom --git-repo-id cloudendure-python -c reference/swagger_config.json -o gen/

update_deps: update_prereqs ## Update the package dependencies via poetry.
	@poetry update

install: isort build_py ## Install the local development version of the module.
	@poetry install .

build_py: update_deps ## Build and package the project for PyPi source and wheel distribution.
	@poetry build

help: ## Show this help information.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-25s\033[0m %s\n", $$1, $$2}'
