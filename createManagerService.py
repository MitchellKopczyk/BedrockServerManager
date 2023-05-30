import os
import getpass
import utils

config = utils.load_json_file("config.json")
flavor = config["Flavor"]

if flavor in utils.flavors:
    flavor_choice = utils.flavors[flavor]
else:
    print("Invalid flavor")

if flavor_choice == 1 or flavor_choice == 3:
    print("creating a service...")
    os.chdir("/etc/systemd/system")
    f = open("BedrockServerManager.service", "w")
    f.write("[Unit]\n")
    f.write("Description=Bedrock Server Manager\n")
    f.write("\n")
    f.write("[Service]\n")
    f.write("WorkingDirectory=" + os.path.abspath(os.path.dirname(__file__)) + "\n")
    f.write("ExecStart=""/usr/bin/python3 " + os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "manager.py""\n")
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
    os.system("systemctl enable BedrockServerManager")
    print("Service Created")
    print("starting service...")
    os.system("systemctl start BedrockServerManager")
    print("service started")
    print("check status by typing systemctl status BedrockServerManager in your terminal")