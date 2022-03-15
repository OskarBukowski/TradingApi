import sqlalchemy
import sqlalchemy as db
from sqlalchemy.sql import select




class DatabaseExecutor:

    def __init__(self, query):
        self.query = query
        self.engine = engine = db.create_engine('postgresql://postgres:remiksow@192.168.0.52/postgres')
        self.connection = engine.connect()
        self.markets_dict = dict()

    def exchanges(self):
        output_proxy = self.connection.execute(self.query)
        output = output_proxy.fetchall()
        return [i[0] for i in output]

    def main(self):
        output_proxy = self.connection.execute(self.query)
        output = output_proxy.fetchall()
        return output

    def markets(self):
        output_proxy = self.connection.execute(self.query)
        output = output_proxy.fetchall()
        return [i[0].split("_")[0] for i in output]

    def markets_dict_creator(self):
        self.markets_dict = {}










query = 'SELECT * FROM bitkub.sushithb_ob LIMIT 5'

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
and NOT (table_name ~* '^pg' or table_name ~* '^sql')'''


d = DatabaseExecutor(query4)

print(d.main())
