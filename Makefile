install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

setup: install build package-install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

lint: 
	poetry run flake8 page_loader

selfcheck:
	poetry check

check: selfcheck test lint

req:
	poetry export -f requirements.txt -o requirements.txt

run:
	poetry run python manage.py runserver

guni:
	poetry run gunicorn project.wsgi:application

get-trans:
	poetry run django-admin makemessages --ignore="static" --ignore=".env"  -l en

run-trans:
	poetry run django-admin compilemessages

shell:
	poetry run python manage.py shell_plus --print-sql