#encoding=utf-8
# AaronCao
# token pool

import json
from enum import Enum

class Tokenstate(Enum):
    FREE = 1
    SOLD = 2

class Token:
    def __init__(self, id, age, st = Tokenstate.FREE, owner = 0):
        self.id = id
        self.age = 0 #
        self.st = st
        self.owner = owner
    
    def release(self):
        if not self.st == Tokenstate.SOLD:
            return False
        self.age = 0
        self.st = Tokenstate.FREE
        self.owner = 0
        return True
    
    def deliver(self, owner):
        if not self.st == Tokenstate.FREE:
            return False
        self.age = 0
        self.st = Tokenstate.SOLD
        self.owner = owner
        return True
    
    def todict(self):
        self.dict = {
            'id': self.id,
            'age': self.age,
            'st': self.st,
            'owner': self.owner
        }
        return self.dict

class Tokenpool:
    tpsize = 101
    def __init__(self):
        self.tokens = []
        for i in range(0, self.tpsize):
            e = Token(i, 0)
            self.tokens.append(e)
            self.tokens[0].deliver(0)

    def redeemtoken(self, id):
        return self.tokens[id].release

    def selltoken(self, id, buyer):
        return self.tokens[id].deliver(buyer)

    def getstate(self):
        self.dicts = []
        for i in range(0, self.tpsize):
            e = self.tokens[i].todict
            self.dicts.append(e)
        return self.dicts

    def loadstate(self, j):
        self.tokens = []

        ds = json.loads(j)
        for d in ds:
            t = Token(
                d.get('id'),
                d.get('age'),
                d.get('st'),
                d.get('owner')
            )
            self.tokens.append(t)
        return True