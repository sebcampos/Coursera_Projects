#!/usr/local/Caskroom/miniconda/base/envs/cybersecurity/bin/python3

import paramiko
import telnetlib

def SSH_login(host, port, username, password):
    try:
        #paramiko ssh client
        ssh = paramiko.SSHClient()
        #ignore the fact that server host key is not in our list of trusted keys
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )
        #perform the login
        ssh.connect(
            host,
            port = port,
            username = username,
            password = password
        )
        #open the session attempt after connection
        ssh_session = ssh.get_transport().open_session()
        #check to see if our ssh session is active and successful
        if ssh_session.active:
            print(f"SSH login successful on {host}:{port} with username {username} and password {password}")
    except Exception as e:
        return
    ssh.close()

def telent_login(host, port, username, password):
    user = bytes(username + "\n","utf-8")
    passwd = bytes(password + "\n","utf-8")
    #used for IoT devices
    tn = telnetlib.Telnet(host, port)
    # reads data off of the wire until it finds this login prompt. Only works if we have the correct login prompt
    tn.read_until(bytes("login: ", "utf-8"))
    tn.write(user)
    tn.read_until(bytes("Password: ","utf-8"))
    tn.write(passwd)
    try:
        #searching for the last login (most IoT have this )
        result = tn.expect(
            [bytes("Last login", "utf-8")],
            timeout = 2
        )
        if result[0] >= 0:
            print(f"Telnet login successful on {host}:{port} with username {username} and password {password}")
        tn.close()

    except EOFError:
        print(f"Login failed {username} {password}")

host = "127.0.0.1"
with open("../resources/defaults.txt","r") as f:
    for line in f:
        vals = line.split()
        username = vals[0].strip()
        password = vals[1].strip()
        SSH_login(host, 22, username, password)
        telent_login(host, 23, username, password)