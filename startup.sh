# startup.sh is used by infra/resources.bicep to automate database migrations and isn't used by the sample application
python manage.py migrate
# gunicorn --workers 2 --threads 4 --timeout 60 --access-logfile \
#     '-' --error-logfile '-' --bind=0.0.0.0:8000 \
#      --chdir=/home/site/wwwroot aljarrash_backend.wsgi
uvicorn your_project_name.asgi:application --host 0.0.0.0 --port 8000 --workers 2