from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKey



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
db.init_app(app)

from Flask_Blog import routes