#!/usr/bin/env python
# Utilidad de línea de comandos de Django (runserver, test, etc.)
import os
import sys


def main():
    # Le indica a Django qué archivo de configuración usar
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multiventas.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
