from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__)#initialzie the app

from routes import *


app.config["SECRET_KEY"] ='sajdlksjc1'#ideal should come from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)#instance  of db

if __name__=='__main__':
  app.run(debug=True) 