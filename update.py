import utils
import os
import sys
import shutil
import datetime
import json

config = utils.load_json_file("config.json")
server_path = config["ServerPath"]
flavor = config["Flavor"]

if flavor in utils.flavors:
    flavor_choice = utils.flavors[flavor]
else:
    print("Invalid flavor")

dir_name = "bedrock-server"
server_info_json_name = "serverinfo.json"
server_info = utils.load_json_file(server_path + dir_name + os.path.sep + server_info_json_name)
cur_ver = server_info["version"]

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'current_version.json')

try:
    json_string = utils.load_json_file(file_path)
    capture_ver = json.loads(json_string)
    download_url = capture_ver["download_url"]
    version_value = capture_ver["version"]
except Exception as e:
    print("No file version file found")
    print(file_path)
    sys.exit()

if(utils.compare_versions(version_value, cur_ver)) :
    print("new version found!")
    print("stopping the service...")

    if flavor_choice == 1 or flavor_choice == 3:
        os.system("systemctl stop minecraft")

    backup_path = server_path + "tmp-bedrock-backup"

    utils.backup(server_path, dir_name, backup_path)

    shutil.rmtree(server_path + dir_name)

    zip_name = "tmp-bedrock-server.zip"
    print("downloading...")
    stream = utils.download_stream(download_url)
    utils.write_stream(server_path + zip_name, stream)

    print("extracting zip...")
    dir_name = "bedrock-server"
    os.mkdir(server_path + dir_name)
    utils.unzip(server_path + zip_name, server_path + dir_name)
    os.remove(server_path + zip_name)

    serer_info = dict()
    serer_info['version'] = version_value
    utils.write_to_json(serer_info, server_path + dir_name + os.path.sep + server_info_json_name)

    utils.restore(server_path, dir_name, backup_path)
    
    shutil.rmtree(backup_path)

    if flavor_choice == 1 or flavor_choice == 3:
        exe_name = "bedrock_server"
        os.system("chmod +x " + server_path + dir_name + os.path.sep + exe_name)
        print("granted privillages!")
        os.system("systemctl start minecraft")
        print("Updated to version: " + version_value + "!")
        with open(os.path.abspath(os.path.dirname(__file__))+ os.path.sep + 'manager_log.txt', 'a') as f:
            f.write("Updated to version " + version_value + ":" + str(datetime.datetime.now()) + '\n')
else:
    print("Server is on the lastest version! " + version_value)