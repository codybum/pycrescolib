from pycrescolib.admin import admin
from pycrescolib.agents import agents
from pycrescolib.dataplane import dataplane
from pycrescolib.globalcontroller import globalcontroller
from pycrescolib.logstreamer import logstreamer
from pycrescolib.messaging import messaging
from pycrescolib.wc_interface import ws_interface


class clientlib(object):

    def __init__(self,host, port, service_key):
        self.host = host
        self.port = port
        self.service_key = service_key
        self.ws_interface = ws_interface()
        self.messaging = messaging(self.ws_interface)
        self.agents = agents(self.messaging)
        self.admin = admin(self.messaging)
        self.globalcontroller = globalcontroller(self.messaging)

    def connect(self):
        try:
            ws_url = 'ws://' + self.host + ':' + str(self.port) +'/api/apisocket'
            isWSConnected = self.ws_interface.connect(ws_url)
            return isWSConnected
        except:
            return False

    def connected(self):
        try:
            return self.ws_interface.connected()
        except:
            return False

    def close(self):
        if self.ws_interface.connected():
            self.ws_interface.close()

    def get_dataplane(self, stream_name):
        return dataplane(self.host, self.port, stream_name)

    def get_logstreamer(self):
        return logstreamer(self.host, self.port)




