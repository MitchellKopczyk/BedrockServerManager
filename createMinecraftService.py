import os
import getpass
import utils

config = utils.load_json_file("config.json")
server_path = config["ServerPath"]
flavor = config["Flavor"]

if flavor in utils.flavors:
    flavor_choice = utils.flavors[flavor]
else:
    print("Invalid flavor")

if flavor_choice == 1 or flavor_choice == 3:
    dir_name = "bedrock-server"
    exe_name = "bedrock_server"
    print("creating a service...")
    os.chdir("/etc/systemd/system")
    f = open("minecraft.service", "w")
    f.write("[Unit]\n")
    f.write("Description=Minecraft Bedrock Server\n")
    f.write("\n")
    f.write("[Service]\n")
    f.write("WorkingDirectory=" + server_path + dir_name + os.path.sep + "\n")
    f.write("ExecStart=" + server_path + dir_name + os.path.sep + exe_name + "\n")
    f.write("Restart=always\n")
    f.write("RestartSec=10\n")
    f.write("KillSignal=SIGINT\n")
    f.write("SyslogIdentifier=mc\n")
    f.write("User=" + getpass.getuser() + "\n")
    f.write("\n")
    f.write("[Install]\n")
    f.write("WantedBy=default.target\n")
    f.close()
    print("registering the service...")
    os.system("systemctl enable minecraft")
    print("Service Created")
    print("starting service...")
    os.system("systemctl start minecraft")
    print("service started")
    print("check status by typing systemctl status minecraft in your terminal")