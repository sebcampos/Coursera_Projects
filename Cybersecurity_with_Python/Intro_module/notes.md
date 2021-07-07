# Cyber Security With Python

## Course
- mitre's attack
- mitre's frameworks

### MITRE Terms
- tactics: 
        
        the tactical goal at a particular stage of a cyberattack or a goal in active defense 

- techniques

        a mechanism by which an attacker can achieve the goal outlined in a particular Tactic
        A sub technique is a method for carrying out a particular technique

- Procedure 

        A specific implementation of a particular technique or sub-technique


### MITRE ATTACK tacitics
1. Pre-ATTACK: Reconnaissance and Resource Development
2. Inital Access
3. Execution
4. Persistence
5. Privilege Escalation
6. Defense Evasion
7. Credential Access
8. Discovery
9. Lateral Movement
10. Collection
11. Command and Control
12. Exfiltration
13. Impact

### MITRE SHIELD tactics
1. Channel
2. Collect
3. Contain
4. Detect
5. Disrupt
6. Facilitate
7. Legitimize
8. Test

### Resources for Course
Code location: https://github.com/hposton/python-for-cybersecurity
Required Python libraries: 
- asyncssh
- brython
- dnspython
- httpserver
- libratom
- paramiko
- psutil
- pycryptodomex 
- pyinstaller
- requests
- scapy
- urllib
- wmi **might have issues

## MITRE PRE-ATTACK
Reconnaissance 
The first stage of PRE-ATTACK focuses on gathering target information from a variety of different sources
- active scanning
- Gather victim Host information
- Gather victim Identity information
- Gather Victim network information
- Gather Victim Org Information
- Phishing for information
- Search Closed Sources
- Search open Technical databases
- Search Open websites/domains
- Search Victim-Owned websites

Resource Development
The second stage of PRE ATTACK involves the attacker developing or acquiring the tools needed to perform their attack
- Acquire Infrastructure
- Compromise Accounts
- Compromise Infrastructure
- Develop Capabilities
- Establish Accounts
- Obtain Capabilities

## Introduction to network scanning
Network scanning
- identification of potential target systems
- discovery of vulnerable applications
- Port scanning
- Banner collection
- Vulnerability scanning

## Introduction to scapy
- Scapy is a python module designed for working with network traffic, see portscan.py

## Open Technical databases
Open-source intelligence (OSINT) is a trove of useful data regarding an organization and its systems
examples of these dataets include:
- WHOIS: WHOIS records may include data about owners of websites, system administrators, etc
- DNS: DNS maps domain names to IP addresses
- CDNs: CDNs store cached content for an organizations websites


## DNS exploration
- see DNS_exploration.py file 

## Initial Access
Initial Access is where an attack transitions from planning to execution:
- attacker exploits a vulnerability discovered during PRE-ATTACK
- Potentially, this is the first time the attacker interacts with the target network

The lines between the MITRE ATTACK stages can be blurred at this point
- perfomring a SQL injection attack to test for a vulnerability can cover reconnaissance, inital access and later Tactics

### MITRE Attack initial access
The mitre attack framework outlines a number of different techniques by which an attacker can achieve inital access
- Drive-by Comprimise
- Exploit Public-Facing Application
- External Remote services 
- Hardware Additions
- Phishing
- Rreplication Through removable media
- Supply Chain compromise
- Trusted relationship
- Valid accounts

### Python for initial Access
Python code can be applied to several of the initial access techniques and sub-techniques
- Many Attack vectors can be automated at some level

This course will demonstrate two applications of Python for inital access
- Valid accounts: Default Account Discovery
- Replication Through removable media: Autorun scripts

### Valid Accounts
* valid accounts are a necessary weakness in an organizations defenses 
    - Users need access to networks, systems, applications, etc

* Attackers commonly target these accounts in their attack
    - User passwords are relatively Easy to compromise
    - Authenticating as a legitimate user makes detection more difficult

### Removable media
* Removable media can be a difficult attack vector to detect
    - USB traffic doesnt flow over the network
    - Many employees have legitimate needs for removable media
    - removable media makes attack chain analysis more difficult

* Compromised removable media can be used to deliver malware in a number of ways 
    - USB autorun scripts
    - Social engineering

