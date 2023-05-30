**Bedrock Server Manager** is a tool that lets you easily set up and manage your own dedicated bedrock server. 

## Why use Bedrock server manager?
The goal of this project is just to make it easier to manage your own dedicated server. Tasks like installing, updating, and creating a service so your server starts when you system boots are now simpler. In addition you can fully automate updates something mojang developers don't allow you to do currently.

## What systems are supported?
Ubuntu/Linux for now, theoretically any system could be implemented.

## How does it work?
Be sure to have Beautiful Soup installed via pip.

Clone the BedrockServerManager to a fixed location on your filesystem, if you move it you will have issues. Run all scripts as sudo or root and from the root of the BedrockServerManager directory. Backup up your server software/worlds manually every once in while!

1.) Modify the config.json, be sure include the file seperator at the end of ServerPath for now. Duration is how often you want to check for automated updates. I recommend 3600 seconds hence one hour.

    "ServerPath": "/home/alexsmith/",
    "Flavor": "Linux",
    "Duration" 3600

You can alternatively prefix Preview before your flavor choice to install the preview version
```
    "Flavor": "PreviewLinux"
```  
Then:

2.) Install a fresh copy of a server:
```
    sudo python3 install.py
```
besure to configure your server.properties like port number, etc...
</br>
If you need to ever need to manually update the server run:</br>
```
    sudo python3 update.py
```
worlds, resource_packs, behavior_packs, server.properties, allowlist.json, permissions.json from your current build are restored after applying an update.</br></br>

3.) create a service for Ubuntu/Linux:
```
    #this allows the server to run on boot
    sudo python3 createMinecraftService.py
```
If you ever need to remove the service for Ubuntu/Linux run:
```
    sudo python3 removeMinecraftService.py
```

4.) Create the manager service
```
    #this allows auto updating
    sudo python3 createManagerService.py
```
If you ever need to remove the manager service for Ubuntu/Linux run:
```
    sudo python3 removeManagerService.py
```

That's it feel free to play around with scripts and 
make them work for your application.
