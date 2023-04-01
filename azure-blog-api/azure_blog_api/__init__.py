from flask import Flask
from azure_blog_api.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from azure_blog_api import routes  # noqa: E402, F401
