from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
SECRET_KEY = 'django-insecure-3@u@_g9syo%ndiy!$5@rg135g)ckjk7h30jh0%zo1k*7kw2t-#'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1', 'localhost',  # Django server
    'chrome-extension://deookenapllfoafcpjgcaididbkadchl',  # Your extension
]

CORS_ALLOWED_ORIGINS = [
    "chrome-extension://deookenapllfoafcpjgcaididbkadchl",  # Your Chrome extension's origin
    "http://127.0.0.1:8000",  # Local Django server
    "https://your-django-backend.com",  # Your live backend, if applicable
]

CORS_ALLOW_METHODS = [
    'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS',  # Allow DELETE requests explicitly
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^chrome-extension://.*$",  # Allow any chrome-extension origin
]

CSRF_COOKIE_SAMESITE = 'None'  # Ensure CSRF cookie works across different origins
CSRF_COOKIE_SECURE = False  # Disable for development
CSRF_COOKIE_HTTPONLY = False  # Allow JavaScript to access CSRF token
CSRF_HEADER_NAME = "X-CSRFTOKEN"  # Ensure CSRF token is passed with the request

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
    'rest_framework',
    'corsheaders',  # Ensure this is listed here
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware should be first
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF middleware should be below CorsMiddleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'collaborative_todo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'collaborative_todo.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Ensure CSRF settings work with cross-origin requests
CSRF_COOKIE_HTTPONLY = False  # Allow JS to access CSRF cookie
CSRF_COOKIE_SECURE = False  # Disable for local development
