#scapy library used for working with network traffic 
from scapy.all import *

#using the scapy rdpcap function to read a packet capture file downloaded from wireshark
packet = rdpcap("../resources/v6-http.cap")

#collection of different packes
#packet 
#<v6-http.cap: TCP:10 UDP:8 ICMP:0 Other:37>
# 10 TCP packets, 8 UDP, and 37 other
