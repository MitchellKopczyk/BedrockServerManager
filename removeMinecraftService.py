import os
import utils

config = utils.load_json_file("config.json")
flavor = config["Flavor"]

if flavor in utils.flavors:
    flavor_choice = utils.flavors[flavor]
else:
    print("Invalid flavor")
 
if flavor_choice == 1 or flavor_choice == 3:
    print("haulting the service...")
    os.system("systemctl stop minecraft")
    print("service stopped")
    print("unregistering the service...")
    os.system("systemctl disable minecraft")
    print("unregistered service")
    print("deleting the service file...")
    os.remove("/etc/systemd/system/minecraft.service")
    print("service file deleted")
    print("done")