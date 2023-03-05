import logging
from flask_limiter import Limiter
from datetime import datetime
from typing import Any, Optional
import connexion_experiment.global_app as global_app
import flask

from connexion_experiment.controllers.controller_utils import public_endpoint

LOGGER = logging.getLogger(__name__)

LIMITER = Limiter(
    lambda: "static-key",
    app=global_app.APP.app,
    # 1
    default_limits=[120, 60],
)

@LIMITER.limit("3/minute", override_defaults=True)
@public_endpoint
def environment() -> str:
    """
    Just environment
    """
    return settings.ENV

@LIMITER.limit("3/minute", override_defaults=True)
@public_endpoint
def version() -> str:
    """Just version number.

    Don't rate limit this, it gets used for health checks.
    """
    return __version__
