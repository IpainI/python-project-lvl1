install:
	poetry install
brain-games:
	poetry add prompt
	poetry run brain-games
	
build:
	poetry build
publish:
	poetry publish 
package-install:
	python3 -m pip instal-user dist/*.whl
lint:
	poetry run flake8 brain-games
	