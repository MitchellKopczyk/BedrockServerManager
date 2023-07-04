import time
import utils
import datetime
import os
import subprocess

config = utils.load_json_file("config.json")
duration = config["Duration"]

with open(os.path.abspath(os.path.dirname(__file__))+ os.path.sep + 'manager_log.txt', 'a') as f:
    f.write("Manager Started: " + str(datetime.datetime.now()) + '\n')

while True:
    time.sleep(duration)
    with open(os.path.abspath(os.path.dirname(__file__))+ os.path.sep + 'manager_log.txt', 'a') as f:
        f.write("Manager Checking: " + str(datetime.datetime.now()) + '\n')
    with open(os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "update.py") as f:
        subprocess.run(["python3"], stdin=f)