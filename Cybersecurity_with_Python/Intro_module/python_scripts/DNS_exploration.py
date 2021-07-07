#!/usr/local/Caskroom/miniconda/base/envs/cybersecurity/bin/python3

#DNS exploration
import dns
import dns.resolver
import socket

def reverse_DNS(ip):
    try:
        #get the domain name associated with that particular address
        result = socket.gethostbyaddr(ip)
    except:
        return []
    #get the value from result zero as a list and if there are more results we will append it to that list
    return [result[0]] + result[1]


def DNS_request(domain):
    try:
        #Using the dns library to look up a particular domain name, and requesting the "A" record (the most common record)
        result = dns.resolver.resolve(domain, "A")
        #if the domain request responds True (the domain exists)
        if result:
            #print the IP address
            print(domain)
            for answer in result:
                print(answer)
                #using reverse DNS function on the answers in result to find associated IP addresses
                print(f"Domain Names: {reverse_DNS(answer.to_text())}")
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return

def subdomain_search(domain, lst, nums):
    #iterate over each subdomain
    for word in lst:
        #create a full subdomain 
        subdomain = word+"."+domain
        #create a DNS request for that subdomain
        DNS_request(subdomain)
        # build an additional subdomain and DNS request 
        # with a number attached to it as it is common for the network to create subdomains that way
        if nums:
            for i in range(0,10):
                s = word+str(i)+"."+domain
                DNS_request(s)


domain = "google.com"
d = "../resources/subdomains.txt"
lst = []
with open(d, "r") as f:
    lst = f.read().splitlines()

subdomain_search(domain, lst, True)
