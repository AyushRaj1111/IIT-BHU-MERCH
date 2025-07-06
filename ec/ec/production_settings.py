"""
Production settings for PythonAnywhere deployment
"""
import os
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Update this with your PythonAnywhere username
ALLOWED_HOSTS = ['ayushraj1111.pythonanywhere.com', 'www.ayushraj1111.pythonanywhere.com']

# Database for production (PythonAnywhere uses MySQL)
# You can also stick with SQLite for simple projects
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files settings for production
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ayushraj1111/IIT-BHU-MERCHANDISE/ec/staticfiles'

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/ayushraj1111/IIT-BHU-MERCHANDISE/ec/media'

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Email settings for production (optional)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-app-password'

# Razorpay settings (keep these secure)
RAZOR_KEY_ID = os.environ.get('RAZOR_KEY_ID', 'rzp_test_LxRqAytA5m1RfA')
RAZOR_KEY_SECRET = os.environ.get('RAZOR_KEY_SECRET', '5IXsKXQ4NR89wHUZNs3GNVur')
