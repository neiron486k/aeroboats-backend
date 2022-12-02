import environ

env = environ.Env(
    DJANGO_CONFIG_MODE=(str, 'base'),
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    EMAIL_HOST=(str, 'localhost'),
    EMAIL_PORT=(str, '2525'),
    DEFAULT_FROM_EMAIL=(str, 'no-replay@aeroglissers.ru'),
    EMAIL_HOST_USER=(str, 'user'),
    EMAIL_HOST_PASSWORD=(str, 'pass'),
    EMAIL_USE_TLS=(bool, False),
    EMAIL_USE_SSL=(bool, False),
)
