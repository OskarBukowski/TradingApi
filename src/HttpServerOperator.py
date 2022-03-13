from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# from src.OrderbookSchema import
# from src.TradesSchema import


app = Flask(__name__)






@app.route('/exchanges')