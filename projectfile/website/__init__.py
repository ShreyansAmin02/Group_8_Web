from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
app = Flask(__name__)


def create_app():

    # we use this utility module to display forms quickly
    bootstrap = Bootstrap(app)

    # A secret key for the session object
    app.secret_key = 'somerandomvalue'

    # Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventDatabase.sqlite'
    db.init_app(app)
    from . import views, auth, events

    # Login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # add blue prints
    # app.register_blueprint(views.viewsbp)
    # app.register_blueprint(auth.authbp)
    app.register_blueprint(events.eventsbp)
    app.secret_key = 'IAB207'
    return app


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template("error.html")
