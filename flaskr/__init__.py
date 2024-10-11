from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = 'dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route("/hello")
    def hello():
        return 'Hello, world!'
    
    @app.route("/exercise")
    def exercise():
        with open("tests/exercise.txt", "r") as f:
            content = f.readlines()

        return render_template("index.html", content = content)
    
    return app