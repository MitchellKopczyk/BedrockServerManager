import os
import utils

config = utils.load_json_file("config.json")
server_path = config["ServerPath"]
dir_name = "bedrock-server"

script_path = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "versionCheck.py"
desktop_entry_directory = os.path.expanduser("~/.config/autostart")
desktop_entry_path = os.path.join(desktop_entry_directory, "bedrock-version-check.desktop")

desktop_entry_content = f"""[Desktop Entry]
Type=Application
Exec=/usr/bin/python3 {script_path}
Path={os.path.abspath(os.path.dirname(__file__))}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=bedrock-version-check
"""

# Create the necessary directory if it doesn't exist
os.makedirs(desktop_entry_directory, exist_ok=True)

with open(desktop_entry_path, "w") as file:
    file.write(desktop_entry_content)

print("Desktop entry file created successfully.")
print("Please reboot your PC Now!")
print("After your PC reboots and your logged, chrome will auto fetch the latest version number")
print("Your PC will do this everytime from now until you run the removeDesktopEntry script and reboot")