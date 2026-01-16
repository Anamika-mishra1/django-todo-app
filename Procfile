web: gunicorn todo_project.wsgi:application
release: python manage.py collectstatic --noinput && python manage.py migrate

