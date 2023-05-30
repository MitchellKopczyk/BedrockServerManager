import time
import utils
import datetime
import os

config = utils.load_json_file("config.json")
duration = config["Duration"]

with open(os.path.abspath(os.path.dirname(__file__))+ os.path.sep + 'log.txt', 'a') as f:
    f.write("Manager Started: " + str(datetime.datetime.now()) + '\n')

while True:
    time.sleep(duration)
    with open(os.path.abspath(os.path.dirname(__file__))+ os.path.sep + 'log.txt', 'a') as f:
        f.write("Checking for updates: " + str(datetime.datetime.now()) + '\n')
    with open(os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "update.py") as f:
        exec(f.read())