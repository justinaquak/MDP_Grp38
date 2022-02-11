from bluetooth import *
from setting import *
import time

#BLUETOOTH_PORT = 0 #some number 

class AndroidApplication(object):

    def __init__(self):
        self.serverSocket = None
        self.sock = None
        self.connection = False

    def isConnected (self):
        return self.connection

    def connectToAndroid (self):
        try:
            uuid = "00001101-0000-1000-8000-00805F9B34FB"
            addr = "CC:46:4E:E1:D0:1D"
            service_matches = find_service( uuid = uuid, address = addr )
            
            print(service_matches)
            print(service_matches[0])
            first_match = service_matches[0]
            port = first_match["port"]
            host = first_match["host"]
            print("port: " + str(port) + "\nhost: " + str(host))
            #BLUETOOTH_PORT = bluetooth.PORT_ANY
            print("Bluetooth port number : ", port)
            self.sock = BluetoothSocket(RFCOMM)
            """self.serverSocket.bind(("",port))
            self.serverSocket.listen(1)
            self.port = port"""
            try:
                self.sock.connect((host, port))
                print ("Successfully Connected to Android :)")
            except Exception as e:
                print("Your android socket as failed: ", str(e))
            print ("Connection via Bluetooth RFCOMM channel %d" %port)
            # self.sock, clientInfo = self.serverSocket.accept()
            #print ("Rpi has accepted connection from ", clientInfo)  
            self.connection = True

        except Exception as e:
            print ("Bluetooth connection has failed, waiting to reconnect. ")
            # self.serverSocket.close()
            self.sock.close()
            print ("Closing bluetooth connection")
            # self.connection = False 

    def disconnectFromAndroid (self):
        self.sock.close()
        print ("Closing bluetooth (client)")
        # self.serverSocket.close()
        print ("Closing bluetooth (server)")
        self.connection = False 

    def writeToAndroid (self, msg):
        try:
            self.sock.send(msg)
            print ("Sent to Android : %s" %(msg))

        except Exception as e:
            print("Error with Bluetooth, waiting for rpi to reconnect")
            self.connectToAndroid()

    def readFromAndroid (self):
        try:
            #sleep(100)
            msg = self.sock.recv(1024)
            msg = msg.decode('utf-8')
            print("Received from Android: %s" % str(msg))
            return (msg)

        except Exception as e:
            print("Error with Bluetooth, waiting for rpi to reconnect")
            print(str(e))
            #self.connectToAndroid()
