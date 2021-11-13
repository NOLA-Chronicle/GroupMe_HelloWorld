import time
import os
import json
import sys
import socket

print("Loading...");

with open("config.json", "r") as in_configFile:
	config = json.load(in_configFile)

#Starting Up
print(config["StartingMsg"])

#Global Declarations
__GMPrivKey_API = os.environ['GroupMePrivKey']
__Port = os.environ['PORT']
host = config["IP_Address"]
baseURL = "https://api.groupme.com/v3"

while True:
	soc = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

	try:
		soc.bind((host, __Port))
	
	except socket.error as exception:
		print('Bind failed. Error Code : ' 
          + str(exception[0]) + ' Message ' 
          + exception[1])
		continue

	print("Socket Binding operation completed")
	print("Listening...")
	soc.listen(10)

	conn, address = soc.accept()
	print('Connected with ' + address[0] + ':' 
      + str(address[1]))

	#Main Code
	print("Ping #" + str(config["counter"]))

	#increment counter
	config["counter"] = config["counter"] + config["increment"]
	
	#Save to config file
	with open("config.json", "w") as out_configFile:
		json.dump(config, out_configFile)

