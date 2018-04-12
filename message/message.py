#encoding=utf-8
# AaronCao
# general network message to RPC
# use mqtt client mq

import json
import paho.mqtt.client as mqtt # Client and transmission
from commands import Command


class Messager:
    # protocol for RPCs and abstract command
    def __init__(self, addr):
        # self.cmd = cmd
        # self.data = data
        self.addr = addr
        self.mqttclient =mqtt.Client
        self.mqttclient.on_connect = self.on_connect
        # self.mqttclient.on_message = self.on_message
        self.mqttclient.on_disconnect = self.on_disconnect

        # self.mqttclient.connect("localhost", 1883, 60) # call in main thread



    def on_connect(self, client, userdata, flags, rc):
        # on connect broad self id
        # pass
        p = str(self.addr)
        client.subscribe('SYNC')
        client.subscribe('BROD')
        client.subscribe('TXSS')
        client.publish('node', p)

    def on_message(self, client, userdata, msg):
        # handling incomming message
        pass

    def on_disconnect(self, client, userdata, rc):
        # reconnect 
        if rc != 0:
            print("disconnection, retry")
        client.reconnect()

    def sendmessage(self, msg):
        # send message using topic
        pass
    
class Message:
    # three type, constructor/parser
    def __init__(self, cmd = Command.SYNC, data = 0):
        self.cmd = cmd
        self.data = data   
    
    def loaddict(self, d):
        if d.get('cat', False):
            self.cmd = Command.TXSS
            self.data = json.dumps(d)
            # TODO: publish once single msg

        elif d.get('cmd') == Command.BROD:
            # other command
            self.cmd == Command.BROD
            self.data = d
            # broadcast for a new block

        else:
            # request sync data
            pass
    
    def send(self, client):
        # complet 
        if self.cmd == Command.BROD:
            return client.publish("BROD", self.data)
        elif self.cmd == Command.TXSS:
            return client.publish("TXSS", self.data)
        elif self.cmd == Command.SYNC:
            return client.publish("SYNC", self.data)
        else:
            return False
            