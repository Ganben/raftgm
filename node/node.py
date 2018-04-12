#encoding=utf-8
# AaronCao
# node controller, receive msg and broadcast msg

from ..message.message import Messager, Message
from ..blockdata.transaction import *
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
    
    def sendtx(self, receiver, amount, fee):
        pass
