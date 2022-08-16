#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.dev')
    
    with open('env', 'r') as file:
        env = [l.strip() for l in file.readlines()]

    env = [l.split('=', maxsplit=1) for l in env]
    
    for e in env:
        name, value = e
        os.environ[name] = value
        
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

