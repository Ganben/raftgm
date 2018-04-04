#encoding=utf-8
# AaronCao
# Address type

class Address:
    address = 0
    
    def __init__(self, i=0):
        self.address = i

    def setvalue(self, i):
        self.address = i
    
    def getvalue(self):
        return self.address
    