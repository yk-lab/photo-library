from logging import getLogger

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import ignore_logger
from .setting_utils import env_float

logger = getLogger(__name__)


def setup():
    from django.conf import settings

    ignore_logger("django.security.DisallowedHost")

    # traces_sample_rate
    traces_sample_rate = env_float("SENTRY_TRACES_SAMPLE_RATE", 0.0)

    # profiles_sample_rate
    profiles_sample_rate = env_float("SENTRY_PROFILES_SAMPLE_RATE", 0.0)

    logger.info(f"SENTRY_RATES: {traces_sample_rate=}, {profiles_sample_rate=}")

    if dsn := getattr(settings, "SENTRY_DSN"):
        sentry_sdk.init(
            dsn=dsn,
            environment=getattr(settings, "ENVIRONMENT"),
            integrations=[
                DjangoIntegration(),
            ],
            #
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=traces_sample_rate,
            #
            # Set profiles_sample_rate to 1.0 to profile 100%
            # of sampled transactions.
            # We recommend adjusting this value in production.
            profiles_sample_rate=profiles_sample_rate,
            #
            # If you wish to associate users to errors (assuming you are using
            # django.contrib.auth) you may enable sending PII data.
            send_default_pii=True,
        )
