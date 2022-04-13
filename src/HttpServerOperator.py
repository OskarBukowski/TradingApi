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

@app.route('/markets', methods=['GET'])
def get_markets():
    query = '''SELECT table_name, table_schema 
    FROM   information_schema.tables
    where not table_schema = 'information_schema'
    and NOT (table_name ~* '^pg' or table_name ~* '^sql')
    and table_name like '%%_ob'; '''

    db = DatabaseExecutor(query)
    return jsonify(markets=db.markets())

@app.route('/trades&ex=<string:exchange>&market=<string:market>&limit=<int:limit>', methods=['GET'])
def get_trades(exchange, market, limit):
    query = '''SELECT * FROM {}.{}_trades
    ORDER BY timestamp DESC
    LIMIT {}'''.format(exchange, market, limit)

    db = DatabaseExecutor(query)
    return jsonify(db.trades())


@app.route('/orderbook&ex=<string:exchange>&market=<string:market>&limit=<int:limit>', methods=['GET'])
def get_orderbooks(exchange, market, limit):
    query = '''SELECT * FROM {}.{}_ob
    ORDER BY timestamp DESC
    LIMIT {}'''.format(exchange, market, limit)

    db = DatabaseExecutor(query)
    return jsonify(db.orderbook())

@app.route('/orderbook_range&ex=<string:exchange>&market=<string:market>&ts_range=<int:ts_from>,<int:ts_to>',
           methods=['GET'])
def get_orderbooks_range(exchange, market, ts_from, ts_to):
    query = '''select * from {}.{}_ob
    where "timestamp" between {} and {}'''.format(exchange, market, ts_from, ts_to)

    db = DatabaseExecutor(query)
    return jsonify(db.orderbook())




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, ssl_context='adhoc')
