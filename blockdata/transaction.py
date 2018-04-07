#encoding=utf-8
# AaronCao
# Transaction object, with a serializable dict(json)

import json


class Transaction:
    def __init__(self, sender, receiver, amount, fee = 0, freez = 0):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee
        self.freez = freez
    
    def todict(self):
        self.dict = {}
        self.dict['sender'] = self.sender
        self.dict['receiver'] = self.receiver
        self.dict['amount'] = self.amount
        self.dict['fee'] = self.fee
        self.dict['freez'] = self.freez
        return self.dict

    def tojson(self):
        # self.todict()
        return json.dumps(self.todict)

    def loadjson(self, j):
        d = json.loads(j)
        s = Transaction(d.get('sender'),
        d.get('receiver'),
        d.get('amount'),
        d.get('fee', 0),
        d.get('freez',0))
        # self.sender = d.get('sender')
        # self.receiver = d.get('receiver')
        # self.amount = d.get('amount')
        # self.fee = d.get('fee')
        # self.freez = d.get('freez')
        return s
        
