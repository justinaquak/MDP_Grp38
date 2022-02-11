#from operator import truediv
#from tkinter import E
from stm import *
from android import *
from pc import *
#from setting import *
import threading
import os

#import argparse
#import cv2
import numpy as np
#import sys
import time
#import serial
from threading import Thread
#import importlib.util


class RaspberryPi(threading.Thread):
	def __init__(self):
		self.STMThread = STMRobot()
		self.pcThread = PCInterface()
		self.androidThread = AndroidApplication()

		#initalise connections
		#self.STMThread.connectToSTM()
		#self.androidThread.connectToAndroid()
		self.pcThread.connectToPC()

		time.sleep(1)

		print("Robot Startup")

	def multithread(self):
		#Android read and write thread
		#readAndroidThread = threading.Thread(target = self.readFromAndroid, args = (), name = "read_android_thread")
		#writeAndroidThread = threading.Thread(target = self.writeToAndroid, args = (), name = "write_android_thread")

		"""# STM read and write thread
		readSTMThread = threading.Thread(target = self.read_STM, args = (), name = "read_STM_thread")
		writeSTMThread = threading.Thread(target = self.write_STM, args = (), name = "write_STM_thread")"""

		# PC read and write thread
		readPCthread = threading.Thread(target = self.readFromPC, args = (), name = "read_pc_thread")
		writePCthread = threading.Thread(target = self.writeToPC, args = (), name = "write_pc_thread")

		# Set daemon for all thread      
		#readPCthread.daemon = True
		#writePCthread.daemon = True

		#readAndroidThread.daemon = True
		#writeAndroidThread.daemon = True

		# readSTMThread.daemon = True
		# writeSTMThread.daemon = True

		# start running the thread for PC
		readPCthread.start()

		# Start running thread for Android
		#readAndroidThread.start()
 
		# Start running thread for STM
		#readSTMThread.start()

	def disconnectAll(self):
		self.STMThread.disconnectFromSTM()
		self.androidThread.disconnectFromAndroid()
		self.pcThread.disconnectFromPC()

	def writeToAndroid(self, message):
		if(self.androidThread.isConnected):
			print("Sending Message")
			self.androidThread.writeToAndroid(message)
			return True
		return False

	def readFromAndroid(self):
		if(self.androidThread.isConnected):
			while True:
				# self.androidThread.connectAndroid()
				androidMessage = self.androidThread.readFromAndroid()
				# print("Read From Android: ", androidMessage)
		
	def readFromPC(self):
		if(self.pcThread.isConnected):
			while True:
				pcMessage = self.pcThread.readFromPC()
				print("Read from PC: ", str(pcMessage))
				# Insert message logic here
				#pcmsgArray = msgPC.split(":")
				#header = pcmsgArray[0]
				# if (self.pcThread.isItConnected() and msgPC):
				#     if(header == 'AN'):
				#        self.writeToAndroid(pcmsgArray[1])
				#     elif(header == 'STM'):
				#         self.writeToSTM(pcmsgArray[1])
				#     else:
				#         print("Incorrect header from PC : %s" %(msgPC)) 

	def writeToPC(self, message):
		if(self.pcThread.isConnected):
			self.pcThread.writeToPC(message)
			return True
		return False

	def writeToSTM (self, message):
		if (self.STMThread.isConnected and message):
			self.STMThread.writeToSTM(message)
			return True
		return False
	def readFromSTM (self):
		try:
			while True:
				serialmsg = self.STMThread.readFromSTM()
				print("Read from STM: ", str(serialmsg))
				#msg_remove = serialmsg.replace('@','')
				#new_msg = msg_remove.split(",")

				#serialmsgArray = new_msg[0].split(":")
				#header = serialmsgArray[0]
		except:
			print("Error")

if __name__ == "__main__":
	print("Program Starting")
	main = RaspberryPi()

	try:
		main.multithread()
		print("MultiTreading")

		try:
			print("send message")
			#main.writeToPC("Testing")
			#main.writeToSTM("Testing")
			main.writeToAndroid("Testing")
			#main.readFromAndroid()
		except Exception as e:
			print(str(e))

	except Exception as e:
		print(str(e))
		#main.disconnectAll()
	except KeyboardInterrupt as e:
		print("Terminating program")
		#main.disconnectAll()
		print("Program Terminated")
