from azure_blog_api import app


@app.route("/")
def hello_world():
    return "Hello world"
