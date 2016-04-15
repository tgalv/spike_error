
import os
import pkg_resources


from flask import Flask, request, jsonify
from flask import render_template


app = Flask(__name__)
app.debug  = True

from .helloworld import views


app.config.from_object(os.environ.get('SETTINGS'))
app.register_blueprint(views.helloworld, url_prefix='/helloworld')


#################
# API
#################

@app.route("/")
def index():
    return "error_spike"


@app.route("/div_zero")
def div_zero():
    1/0


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
    if request_wants_json() or request_accepts_all_mime():
        print(request.data)
        return jsonify({'hello' : 'world'})
    else:
        return 'Not Supported', 406


##################
# HANDLERS
##################


@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e,), exc_info=True)
    return render_template('503.html'), 500
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
