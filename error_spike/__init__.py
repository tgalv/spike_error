
import os
import pkg_resources


from jsonschema import validate, Draft4Validator
from jsonschema.exceptions import ValidationError
from flask import Flask, request, jsonify
from flask import render_template


app = Flask(__name__)
app.debug  = True

from .helloworld import views


app.config.from_object(os.environ.get('SETTINGS'))
app.register_blueprint(views.helloworld, url_prefix='/helloworld')


schema = {
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
    },
}



#################
# API
#################

@app.route("/")
def index():
    return "error_spike"


@app.route("/div_zero")
def div_zero():
    app.logger.debug("div_zero")
    1/0


#################
# SCHEMA
#################

class ValidateAllErrors(Exception):
    
    status_code = 400

    def __init__(self, message):
        self.message = message
    

def validate_report_all_errors(instance, schema):
    try:
        validate(instance, schema)
    except ValidationError:
        v = Draft4Validator(schema)
        msg = ','.join([err.message for err in v.iter_errors(instance)])
        raise ValidateAllErrors(msg)
        
###############
# CONTENT-NEG
###############

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']


def request_accepts_all_mime():
    return '*/*' in request.accept_mimetypes.values()


@app.route('/json_post', methods=["POST"])
def json_post():
    app.logger.debug("json_post: '%s'", request.data)
    if request_wants_json() or request_accepts_all_mime():
        print(request.mimetype)
        if request.mimetype != 'application/json' and request.mimetype != 'application/x-www-form-urlencoded':
            return 'Unsupported Media Type', 415
        #
        validate_report_all_errors(request.json, schema)
        #
        return jsonify({'hello':'world'})
    else:
        return 'Not Acceptable', 406


##################
# HANDLERS
##################

@app.errorhandler(ValidateAllErrors)
def handle_schema_validation(error):
    response = error.message
    return response, error.status_code


@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e,), exc_info=True)
    return render_template('503.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    app.logger.error('Page not found: %s', (e,), exc_info=True)
    return render_template('404.html'), 404
