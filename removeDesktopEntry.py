import os

desktop_entry_path = os.path.expanduser("~/.config/autostart/bedrock-version-check.desktop")

if os.path.exists(desktop_entry_path):
    os.remove(desktop_entry_path)
    print("Desktop entry file removed successfully.")
else:
    print("Desktop entry file does not exist.")