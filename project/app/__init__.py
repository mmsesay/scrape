# __init__.py
"""
Filename        :   __init__.py
Description     :   This file contains the whole logic for the application
Author          :   Muhammad Sesay
Email           :   contact@maej.dev
Started writing :   8/March/2023
Completed on    :   in progress
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app) # enable cors

# app secret key
app.config['SECRET_KEY'] = 'devkey'
app.config["JWT_SECRET_KEY"] = "testsecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://maej:maejor123@localhost:5432/flask_db' # sqlite:///' + os.path.join(app.root_path, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import routes

if __name__ == "__main__":
   app.run(debug=True)
