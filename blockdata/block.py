#encoding=utf-8
# AaronCao
# Block object
import json

class Block:

    def __init__(self, no, tks, miner = 0):
        self.miner = miner
        self.no = no
        self.txs = []
        self.rds = []
        self.bis = []
        self.rws = []
        self.tks = tks
        # self.tokenpool =Tkpool()
    def addtx(self, tx):
        self.txs.append(tx)
    
    def addrd(self, rd):
        self.rds.append(rd)

    def addbi(self, bi):
        self.bis.append(bi)
        if len(self.rds) == len(self.bis):
            return False
        else:
            return 

    def updatetkpool(self, tkpool):
        self.tkpool = tkpool
    
    # funcs for fake tkpool and rdtx for malicious miner

    def todict(self):
        # serialization
        pass

    def tojson(self):
        # serilization
        d = {}
        d['head'] = {
            'no': self.no,
            'miner': self.miner
        }
        ltks = []
        for e in self.tks:
            ltks.append(e.todict)
        lbids = []
        for e in self.bis:
            lbids.append(e.todict)
        lrds = []
        for e in self.rds:
            lrds.append(e.todict)
        lrws = []
        for e in self.rws:
            lrws.append(e.todict)
        d['tks'] = ltks
        d['bis'] = lbids
        d['rds'] = lrds
        d['rws'] = lrws
        return json.dumps(d)
        