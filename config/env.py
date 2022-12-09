import environ

env = environ.Env(
    DJANGO_CONFIG_MODE=(str, "base"),
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    EMAIL_HOST=(str, "localhost"),
    EMAIL_PORT=(str, "2525"),
    DEFAULT_FROM_EMAIL=(str, "no-replay@aeroglissers.ru"),
    DEFAULT_TO_EMAIL=(str, "boss.kletsin1@mail.ru"),
    EMAIL_HOST_USER=(str, "user"),
    EMAIL_HOST_PASSWORD=(str, "pass"),
    EMAIL_USE_TLS=(bool, False),
    EMAIL_USE_SSL=(bool, False),
    DRF_RECAPTCHA_SECRET_KEY=(str, "private_key"),
    DRF_RECAPTCHA_TESTING=(bool, False),
)
