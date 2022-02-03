from stm import *
from android import *
from pc import *
from config import *
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
from start_camtopc import *


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



if __name__ == "__main__":
    print("Program Starting")
    main = RaspberryPi()

    try:
        main.multithread()
    except:
        print("Error")

