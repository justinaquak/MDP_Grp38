from bluetooth import *
from setting import *
import time

#BLUETOOTH_PORT = 0 #some number 

class AndroidApplication(object):

	def __init__(self):
		#self.serverSocket = None
		self.sock = None
		self.isConnected = False

	def connectToAndroid (self):
		try:
			print("Connecting to Android Device")
			while True:
				service_matches = find_service( uuid = UUID, address = ANDROID_ADDR )
				if  len(service_matches) > 0:	
					first_match = service_matches[0]
					port = first_match["port"]
					host = first_match["host"]
					#print(service_matches)
					#print(service_matches[0])
					break
				else:
					print("Cannot find bluetooth device")
					time.sleep(1)
			
			self.sock = BluetoothSocket(RFCOMM)
			print("port: " + str(port) + "\nhost: " + str(host))
			print("Bluetooth port number : ", port)
	

			"""self.serverSocket.bind(("",port))
			self.serverSocket.listen(1)
			self.port = port"""

			self.sock.connect((host, port))
			print ("Successfully Connected to Android :)")
			print ("Connection via Bluetooth port: %s, host: %s" %(port, host))
			#self.sock, clientInfo = self.serverSocket.accept()
			#print ("Rpi has accepted connection from ", clientInfo)  
			self.isConnected = True

		except Exception as e:
			print ("Bluetooth connection has failed, waiting to reconnect. ", str(e))
			#self.sock.close()
			print ("Closing bluetooth connection")
			self.isConnected = False

	def disconnectFromAndroid (self):
		self.sock.close()
		print ("Closing bluetooth (client)")
		#print ("Closing bluetooth (server)")
		self.isConnected = False 

	def writeToAndroid (self, msg):
		try:
			self.sock.send(msg)
			print ("Sent to Android : %s" %(msg))
		except Exception as e:
			print("Error with Bluetooth(write): ", str(e))
			self.isConnected = False 
			#self.sock.close()
			self.connectToAndroid()

	def readFromAndroid (self):
		try:
			msg = self.sock.recv(1024)
			msg = msg.decode('utf-8')
			return (msg)
		except Exception as e:
			print("Error with Bluetooth(read): ", str(e))
			self.isConnected = False
			#self.sock.close()
			self.connectToAndroid()
