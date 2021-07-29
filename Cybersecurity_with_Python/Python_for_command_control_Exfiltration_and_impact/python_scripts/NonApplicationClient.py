from scapy.all import *

def transmit(message, host):
    for m in message:
        mac = get_if_hwaddre(conf.iface)
        packet = Ether(src=mac, dst=mac) / IP(dst=host)/ICMP(code = ord(m))
        sendp(packet, verbose = False)



host = "10.10.10.8"
message = "Hello"
transmit(message, host)

