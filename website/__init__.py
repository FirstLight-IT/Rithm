from flask import Flask

def getApp():
    app = Flask(__name__, template_folder='templates')

    app.config['SECRET_KEY'] = 'OS101FINALPT'

    from .routes import bp
    app.register_blueprint(bp)

    return app
