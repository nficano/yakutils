dev:
	pipenv install --dev

deploy-patch: requirements bumpversion-patch sdist bdist wheels upload clean

deploy-minor: requirements bumpversion-minor sdist bdist wheels upload clean

deploy-major: requirements bumpversion-major sdist bdist wheels upload clean

requirements:
	pipenv_to_requirements

sdist: requirements
	python setup.py sdist

bdist: requirements
	python setup.py bdist

wheels: requirements
	python setup.py bdist_wheel

clean: clean-build clean-pyc

VERSION_PATCH = $(bumpversion --dry-run --list patch | grep new_version | sed  s/'^.*='//)
VERSION_MINOR = $(bumpversion --dry-run --list minor | grep new_version | sed  s/'^.*='//)
VERSION_MAJOR = $(bumpversion --dry-run --list major | grep new_version | sed  s/'^.*='//)
VERSION_CURRENT = $(bumpversion --dry-run --list major | grep current_version | sed  s/'^.*='//)

bumpversion-patch:
	bumpversion patch
	pre-commit run --all-files || true
	git add .
	git commit -am "Bump version: ${VERSION_CURRENT} → ${VERSION_PATCH}"
	git push
	git push --tags

bumpversion-minor:
	bumpversion minor
	pre-commit run --all-files || true
	git add .
	git commit -am "Bump version: ${VERSION_CURRENT} → ${VERSION_MINOR}"
	git push
	git push --tags

bumpversion-major:
	bumpversion major
	pre-commit run --all-files || true
	git add .
	git commit -am "Bump version: ${VERSION_CURRENT} → ${VERSION_MAJOR}"
	git push
	git push --tags

upload:
	python setup.py sdist bdist bdist_wheel upload

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.DS_Store' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +
