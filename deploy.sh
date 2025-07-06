#!/bin/bash
# PythonAnywhere Deployment Script
# Run this script in your PythonAnywhere Bash console

# Navigate to your home directory
cd ~

# Clone your repository
git clone https://github.com/AyushRaj1111/IIT-BHU-MERCHANDISE.git

# Navigate to the project directory
cd IIT-BHU-MERCHANDISE/ec

# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 iitbhu-merchandise

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser (you'll be prompted for details)
python manage.py createsuperuser

echo "Deployment completed! Don't forget to:"
echo "1. Update ALLOWED_HOSTS in production_settings.py with your PythonAnywhere domain"
echo "2. Configure the web app in PythonAnywhere dashboard"
echo "3. Set up static and media files mapping"
