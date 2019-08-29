# Define make entry and help functionality
.DEFAULT_GOAL := help

.PHONY: help

REPO_NAME := mbeacom/cloudendure-python
SHA1 := $$(git log -1 --pretty=%h)
CURRENT_BRANCH := $$(git symbolic-ref -q --short HEAD)
LATEST_TAG := ${REPO_NAME}:latest
GIT_TAG := ${REPO_NAME}:${SHA1}
VERSION := v0.0.10

info: ## Show information about the current git state.
	@echo "Github Project: https://github.com/${REPO_NAME}\nCurrent Branch: ${CURRENT_BRANCH}\nSHA1: ${SHA1}\n"

build: ## Build the Gitcoin Web image.
	@docker build \
		--stream \
		--pull \
		--build-arg BUILD_DATETIME=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
		--build-arg "SHA1=${SHA1}" \
		--build-arg "VERSION=${VERSION}" \
		-t "${GIT_TAG}" .
	@docker tag "${GIT_TAG}" "${LATEST_TAG}"
	@docker tag "${GIT_TAG}" "${VERSION}"
	@docker build \
		--stream \
		--pull \
		--build-arg BUILD_DATETIME=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
		--build-arg "SHA1=${SHA1}" \
		--build-arg "VERSION=${VERSION}" \
		-t "${GIT_TAG}-py38" Dockerfile-py38
	@docker tag "${GIT_TAG}-py38" "${LATEST_TAG}-py38"
	@docker tag "${GIT_TAG}-py38" "${VERSION}-py38"

gh_push: ## Push the Github Docker image.
	@docker tag ${GIT_TAG} docker.pkg.github.com/mbeacom/cloudendure-python/cloudendure:${VERSION}
	@docker push docker.pkg.github.com/mbeacom/cloudendure-python/cloudendure:${VERSION}
	@docker tag ${GIT_TAG}-py38 docker.pkg.github.com/mbeacom/cloudendure-python/cloudendure:${VERSION}-py38
	@docker push docker.pkg.github.com/mbeacom/cloudendure-python/cloudendure:${VERSION}-py38

login: ## Login to Docker Hub.
	@docker login -u "${DOCKER_USER}" -p "${DOCKER_PASS}"

gh_login: ## Login to Docker Hub.
	@docker login docker.pkg.github.com -u "${DOCKER_GH_USER}" -p "${DOCKER_GH_TOKEN}"

push: ## Push the Docker image to the Docker Hub repository.
	@docker push "${REPO_NAME}"

docker: ## Build and publish Docker images.
	@docker build -t cloudendure .
	@docker tag cloudendure mbeacom/cloudendure-python
	@docker push

lint: isort ## Lint the CloudEndure project with Black.
	@pipenv run black --target-version py37 --exclude "/(\.eggs|\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|build|dist|tests|cloudendure_api)/" .

update_prereqs: ## Update the local development pre-requisite packages.
	@pip install --upgrade pipenv wheel setuptools pip

install-py-deps: update_prereqs ## Install the Python dependencies specified in the Pipfile.lock.
	@echo "Installing Python project dependencies..."
	@pipenv install --dev --pre
	@echo "Python dependencies installed!"

init: ## Initialize the project.
	@pip install --upgrade pipenv wheel setuptools pip
	@pipenv install --dev --pre

ci: ## Run the CI specific tests.
	@pipenv run py.test -n 8 --boxed --junitxml=report.xml

flake8: ## Run Flake8 against the project.
	@pipenv run flake8 --ignore=E501,F401,E128,E402,E731,F821 cloudendure

yapf: ## Run YAPF against the project.
	@pipenv run yapf cloudendure

isort: ## Run isort against the project.
	@pipenv run isort -sp=setup.cfg -rc .

coverage: ## Generate a test coverage report.
	pipenv run py.test --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=cloudendure tests

publish: ## Publish the package to PyPi.
	pipenv run python3 setup.py sdist bdist_wheel
	pipenv run twine upload dist/*
	rm -fr build dist .egg requests.egg-info

docs: ## Build the documentation.
	pipenv run pydocmd build

update_fork: ## Update the current fork master branch with upstream master.
	@echo "Updating the current fork with the upstream master branch..."
	@git checkout master
	@git fetch upstream
	@git merge upstream/master
	@git push origin master
	@echo "Updated!"

gen_client: ## Generate the swagger client from the API config.
	@swagger-codegen generate -i https://console.cloudendure.com/api_doc/apis.json -l python --model-name-prefix CloudEndure --git-user-id mbeacom --git-repo-id cloudendure-python -c reference/swagger_config.json -o gen/

update_deps: update_prereqs ## Update the package dependencies via pipenv.
	@pipenv update --pre --dev

install: isort build_py ## Install the local development version of the module.
	@pipenv install .

build_py: update_deps ## Build and package the project for PyPi source and wheel distribution.
	@pipenv run python3 setup.py sdist bdist_wheel

help: ## Show this help information.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-25s\033[0m %s\n", $$1, $$2}'
