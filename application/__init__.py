#!/usr/bin/python3

#   __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from os import get env
import pymysql

app = Flask(__name__)

#pp.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://ash:root21@localhost/wardrobe_db"

db = SQLAlchemy(app)

from application import routes

