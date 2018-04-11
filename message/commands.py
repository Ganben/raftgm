#encoding=utf-8
# AaronCao
# rpc protocols/mq topics

from enum import Enum

class Command(Enum):
    SYNC = 1  # confirmed old block sync
    TXSS = 2  # txs transmission
    BROD = 3  # mining/new block broadcasting


    