


class PCInterface(object):

    def __init__(self):
        self.host = WIFI_IP
        self.port = WIFI_PORT
        self.isConnected = False
    
    def connectToPC(self):
        print("Connect to PC")

    def disconnectToPC(self):
        print("Disconnect to PC")

    def writeToPC(self):
        print("Write to PC")
    def readFromPC(self):
        print("Read from PC")

    