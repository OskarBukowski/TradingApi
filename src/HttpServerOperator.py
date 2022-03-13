from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# from src.OrderbookSchema import
# from src.TradesSchema import


app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:remiksow@192.168.0.52/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init database
db = SQLAlchemy(app)
