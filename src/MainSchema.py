from marshmallow import fields, Schema

class ObResponse:
    def __init__(self):
        pass


class TradesResponse:
    pass


# class Exchanges:
#     def __init__(self, names: list):
#         self.names = names
#
#     def __repr__(self):
#         return '<Exchanges(names={self.names!r})>'.format(self=self)
#
#
# class ExchangesSchema(Schema):
#     names = fields.List(fields.String(), required=True)