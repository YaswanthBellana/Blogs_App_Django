#!/bin/bash
set -e

# Run database migrations
echo "Running migrations..."
echo "Ensuring logs directory exists..."
mkdir -p "./logs"
python manage.py migrate --noinput

# (Optional) collect static files
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# Execute the container's main process (CMD)
# exec "$@"
exec gunicorn blog.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 90
