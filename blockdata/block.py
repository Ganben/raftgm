#encoding=utf-8
# AaronCao
# Block object

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