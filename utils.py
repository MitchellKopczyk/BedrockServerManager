import ssl
import urllib.request
import zipfile
import json
import requests
import os
import shutil
from bs4 import BeautifulSoup

def download_stream(url) :
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(url, context=context)
    return response.read()

def write_stream(dst, stream) :
    with open(dst, "wb") as f:
        f.write(stream)

def unzip(src, dst) :
    with zipfile.ZipFile(src, "r") as z:
        z.extractall(dst)

def load_json_file(src):
    with open(src, "r") as f :
        return json.load(f)

def write_to_json(data, dst):
    with open(dst, "w") as outfile :
        json.dump(data, outfile)

def compare_versions(v1, v2) :
    v1_parts = v1.split('.')
    v2_parts = v2.split('.')
    for i in range(min(len(v1_parts), len(v2_parts))):
        if int(v1_parts[i]) > int(v2_parts[i]):
            return True
        elif int(v1_parts[i]) < int(v2_parts[i]):
            return False
    if len(v1_parts) > len(v2_parts):
        return True
    elif len(v1_parts) < len(v2_parts):
        return False
    else:
        return False
    
def get_latest_ver_info(serverType):
    download_urls = {
        0: "https://minecraft.azureedge.net/bin-win/bedrock-server-",
        1: "https://minecraft.azureedge.net/bin-linux/bedrock-server-",
        2: "https://minecraft.azureedge.net/bin-win-preview/bedrock-server-",
        3: "https://minecraft.azureedge.net/bin-linux-preview/bedrock-server-"
    }
    download_url = download_urls[serverType]

    url = 'https://minecraft.fandom.com/api.php'
    params = {
        'action': 'parse',
        'page': 'Bedrock_Dedicated_Server',
        'format': 'json'
    }

    response = requests.get(url, params=params)
    data = response.json()
    page_content = data['parse']['text']['*']
    soup = BeautifulSoup(page_content, 'html.parser')

    if serverType in [0, 1]:
        table = soup.find_all('table', {'class': 'mw-collapsible mw-collapsed wikitable'})[0]
    else:
        table = soup.find_all('table', {'class': 'mw-collapsible mw-collapsed wikitable'})[1]

    rows = table.find_all('tr')

    ver_info = dict()
    for row in rows:
        version = row.find('th').text.strip()
        ver_info['version'] = version
        ver_info['download_url'] = download_url + version + ".zip"

    ver_JSON = json.dumps(ver_info)
    return ver_JSON

flavors = {
    "Windows": 0,
    "Linux": 1,
    "PreviewWindows": 2,
    "PreviewLinux": 3
}

def backup(server_path, dir_name, backup_path):
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    if os.path.exists(server_path + dir_name + os.path.sep + "worlds"):
        shutil.copytree(server_path + dir_name + os.path.sep + "worlds", backup_path + os.path.sep + "worlds")
    else:
        print("The directory does not exist.")

    if os.path.exists(server_path + dir_name + os.path.sep + "resource_packs"):
        shutil.copytree(server_path + dir_name + os.path.sep + "resource_packs", backup_path + os.path.sep + "resource_packs")
    else:
        print("The directory does not exist.")

    if os.path.exists(server_path + dir_name + os.path.sep + "behavior_packs"):
        shutil.copytree(server_path + dir_name + os.path.sep + "behavior_packs", backup_path + os.path.sep + "behavior_packs")
    else:
        print("The directory does not exist.")

    if os.path.exists(server_path + dir_name + os.path.sep + "server.properties"):
        shutil.copy(server_path + dir_name + os.path.sep + "server.properties", backup_path)
    else:
        print("The file does not exist.")

    if os.path.exists(server_path + dir_name + os.path.sep + "allowlist.json"):
        shutil.copy(server_path + dir_name + os.path.sep + "allowlist.json", backup_path)
    else:
        print("The file does not exist.")

    if os.path.exists(server_path + dir_name + os.path.sep + "permissions.json"):
        shutil.copy(server_path + dir_name + os.path.sep + "permissions.json", backup_path)
    else:
        print("The file does not exist.")
        
def restore(server_path, dir_name, backup_path):
    if not os.path.exists(backup_path):
        print("The backup directory does not exist.")
        return

    try:
        if os.path.exists(server_path + dir_name + os.path.sep + "worlds"):
            shutil.rmtree(server_path + dir_name + os.path.sep + "worlds")
        if os.path.exists(backup_path + os.path.sep + "worlds"):
            shutil.copytree(backup_path + os.path.sep + "worlds", server_path + dir_name + os.path.sep + "worlds")

        if os.path.exists(server_path + dir_name + os.path.sep + "resource_packs"):
            shutil.rmtree(server_path + dir_name + os.path.sep + "resource_packs")
        if os.path.exists(backup_path + os.path.sep + "resource_packs"):
            shutil.copytree(backup_path + os.path.sep + "resource_packs", server_path + dir_name + os.path.sep + "resource_packs")

        if os.path.exists(server_path + dir_name + os.path.sep + "behavior_packs"):
            shutil.rmtree(server_path + dir_name + os.path.sep + "behavior_packs")
        if os.path.exists(backup_path + os.path.sep + "behavior_packs"):
            shutil.copytree(backup_path + os.path.sep + "behavior_packs", server_path + dir_name + os.path.sep + "behavior_packs")

        if os.path.exists(backup_path + os.path.sep + "server.properties"):
            shutil.copy(backup_path + os.path.sep + "server.properties", server_path + dir_name)
        else:
            print("The file does not exist.")

        if os.path.exists(backup_path + os.path.sep + "allowlist.json"):
            shutil.copy(backup_path + os.path.sep + "allowlist.json", server_path + dir_name)
        else:
            print("The file does not exist.")

        if os.path.exists(backup_path + os.path.sep + "permissions.json"):
            shutil.copy(backup_path + os.path.sep + "permissions.json", server_path + dir_name)
        else:
            print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")