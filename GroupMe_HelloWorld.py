import time
import os
import json

print("Loading...");

with open("config.json", "r") as in_configFile:
	config = json.load(in_configFile)

#Starting Up
print(config["StartingMsg"])

#Global Declarations
__GMPrivKey_API = os.environ['GroupMePrivKey']
baseURL = "https://api.groupme.com/v3"

print("Ping #" + str(config["counter"]))

config["counter"] = config["counter"] + config["increment"]


with open("config.json", "w") as out_configFile:
	json.dump(config, out_configFile)

