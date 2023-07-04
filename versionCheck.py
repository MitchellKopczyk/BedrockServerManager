from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import utils
import datetime
import os

config = utils.load_json_file("config.json")
duration = config["Duration"]
server_path = config["ServerPath"]
dir_name = "bedrock-server"
flavor = config["Flavor"]

if flavor in utils.flavors:
    flavor_choice = utils.flavors[flavor]
else:
    print("Invalid flavor")
    
with open(os.path.abspath(os.path.dirname(__file__))+ os.path.sep + 'version_log.txt', 'a') as f:
    f.write("versionCheck Started: " + str(datetime.datetime.now()) + '\n')

while True:
    time.sleep(300) #sleep for a bit when user first logs in
    with open(os.path.abspath(os.path.dirname(__file__))+ os.path.sep + 'version_log.txt', 'a') as f:
        f.write("Checking online for updates: " + str(datetime.datetime.now()) + '\n')
    utils.get_latest_version_info_to_file(flavor_choice)
    time.sleep(duration)
