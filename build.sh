#!/usr/bin/env bash
# Exit on error
set -0 errexit

# Modify this line as neede for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Supply any outstanding database migrations
python manage.py migrate