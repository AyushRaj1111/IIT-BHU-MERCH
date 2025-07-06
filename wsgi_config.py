# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It has been auto-generated and should require no changes.

import os
import sys

# Add your project directory to sys.path
path = '/home/JackedCoder/IIT-BHU-MERCHANDISE/ec'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'ec.production_settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
