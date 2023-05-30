import json
import utils
import os

config = utils.load_json_file("config.json")
server_path = config["ServerPath"]
flavor = config["Flavor"]

if flavor in utils.flavors:
    flavor_choice = utils.flavors[flavor]
else:
    print("Invalid flavor")

found = False
for dir in os.listdir(server_path):
    if "bedrock-server" in dir:
        found = True
        break
if found:
    print("A server already exists!")
else:
    print("Searching for latest version...") 

    capture_ver = json.loads(utils.get_latest_ver_info(flavor_choice))
    download_url = capture_ver["download_url"]
    version_value = capture_ver["version"]
    print(f"Attempting to download version {version_value}...")
    print("Downloading...")
    try:
        zip_name = "tmp-bedrock-server.zip"
        stream = utils.download_stream(download_url)
        utils.write_stream(server_path + zip_name, stream)
        print(f"Successfully downloaded version {version_value}!")
    except:
        print(f"Failed to download version {version_value}.")

    zip_name = "tmp-bedrock-server.zip"
    stream = utils.download_stream(download_url)
    utils.write_stream(server_path + zip_name, stream)

    print("Extracting zip...")
    dir_name = "bedrock-server"
    os.mkdir(server_path + dir_name)
    utils.unzip(server_path + zip_name, server_path + dir_name)
    os.remove(server_path + zip_name)

    server_info_json_name = "serverinfo.json"
    server_info = dict()
    server_info['version'] = version_value
    utils.write_to_json(server_info, server_path + dir_name + os.path.sep + server_info_json_name)

    if flavor_choice == 1 or flavor_choice == 3:
        exe_name = "bedrock_server"
        os.system("chmod +x " + server_path + dir_name + os.path.sep + exe_name)
        print("Granted privillages!")

    print("Install complete!")
    print("Version " + version_value + " was installed!")