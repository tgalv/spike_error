"""
The endpoint of the error_spike application.
"""

from flask import request, Blueprint, Response
from error_spike import app


helloworld = Blueprint('helloworld' , __name__)


@helloworld.route('/', methods=["GET"])
def index():
    """
    Say Hello.

    :return: The de-facto greeting.
    :rtype: str
    """
    app.logger.debug("Saying hello...")
    return 'Hello World!'
