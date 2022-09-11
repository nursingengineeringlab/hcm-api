# how to setup backedn in a local enviroment

### Install venv (Ubuntu Linux)

```
python -m venv ./venv

source ./venv/bin/active
```

### Install dependencies

```
pip3 install -r ./requirements.txt
```

### Make sure the config files are correct

```
vim care_api/settings.py
```

The content is like this:

```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'po503mb0a39g1j&*(a#crfg$vnni#w+4v-re-43v7tw*siw19u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []

# SECURE_SSL_REDIRECT = True

# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'data_api',
    'rest_framework.authtoken',
    'djoser'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'care_api.urls'

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

WSGI_APPLICATION = 'care_api.wsgi.application'

ASGI_APPLICATION = 'care_api.asgi.application'

CHANNEL_LAYERS = {'default':{
    "BACKEND": "channels.layers.InMemoryChannelLayer"
}}


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'PAGE_SIZE': 10000,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


SQLLITE = 'django.db.backends.sqlite3'
POSTSQL = 'django.db.backends.postgresql'

DATABASES = {
    'default': {
        'ENGINE': POSTSQL,
        'NAME': 'SensorData',
        'USER': 'CHSUser1',
        'HOST': 'postgres-db-svc.postgresql.svc.cluster.local',
        'PASSWORD': 'A9EQFT6gS#LRHHwo75MRPZQl8mWaA02N&',
        'PORT': 5432,
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/backend/static/'

ALLOWED_HOSTS=['*']

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3001",
    "http://127.0.0.1:3001",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://nelab.ddns.umass.edu",
    "https://nelab.ddns.umass.edu",
    "http://nelab-ingress.eastus.cloudapp.azure.com",
    "https://nelab-ingress.eastus.cloudapp.azure.com",
]


ALLOWED_HOSTS = ['nelab-ingress.eastus.cloudapp.azure.com', 'nelab.ddns.umass.edu']

DJOSER = {
    "USER_ID_FIELD": "username"
}

```

### Run backend

```
./entrypoint.sh
```

or 

```
python3 manage.py makemigrations --noinput
python3 manage.py migrate
DJANGO_SUPERUSER_PASSWORD=test python3 manage.py createsuperuser --username test --email test@gamil.com --noinput
python3 manage.py runserver 0.0.0.0:8000
```


# how to deploy on kubernetes


### make sure you commit and push the code to codebase

```
git add -A
git commit -m "some changes"
git push origin/main
```

### Docker build local image

```
docker build . -t nelab/hcm-api:latest
```

### Docker push to dockerhub

```
docker push nelab/hcm-api:latest
```

### Login to kubernetes cluster

```
ssh nelab.ddns.umass.edu

```

### delete existing pod 

```
kubectl get namespace

NAME              STATUS   AGE
kube-system       Active   186d
kube-public       Active   186d
kube-node-lease   Active   186d
default           Active   186d
monitoring        Active   186d
redis             Active   170d
emqx              Active   169d
postgresql        Active   169d
ingress           Active   166d
traefik-v2        Active   163d
ingress-nginx     Active   163d
app               Active   162d

kubectl ns app  (make sure you install kubectx and kubens plugin)

Context "microk8s" modified.
Active namespace is "app".

kubectl get pods

NAME                           READY   STATUS    RESTARTS       AGE
datafetcher-8568568764-58vcb   1/1     Running   10 (16d ago)   149d
api-64475d566b-bpd7t           1/1     Running   0              8d
frontend-7bf4878444-h8hlv      1/1     Running   0              8d


kubectl delete pod api-64475d566b-bpd7t 

```

### wait for pod recreate and then it will pull the latest image from docker hub

