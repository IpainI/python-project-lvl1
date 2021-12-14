install:
	poetry install
brain-games:
	poetry add prompt
	poetry add --dev flake8
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip instal-user dist/*.whl
lint:
	poetry run flake8 brain-games
	