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
- Scapy is a python module designed for working with network traffic



