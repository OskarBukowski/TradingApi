import sqlalchemy
import sqlalchemy as db
from sqlalchemy.sql import select


class DatabaseExecutor:

    def __init__(self, query):
        self.query = query
        self.engine = engine = db.create_engine('postgresql://postgres:****@****/postgres')
        self.connection = engine.connect()
        self.markets_dict = dict()

    def exchanges(self):
        output_proxy = self.connection.execute(self.query)
        output = output_proxy.fetchall()
        return [i[0] for i in output]

    def markets(self):
        output_proxy = self.connection.execute(self.query)
        output = output_proxy.fetchall()
        return [{i[1]: i[0].split("_")[0]} for i in output]

    def main(self):
        output_proxy = self.connection.execute(self.query)
        output = output_proxy.fetchall()
        return output

    def trades(self):
        output_proxy = self.connection.execute(self.query)
        output = output_proxy.fetchall()
        return {'status': 'ok',
                 'data': [{'id': r[0],
                           'price': r[1],
                           'amount': r[2],
                           'timestamp': r[3]} for r in output]}

    @staticmethod
    def ob_divider(data):
        return tuple(data[x:x + 2] for x in range(0, len(data), 2))

    def orderbook(self):
        output_proxy = self.connection.execute(self.query)
        output = [[r[x:x + 2] for x in range(0, len(r), 2)] for r in output_proxy.fetchall()]
        return {'status': 'ok',
                'data': [{'asks': r[0:10],
                          'bids': r[10:20],
                          'timestamp': r[20]} for r in output]}







query = '''SELECT * FROM bitkub.dogethb_ob
ORDER BY timestamp DESC
LIMIT 15'''

query2 = '''select schema_name from information_schema.schemata
where not schema_name ~* '^pg'
and not schema_name = 'information_schema';'''

query3 = '''SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE='BASE TABLE'
AND NOT (table_name ~* '^pg' or table_name ~* '^sql')'''

query4 = '''SELECT table_name, table_schema 
FROM   information_schema.tables
where not table_schema = 'information_schema'
and NOT (table_name ~* '^pg' or table_name ~* '^sql')
and table_name like '%%_ob'; '''


d = DatabaseExecutor(query)



res = d.main()

# print(res[0])


r = [res[0][x:x + 2]
      for x in range(0, len(res[0]), 2)]

# print(r)
#
# print([{'status': 'ok',
#         'data': [{'asks': r[0:10],
#                   'bids': r[20:20],
#                   'timestamp': r[20]} for r in res]}])


# output = [[r[x:x + 2] for x in range(0, len(r), 2)] for r in res]
#
# print(output)
#
# z = {'status': 'ok',
#          'data': [{'asks': r[0:10],
#                   'bids': r[10:20],
#                   'timestamp': r[20]} for r in output]}
#
# print(z)