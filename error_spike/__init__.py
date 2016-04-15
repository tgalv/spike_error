import os
import pkg_resources
from flask import Flask
from flask import render_template

from flask.ext.api.exceptions import APIException, ParseError, NotFound


app = Flask(__name__)
app.debug  = True

from .helloworld import views


app.config.from_object(os.environ.get('SETTINGS'))
app.register_blueprint(views.helloworld, url_prefix='/helloworld')

@app.route("/")
def index():
    return "error_spike"


@app.route("/div_zero")
def div_zero():
    1/0


@app.errorhandler(APIException)
def handle_api_exception(error):
    from pdb import set_trace; set_trace()
    return 'foo'


@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e,), exc_info=True)
    return render_template('503.html'), 500
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
