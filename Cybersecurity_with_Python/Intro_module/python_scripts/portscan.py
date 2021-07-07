#!/usr/local/Caskroom/miniconda/base/envs/cybersecurity/bin/python3

from scapy.all import *

ports = [25, 80, 53, 443, 445, 8080, 8443]

def sync_scan(host):
    #using sr function to send and listen for responses on a host given a list of ports
    #ans will return all the answered packets and unans will return all the unanswered packets
    ans, unans = sr(
        #building a simple packet
        IP(dst = host) / TCP(sport = 5555, dport = ports, flags="S"), timeout = 2, verbose = 0
        )
    #looping over the answered packets to reveal open ports
    print(f"Open ports at {host}")
    #s = sent, r = recieved
    for (s,r,) in ans:
        # is the sent destination port is equal to the recieved port print the port
        if s[TCP].dport == r[TCP].sport:
            print(s[TCP].dport)

def DNS_scan(host):
    #checking to see if a particular port properly responds to a DNS request
    ans, unans = sr(
        #building a simple packet for DNS
        IP(dst = host) / UDP(sport = 5555, dport = 53) / DNS(rd = 1, qd = DNSQR(qname="google.com")), timeout = 2, verbose = 0
    ) 
    if ans:
        print(f"DNS Server at {host}")
    
host = "8.8.8.8"

sync_scan(host)
DNS_scan(host)

