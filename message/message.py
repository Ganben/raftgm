#encoding=utf-8
# AaronCao
# general network message to RPC
# use sname mq

import json

class Message:
    # protocol for RPCs and abstract command
    def __init__(self, cmd = None, data = None):
        self.cmd = cmd
        self.data = data

    def tojson(self):
        # return a serialized json 
        r = {
            'cmd': self.cmd,
            'data': self.data
        }
        j = json.dumps(r)
        return j

