<img src="https://raw.githubusercontent.com/MitchellKopczyk/BedrockServerManager/main/minecraft.png" width="200" height="200">

# Bedrock Server Manager

Bedrock Server Manager is a tool that lets you easily set up and manage your own dedicated Bedrock server.

## Table of Contents

- [Why use Bedrock server manager?](#why-use-bedrock-server-manager)
- [Dependencies](#dependencies)
- [Installation](#installation)

## Why use Bedrock server manager?

The goal of this project is to simplify managing your own dedicated server. Tasks like installing, updating, and creating a service so your server starts when your system boots are now easier. Moreover, you can fully automate updates, a feature currently not provided by Mojang developers.

## Dependencies

Before running the scripts, ensure the following dependencies are installed:
- Ubuntu (GNOME GUI Versions Only): LTS or non LTS
- selenium: Install using pip3: ```pip3 install selenium```
- chromium: Install using snap: ```sudo snap install chromium```
- chromedriver: Install using apt: ```sudo apt install chromium-chromedriver -y```
- Auto User Login: For uninterrupted functionality, the user needs to remain logged in at all times in the GNOME desktop enviroment. Configure your system settings to prevent the desktop from going to sleep, as Chrome must run in headed mode to check for updates. For enhanced security, limit the user permissions accordingly.

## Installation

Clone the BedrockServerManager to a fixed location on your filesystem. If you move it, you may encounter issues. Run all scripts from the root of the BedrockServerManager directory. Remember to manually backup your server software/worlds occasionally! Be sure also to do this inital setup from the Server from the GNOME Desktop otherwhise selenium will throw errors.

### Configure the Config File
Modify the config.json, ensuring to include the file separator at the end of ServerPath. Duration is how often you want the server to check for an update.

```
{
    "ServerPath": "/home/alexsmith/",
    "Flavor": "Linux",
    "Duration": 3600
}
```

For installing the preview version, prefix 'Preview' before your flavor choice:

```
{
    "Flavor": "PreviewLinux"
}
```

### Install Server

Install a fresh copy of the server. Do not run this script as root, sudo, or su.

```
python3 install.py
```

Make sure to configure your server.properties, like the port number, etc.

### Create Services

Create a service. This allows the server to run on boot.

```
sudo python3 createMinecraftService.py
```

To remove the service, run:

```
sudo python3 removeMinecraftService.py
```

Create the manager service. This is needed for auto updating to work.

```
sudo python3 createManagerService.py
```

If you ever need to remove the manager service, run:

```
sudo python3 removeManagerService.py
```

### Create Desktop Entry

Create a desktop entry. This allows checking for updates from server download site. Do not run this script as root, sudo, or su.

```
python3 createDesktopEntry.py
sudo reboot
```

If you ever need to remove the desktop entry run Do not run this script as root, sudo, or su.: 

```
python3 removeDesktopEntry.py
sudo reboot
```

That's it! Feel free to play around with scripts and make them work for your application. I wrote this because other managers seem to break all the time.
