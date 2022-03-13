import sqlalchemy
import sqlalchemy as db
from sqlalchemy.sql import select




class DatabaseExecutor:

    def __init__(self, query):
        self.query = query
        self.engine = engine = db.create_engine('postgresql://postgres:remiksow@192.168.0.52/postgres')
        self.connection = engine.connect()

    def exchanges(self):
        output_proxy = self.connection.execute(self.query)
        output = output_proxy.fetchall()
        return [i[0] for i in output]

    def main(self):
        output_proxy = self.connection.execute(self.query)
        output = output_proxy.fetchall()
        return output










query = 'SELECT * FROM bitkub.sushithb_ob LIMIT 5'

query2 = '''select schema_name from information_schema.schemata
where not schema_name ~* '^pg'
and not schema_name = 'information_schema';'''

d = DatabaseExecutor(query)

print(d.main())
