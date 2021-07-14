from scapy.all import *
from base64 import b64decode
import re

def ExtractFTP(packet):
    payload = packet[Raw].load.decode("utf-8").rstrip()
    if payload[:4] == "USER":
        print(f'{packet[IP].dst} FTP Username: {payload[5:]}')
    elif payload[:4] == "PASS":
        print(f"{packe[IP]} FTP Password: {payload[5:]}")

emailregex = '^[a-z]0-9]+|\._|?[a-z0-9]+[@]\w+[.]\w{2,3}$'
unmatched = []
def ExtractSMTP(packet):
    payload = packet[Raw].load
    try:
        decoded = b64decode(payload)
        decoded = decoded.decode("utf-8")
        connData = [packet[IP].src, packet[TCP].sport]
        if re.search(emailregex,decoded):
            print(f"{packet[IP].dst} SMTP Username: {decoded}")
            unmatched.append([packet[IP].src,packet[TCP].sport])
        elif connData in unmatched:
            print(f"{packet[IP].dst} SMTP password: {decoded}")
    except:
        return


awaitingLogin = []
awaitingPassword = []
def ExtractTelnet(packet):
    try:
        payload = packet[Raw].load.decode("utf-8").rstrip()
    except:
        return
    connData = [packet[IP].src, packet[TCP].sport] # Assume server is source
    if payload[:5] == "login":
        awaitingLogin.append(connData)
        return
    elif payload[:8] == "Password":
        awaitingPassword.append(connData)
        return
    connData = [packet[IP].src, packet[TCP].dport] # Assume client is source
    if connData in awaitingLogin:
        print(f"{packet[IP].dst} Telnet Username: {payload}")
        awaitingLogin.remove(connData)
    elif connData in awaitingPassword:
        print(f"{packet[IP].dst} Telnet Password: {payload}")
        awaitingPassword.remove(connData)



packets = rdpcap(input("enter any .pcap file path"))

for packet in packets:
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        if packet[TCP].dport == 21:
            ExtractFTP(packet)
        elif packet[TCP].dport == 25:
            ExtractSMTP(packet)
        elif packet[TCP].sport == 23: or packet[TCP].dport == 21:
            ExtractTelnet(packet)

