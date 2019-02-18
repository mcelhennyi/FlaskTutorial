import os

from flask import Flask

from Database import db
from Site.public import mod as public_mod

app = Flask(__name__)

# Setup Blueprints
app.register_blueprint(public_mod)

# Configs
debug = True
app.config['SQLALCHEMY_ECHO'] = debug
db_path = 'sqlite:///' + os.path.join("Database", "tutorial.db")
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# Create db initialization
def init_db():
    db.init_app(app)
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    init_db()
    app.run(debug=debug)
