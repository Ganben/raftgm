#encoding=utf-8
# AaronCao
# general network message to RPC

class Message:
    # protocol for RPCs and abstract command
    def __init__(self, cmd, data):
        self.cmd = cmd
        self.data = data
    