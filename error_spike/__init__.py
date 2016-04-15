import os
import pkg_resources
from flask import Flask


app = Flask(__name__)

from .helloworld import views

app.config.from_object(os.environ.get('SETTINGS'))
app.register_blueprint(views.helloworld, url_prefix='/helloworld')

@app.route("/")
def index():
    return "error_spike"
