#encoding=utf-8
# AaronCao
# Block object

class Block:

    def __init__(self, no):
        self.no = no
        self.txs = []
        self.rdtx = []
        # self.tokenpool =Tkpool()
    def addtx(self, tx):
        self.txs.append(tx)
    
    def addrdtx(self, rdtx):
        self.rdtx.append(rdtx)

    def updatetkpool(self, tkpool):
        self.tkpool = tkpool
    
    # funcs for fake tkpool and rdtx for malicious miner