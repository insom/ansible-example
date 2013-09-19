from flask import Flask
from webapp.models import db


def register_blueprints(app):
    from webapp.inventory import inventory
    app.register_blueprint(
        inventory,
        url_prefix='/inventory',
    )


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp/example.db'

    db.init_app(app)
    register_blueprints(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
