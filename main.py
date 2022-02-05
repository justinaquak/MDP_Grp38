from operator import truediv
from stm import *
#from android import *
#from pc import *
#from config import *
import threading
import os

import argparse
import cv2
import numpy as np
import sys
import time
import serial
from threading import Thread
import importlib.util
#from start_camtopc import *


class RaspberryPi(threading.Thread):
    def __init__(self):
        self.STMThread = STMRobot()
        self.pcThread = PCInterface()
        self.androidThread = AndroidApplication()

        #initalise connections
        self.STMThread.connectToSTM()
        self.androidThread.connectToAndroid()
        self.pcThread.connectToPC()

        time.sleep(2)

        print("Robot Startup")

    def multithread(self):
        #Android read and write thread
        #readAndroidThread = threading.Thread(target = self.readFromAndroid, args = (), name = "read_android_thread")
        #writeAndroidThread = threading.Thread(target = self.writeToAndroid, args = (), name = "write_android_thread")

        # STM read and write thread
        readSTMThread = threading.Thread(target = self.read_STM, args = (), name = "read_STM_thread")
        writeSTMThread = threading.Thread(target = self.write_STM, args = (), name = "write_STM_thread")

        # PC read and write thread
        #readPCthread = threading.Thread(target = self.readFromPC, args = (), name = "read_pc_thread")
        #writePCthread = threading.Thread(target = self.writeToPC, args = (), name = "write_pc_thread")

        # start running the thread for PC
        #readPCthread.start()

        # Start running thread for Android
        #readAndroidThread.start()

        # Start running thread for STM
        readSTMThread.start()

    def writeToAndroid(self, message):
        if(self.androidThread.isConnected):
            self.androidThread.writeToAndroid
            return True
        return False

    def readFromAndroid(self):
        if(self.androidThread.isConnected):
            while True:
                androidMessage = str(self.androidThread.readFromAndroid)
                print(androidMessage)
        
    def readFromPC(self):
        if(self.pcThread.isConnected):
            while True:
                self.pcThread.readFromPC
                print()
    def writeToPC(self, message):
        if(self.pcThread.isConnected):
            self.pcThread.writeToPC(message)

    def write_STM (self, message):
        if (self.STMThread.isConnected and message):
            self.STMThread.writeToSTM(message)
            return True
        return False
    def read_STM (self):
        try:
            while True:
                serialmsg = self.STMThread.readFromSTM()
                msg_remove = serialmsg.replace('@','')
                new_msg = msg_remove.split(",")

                serialmsgArray = new_msg[0].split(":")
                header = serialmsgArray[0]
        except:
            print("Error")

if __name__ == "__main__":
    print("Program Starting")
    main = RaspberryPi()

    try:
        main.multithread()

        
    except:
        print("Error")

