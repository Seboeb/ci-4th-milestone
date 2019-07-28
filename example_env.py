import os
os.environ.setdefault('SECRET_KEY', '<RANDOM_SECRET_KEY>')
os.environ.setdefault('EMAIL_ADDRESS', '<YOUR_EMAIL_ADDRESS>')
os.environ.setdefault('EMAIL_PASSWORD', '<YOUR_EMAIL_PASSWORD>')
os.environ.setdefault('DATABASE_URL', '<YOUR_DATABASE_URL>')
os.environ.setdefault('DEVELOPMENT', '1')
os.environ.setdefault('STRIPE_PUBLISHABLE',
                      'pk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
os.environ.setdefault(
    'STRIPE_SECRET', 'sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# Link to a secret key generator for Django
# https://www.miniwebtool.com/django-secret-key-generator/
