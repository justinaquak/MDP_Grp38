import os, sys
import serial
import time
from setting import *


class STMRobot:
    def __init__(self):
        self.port = "/dev/ttyUSB1"
        self.baudRate = STM_BAUDRATE
        self.ser = 0
        self.isConnected = False

    def connectToSTM(self):
        counter = 0
        print("Connecting to STM")
        try:
            while self.isConnected != True or counter < 10 :
                counter+=1
                self.ser = serial.Serial(SERIAL_PORT0, self.baudRate, timeout=3)
                time.sleep(1)
                if(self.ser != 0):
                    print ("Serial Port 0 Connected to STM")
                    self.isConnected = True
                    break
                self.ser = serial.Serial(SERIAL_PORT1, self.baudRate, timeout=3)
                time.sleep(1)
                if(self.ser != 0):
                    print("Serial Port 1 Connected to STM")
                    self.isConnected = True
                    break
        except Exception as e:
            print("No Connection is found... %s" %str(e))
            #traceback.print_exc(limit=10, file=sys.stdout)

    def disconnectFromSTM (self):
        self.ser.close()
        self.isConnected = False
        print("Disconnected from STM.")

    def writeToSTM (self, msg):
        try:
            self.ser.write(str.encode(msg))
            print ("Sent to STM: %s" % msg)
        
        except Exception as e:
            print ("Failed to send message to STM. Exception Error : %s" %str(e))
            self.connectToSTM()

    def readFromSTM (self):
        try:
            msg = self.ser.readline()
            receivedMsg = msg.decode('utf-8')
            receivedMsg = str(receivedMsg)
            print ("Received from STM: %s" % receivedMsg)
            return receivedMsg

        except Exception as e:
            print ("Failed to receive message from STM")
            self.connectToSTM()
