import platform

def setWindowsPassword(username, password):
    from win32com import adsi
    ads_obj = adsi.ADsGetObject(f"WinNT://localhost/{username},user")
    ads_obj.GetInfo()
    ads_obj.SetPassword(password)


def setLinuxPassword(ysername, password):
    os.system(f'echo -e "newpass\nnewpass" | passwd {username}')

def changeCriteria(username):
    if username in ["testuser","user1"]:
        return True
    else:
        return False

if platform.system() == "Windows":
    import wmi
    w = wmi.WMI()
    for user in w.Win32_UserAccount():
        username = user.Name
        if changeCriteria(username):
            print(f"Changing password {username}")
            setWindowsPassword(username, "newpass")


else:
    import pwd
    for p in pwd.getpwall():
        if p.pwd_uid == 0 or p.pwd_uid > 500:
            username = p.pwd_name
            if changeCriteria(username):
                print(f"Chanign password: {username}")
                setLinuxPassword(username, "newpass")