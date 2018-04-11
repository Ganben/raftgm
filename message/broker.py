#encoding=utf-8
# AaronCao
# broker for snake mq #I give up, no, try another one

import snakemq.link
import snakemq.packeter
import snakemq.messaging
import snakemq.message

class Broker:
    # broker for mq server
    def __init__(self, port = 9000):
        self.link = snakemq.link.Link()
        self.packeter = snakemq.packeter.Packeter(self.link)
        self.link.add_listener(("", port)) # all interface/ip on port no
        self.clients = []

    def loop(self):
        # this is looping to driving all
        self.link.loop()
    
    def broadcast(self):
        # this is broadcasting method
        pass

    def onconn(self):
        # on connection put into list
        pass