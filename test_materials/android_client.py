from bluetooth import *
import sys

if sys.version < '3':
    input = raw_input

addr = "CC:46:4E:E1:D0:1D"

if len(sys.argv) < 2:
    print("no device specified.  Searching all nearby bluetooth devices for")
    print("the SampleServer service")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on %s" % addr)

# search for the SampleServer service
uuid = "00001101-0000-1000-8000-00805F9B34FB"
service_matches = find_service( uuid = uuid, address = addr )
# service_matches = find_service()

print("service matches")
for i in service_matches:
    print("services: ", i)

if len(service_matches) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))
print("port " + str(port))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

print("connected.  type stuff here!")
nextIteration = True
while True:
    data = input()
    if len(data) == 0: break
    sock.send(data)
    print("From AA: " + str(sock.recv(1024)))

sock.close()
