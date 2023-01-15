install:
	poetry install

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test task_manager
	poetry run coverage xml
	poetry run coverage report

lint: 
	poetry run flake8 .

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
	poetry run django-admin makemessages -l ru

run-trans:
	poetry run django-admin compilemessages

shell:
	poetry run python manage.py shell_plus --print-sql