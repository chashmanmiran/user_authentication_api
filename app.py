from flask import Flask
from extensions import db
from flask_bcrypt import Bcrypt
from resources import blp
import os


app = Flask(__name__)

#SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#Secret-Key
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-replace-me")

#Password Hashing
bcrypt = Bcrypt(app)

#Resources
app.register_blueprint(blp)


with app.app_context():
    db.create_all()

#Debugger
if __name__ == "__main__":
    app.run(debug=True)


