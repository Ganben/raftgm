#encoding=utf-8
# AaronCao
# node controller, receive msg and broadcast msg

from ..message.message import Messager, Message, Command

from ..blockdata.transaction import *
from ..blockdata.block import Block
from enum import Enum

class TkState(Enum):
    Tokenless = 1
    Candidate = 2
    Tokenwinner = 3


class Node:
    # node object, init method to setup enough 
    def __init__(self, addr):
        self.addr = addr # address for a node object
        self.state = TkState.Tokenless # initial state
        self.txpool = []
        self.no = 0
        self.currentblock = Block(self.no, self.txpool, self.addr)

    def sendcoin(self, receiver, amount, fee):
        # input in add
        t = Transaction(self.addr, receiver, amount, fee)

        m = Message(Command.TXSS, t.todict)
        return m

    def broadblock(self):
        # seal a block data then broad
        m = Message(Command.BROD, self.currentblock.tojson)
        return m

    