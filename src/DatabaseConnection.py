import sqlalchemy as db

engine = db.create_engine('postgresql://postgres:remiksow@192.168.0.52/postgres')
connection = engine.connect()
ResultProxy = connection.execute('SELECT * FROM bitkub.sushithb_trades LIMIT 5')
Result = ResultProxy.fetchall()
print(Result)