from stm import *
#from android import *
from pc import *
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
        self.pcThread = PCinterface()
        self.androidThread = AndroidApplication()

        #initalise connections
        self.STMThread.connectToSTM()
        self.androidThread.connectToTablet()
        self.pcThread.connectToPC()

        time.sleep(2)

        print("Robot Startup")

    def multithread(self):
        #Android read and write thread
        readAndroidThread = threading.Thread(target = self.read_Android, args = (), name = "read_android_thread")
        writeAndroidThread = threading.Thread(target = self.write_Android, args = (), name = "write_android_thread")

        # STM read and write thread
        readSTMThread = threading.Thread(target = self.read_STM, args = (), name = "read_STM_thread")
        writeSTMThread = threading.Thread(target = self.write_STM, args = (), name = "write_STM_thread")

        # PC read and write thread
        readPCthread = threading.Thread(target = self.read_PC, args = (), name = "read_pc_thread")
        writePCthread = threading.Thread(target = self.write_PC, args = (), name = "write_pc_thread")

        # start running the thread for PC
        readPCthread.start()

        # Start running thread for Android
        readAndroidThread.start()

        # Start running thread for STM
        readSTMThread.start()



if __name__ == "__main__":
    print("Program Starting")
    main = RaspberryPi()

    try:
        main.multithread()
    except:
        print("Error")

