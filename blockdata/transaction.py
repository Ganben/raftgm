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
        self.cat = 'tx'
    
    def todict(self):
        self.dict = {}
        self.dict['sender'] = self.sender
        self.dict['receiver'] = self.receiver
        self.dict['amount'] = self.amount
        self.dict['fee'] = self.fee
        self.dict['freez'] = self.freez
        self.dict['cat'] = self.cat
        return self.dict

    def tojson(self):
        # self.todict()
        return json.dumps(self.todict)

    def loadjson(self, j):
        d = json.loads(j)
        return Transaction(d['sender'], 
               d['receiver'], 
               d['amount'], d.get('fee'), d.get('freez'))

    def validate(self):
        # can be verified, not yet implt
        return True

class Bid:
    def __init__(self, sender, no=0, amount = 0):
        #amount = 100k + 0
        self.sender = sender
        self.amount = 10000 * 1000 + amount * 1000
        self.no = no
        self.cat = 'bi'
    
    def todict(self):
        # return a dict
        self.dict = {}
        self.dict['sender'] = self.sender
        self.dict['no'] = self.no
        self.dict['amount'] = self.amount
        self.dict['cat'] = self.cat
        return self.dict
    
    def tojson(self):
        # self.todict()
        return json.dumps(self.todict)

class Redeem:
    def __init__(self, receiver, no=0, tk=0, amount = 0):
        #
        self.receiver = receiver
        self.tk = tk
        self.no = no
        self.amount = 10000 * 1000 + amount * 1000
        self.cat = 'rd'
    
    def todict(self):
        #return a dict
        self.dict = {}
        self.dict['receiver'] = self.receiver
        self.dict['tk'] = self.tk
        self.dict['amount'] = self.amount
        self.dict['cat'] = 'rd'
        return self.dict

    def tojson(self):
        # self.todict()
        return json.dumps(self.todict)

class Reward:
    def __init__(self, amount, receiver, y=1, no=0, ratio = 0.5):
        self.amount = amount * 1000
        self.ratio = ratio
        self.no = no
        self.receiver = receiver
        self.y = y
        self.cat = 'rw'

    def todict(self):
        # return a dict
        self.dict = {}
        self.dict['no'] = self.no
        self.dict['ratio'] = self.ratio
        self.dict['receiver'] = self.receiver
        self.dict['y'] = self.y
        self.dict['amount'] = self.amount
        self.dict['cat'] = self.cat
        return self.dict
        
    def tojson(self):
        # self.todict()
        return json.dumps(self.todict)

def bulkloadjson(j):
    # load any txs and return a list of them
    d = json.loads(j)
    result = []
    for e in d:
        r = loadjson(e)
        result.append(r)
    return result


def loadjson(j):
    
    try:
        e = json.loads(j)
        tp = e.get('cat', 0)
        if tp == 'tx':
            # return a tx
            tx = Transaction(e.get('sender'), e.get('receiver'), 
            e.get('amount'), e.get('fee'), e.get('freez'))
            return tx

        elif tp == 'bi':
            # return a bid
            bi = Bid(
                e.get('sender'),
                e.get('no'),
                e.get('amount')
            )
            return bi
        
        elif tp == 'rd':
            # return a redeem
            rd = Redeem(
                e.get('receiver'),
                e.get('no'),
                e.get('tk'),
                e.get('amount')
            )
            return rd
        
        elif tp == 'rw':
            # return a reward
            rw = Reward(
                e.get('amount'),
                e.get('receiver'),
                e.get('y'),
                e.get('no'),
                e.get('ratio')
            )
            return rw
        else:
            raise ValueError('no cat')
    except:
        raise ValueError('json key')
    
    raise ValueError('json')