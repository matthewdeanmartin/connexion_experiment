import decimal
import logging
import os
import sys
import traceback
from typing import Any, Optional

import connexion
from connexion.lifecycle import ConnexionResponse

import connexion_experiment.global_app as global_app
from connexion_experiment.global_app import APP

LOGGER = logging.getLogger(__name__)

# broken too....
# def any_error_as_problem(exception: Exception) -> ConnexionResponse:
#     """Customize exceptions"""
#     LOGGER.warning(exception)
#     traceback.print_exc()
#
#     error_document = {"code": 1, "message": str(exception)}
#
#     log = logging.getLogger(__name__)
#     log.error(error_document["message"])
#     log.exception("HTTP Error")  # exception() includes exec_info automatically
#
#     if os.environ.get("ENV", "") in ["WORKSTATION", "DEV", "TEST"]:
#         problem = connexion.problem(500, type(exception).__name__, str(exception))
#     else:
#         problem = connexion.problem(500, type(exception).__name__, "An error occurred")
#     return connexion.FlaskApi.get_response(problem)


YAML = "openapi.yaml"


print("got env workstation")
global_app.APP.add_api(
    YAML,
    strict_validation=True,
    validate_responses=True,
    # connexion tries to json encode all mimetypes
    # validator_map={"response": CustomResponseValidator},
)

# You need the FLASK_APP attribute to launch/debug as a flask app.
FLASK_APP = global_app.APP.app
# broken too
# global_app.APP.add_error_handler(Exception, any_error_as_problem)

