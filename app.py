from flask import Flask;
from routes.index import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix="/api")


@app.route("/")
def home():
    return "<h1>Hello World from flask</h1>"

if __name__ == "__main__":
    app.run(debug=True)