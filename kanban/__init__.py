from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cs162isnice:cs162isnice@coffee-testing.cfk6e1o4l4d6.us-east-1.rds.amazonaws.com/cs162coffee'
db = SQLAlchemy(app)

from kanban import routes



