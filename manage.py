#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line, call_command
from django.contrib.auth import get_user_model

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

    # Setup Django apps
    application = get_wsgi_application()

    # Run migrations first
    print("Running migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    execute_from_command_line(['manage.py', 'migrate', 'quiz'])

    # Create superuser automatically (after migrations)
    User = get_user_model()
    if not User.objects.filter(is_superuser=True).exists():
        print("Creating superuser...")
        User.objects.create_superuser(
            username="admin",  # Change as necessary
            email="admin@example.com",  # Change as necessary
            password="adminpassword"  # Change as necessary
        )
        print("Superuser created.")
        
    # Check for the PORT environment variable
    port = os.getenv("PORT", "8000")  # Default to port 8000 if PORT is not set
    if "runserver" in sys.argv:
        # Check if the port is already provided; if not, append it
        if len(sys.argv) == sys.argv.index("runserver") + 1:
            sys.argv.append(f"0.0.0.0:{port}")
        else:
            sys.argv[sys.argv.index("runserver") + 1] = f"0.0.0.0:{port}"

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
