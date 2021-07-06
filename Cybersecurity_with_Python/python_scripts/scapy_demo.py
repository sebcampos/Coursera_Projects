#scapy library used for working with network traffic 
from scapy.all import *

#using the scapy rdpcap function to read a packet capture file downloaded from wireshark
packet = rdpcap("../resources/v6-http.cap")

#collection of different packes
#packet 
#<v6-http.cap: TCP:10 UDP:8 ICMP:0 Other:37>
# 10 TCP packets, 8 UDP, and 37 other

#pull out very first pack and look at contents
packet[0].show()

#Output
# ###[ Ethernet ]###
#   dst       = 33:33:ff:82:95:b5
#   src       = 00:11:25:82:95:b5
#   type      = IPv6
# ###[ IPv6 ]###
#      version   = 6
#      tc        = 0
#      fl        = 0
#      plen      = 32
#      nh        = ICMPv6
#      hlim      = 255
#      src       = fe80::211:25ff:fe82:95b5
#      dst       = ff02::1:ff82:95b5
# ###[ ICMPv6 Neighbor Discovery - Neighbor Solicitation ]###
#         type      = Neighbor Solicitation
#         code      = 0
#         cksum     = 0x79e6
#         res       = 0
#         tgt       = 2001:6f8:102d:0:211:25ff:fe82:95b5
# ###[ ICMPv6 Neighbor Discovery Option - Source Link-Layer Address ]###
#            type      = 1
#            len       = 1
#            lladdr    = 00:11:25:82:95:b5

