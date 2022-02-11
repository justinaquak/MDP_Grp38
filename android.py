from bluetooth import *
from setting import *
import time

#BLUETOOTH_PORT = 0 #some number 

class AndroidApplication(object):

	def __init__(self):
		#self.serverSocket = None
		self.sock = None
		self.connection = False

	def isConnected (self):
		return self.connection

	def connectToAndroid (self):
		try:
			service_matches = find_service( uuid = UUID, address = ANDROID_ADDR )
			
			#print(service_matches)
			#print(service_matches[0])
			first_match = service_matches[0]
			port = first_match["port"]
			host = first_match["host"]
			print("port: " + str(port) + "\nhost: " + str(host))
			print("Bluetooth port number : ", port)
			self.sock = BluetoothSocket(RFCOMM)

			"""self.serverSocket.bind(("",port))
			self.serverSocket.listen(1)
			self.port = port"""

			self.sock.connect((host, port))
			print ("Successfully Connected to Android :)")
			print ("Connection via Bluetooth RFCOMM channel %d" %port)
			#self.sock, clientInfo = self.serverSocket.accept()
			#print ("Rpi has accepted connection from ", clientInfo)  
			self.connection = True

		except Exception as e:
			print ("Bluetooth connection has failed, waiting to reconnect. ")
			#self.sock.close()
			print ("Closing bluetooth connection")
			self.connection = False
			raise

	def disconnectFromAndroid (self):
		self.sock.close()
		print ("Closing bluetooth (client)")
		# self.serverSocket.close()
		#print ("Closing bluetooth (server)")
		self.connection = False 

	def writeToAndroid (self, msg):
		try:
			print(msg)
			self.sock.send(msg)
			print ("Sent to Android : %s" %(msg))

		except Exception as e:
			print("Error with Bluetooth(write): ", str(e))
			#self.connectToAndroid()

	def readFromAndroid (self):
		try:
			#sleep(100)
			msg = self.sock.recv(1024)
			msg = msg.decode('utf-8')
			print("Received from Android: %s" % str(msg))
			return (msg)

		except Exception as e:
			print("Error with Bluetooth(read): ", str(e))
			#self.connectToAndroid()
