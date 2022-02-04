import socket
import sys
import traceback
import errno
from setting import *


class PCInterface(object):

    def __init__(self):
        self.host = RPI_WIFI_IP
        self.port = WIFI_PORT
        self.isConnected = False


    def connectToPC (self):
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.connection.bind((self.host, self.port))
            print("Socket Bind")

            self.connection.listen(3)
            print ("Waiting for connection from PC........")

            self.clientSocket, self.address = self.connection.accept()
            print ("Connected to PC with the IP Address: ", self.address, ":)")
            self.isConnected = True

        except Exception as e:
            print ("Exception Error : %s" % str(e))
            print ("Please wait to try again")


    def disconnect(self):
        try:
            self.socket.close()
            self.connected = False
            self.threadListening = False
            print("Disconnected from PC successfully.")
        except Exception as e:
            print("Failed to disconnect from PC: %s" %str(e))

    def writeToPC(self, message):
        try:
            encoded_string = message.encode()
            byte_array = bytearray(encoded_string)
            self.client_socket.send(byte_array)
            print("Send to PC: " + message)
        except ConnectionResetError:
            print("Failed to send to PC: ConnectionResetError")
            self.disconnect()
        except socket.error:
            print("Failed to send to PC: socket.error")
            self.disconnect()

    def readFromPC (self):
        try:
            msg = self.clientSocket.recv(1024)
            msg = msg.decode('utf-8')
            print(len(msg))
            print ("Read from PC: %s" %(msg))

            if (not msg):
                self.disconnectFromPC()
                print('No message received, please wait to reconnect ')
                self.connectToPC()
                return msg

            return msg

        except Exception as e:
            print ('PC message reading failed. Exception Error : %s' % str(e))
            self.connectToPC()

    