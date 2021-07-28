from scapy.all import *

# decoys = {
#     "127.0.0.1":[443, 8443],
#     "10.10.10.0":[443, 8443],
# }

def analyzePackets(p):
    if p.haslayer(IP):
        decoyIP = [ip for ip in [p[IP].src, p[IP].dst]]
        print(decoyIP)
        if len(decoyIP) > 0:
            ports = None
            if p.haslayer(TCP):
                print("hasTCP")
                ports = [p[TCP].sport, p[TCP].dport]
            elif p.haslayer(UDP):
                print("hasUDP")
                ports = [p[UDP].sport, p[UDP].dport]
            decoyPort = [port for port in ports]
            if len(decoyPort) > 0:
                wrpcap("out.pcap",p,append=True)


sniff(prn=analyzePackets)