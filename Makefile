install:
	poetry install

i18n_make:
	poetry run django-admin makemessages -l ru
	poetry run django-admin makemessages -l en

i18n_compile:
	poetry run django-admin.py compilemessages -l ru
	poetry run django-admin.py compilemessages -l en

lint:
	poetry run flake8 task_manager --exclude=migrations,task_manager/settings.py

start_server:
	poetry run python manage.py runserver 127.0.0.1:8000

test:
	poetry run python manage.py test
	
test_coverage:
	poetry run coverage run --source='task_manager' manage.py test
	poetry run coverage xml
	poetry run coverage report

.PHONY: test