#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Check for the PORT environment variable
    port = os.getenv("PORT")
    if port and "runserver" in sys.argv:
        sys.argv[sys.argv.index("runserver") + 1] = f"0.0.0.0:{port}"

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
