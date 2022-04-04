from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# from src.OrderbookSchema import
# from src.TradesSchema import
# from MainSchema import ExchangesSchema, Exchanges
from DatabaseConnection import DatabaseExecutor

app = Flask(__name__)


### ENV ACTIVATION ###
# source env/bin/activate


@app.route('/exchanges', methods=['GET'])
def get_exchanges():
    query = '''select schema_name from information_schema.schemata
    where not schema_name ~* '^pg'
    and not schema_name = 'information_schema';'''

    db = DatabaseExecutor(query)
    return jsonify(exchanges=db.exchanges())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, ssl_context='adhoc')
