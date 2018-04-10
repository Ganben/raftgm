#encoding=utf-8
# AaronCao
# rpc protocols

from enum import Enum

class Command(Enum):
    SYNC = 1
    TXSS = 2
    BROD = 3
    