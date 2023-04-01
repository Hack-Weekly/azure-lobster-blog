import os

import pytest

from azure_blog_api import app as flask_app

basedir = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture()
def app():
    flask_app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here
    with flask_app.app_context():
        yield flask_app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


class TestApp:
    def setup_method(self):
        flask_app.config["TESTING"] = True
        self.app = flask_app.test_client()

    def test_hello_world(self, client):
        response = client.get("/")
        assert b"Hello world" in response.data
