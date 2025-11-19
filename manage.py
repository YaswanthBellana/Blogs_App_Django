#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Ensure logs directory exists so Django logging file handler can write logs
    logs_dir = os.path.join(os.path.dirname(__file__), 'logs')
    try:
        os.makedirs(logs_dir, exist_ok=True)
    except Exception:
        # If directory creation fails, continue; logging may still work to console
        pass
    logging.getLogger(__name__).info('Starting manage.py')
    main()
