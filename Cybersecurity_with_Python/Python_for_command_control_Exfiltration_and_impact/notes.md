# Python for Command-and-control
## MITRE ATTACK Command and Control
* Malware is rarley designed to operate completely authonomously:
    - Accept and execute commands from its operator
    - exfiltrate collected data from the target system

* Malware command-and-control channels contain sensitive information for the attacker
    - Insights into the malwares impact and operations on the infected systems

* Protecting malware against cyber defenders require protecting these command-and-control channels
    - Mae them more difficult to identify and decode

* An attcker can use a variety of different techniques to conceal command and control channels
    - Application Layer Protocol
    - Communication Through Removable Media
    - Data Encoding
    - Data Obfuscation
    - Dynamic Resolution
    - Encrypted Channel
    - Fallback Channels
    - Ingress Tool Transfer
    - Multi-Stage Channels
    - Non-Application Layer protocol
    - Non-Standard port
    - Protocol Tunneling
    - Proxy
    - Remote Access Software
    - Traffic Signaling 
    - Web Service

* Python can be used for command-and-control
    1. Encrypted Channel: symmetric cryptography
    2. Protocol Tunneling

## Introduction to Encrypted Channels
* Modern Encryption algorithms are secure against compromise
    - Cant be broken using modern technology
    - Data only decryptable with knowledge of the secret key

* This makes them an ideal solution for proctecting the confidentiality of command-and-control
    - Defenders can only read the data if they can access the appropriate encryption key

## Introduction to protocol tunneling
* Certin types of traffic are more common on an organizations network than others
    - Web
    - Email
    - DNS
    - And so on

* Hiding Command-and-Control data in this traffic makes it more likely to succeed:
    - Common traffic types are less suspicious than unusual ones
    - Common protocols are not blocked by the network firewall


# Python for exfiltration
## MITRE ATTACK Exfiltration
* A data breach is a multi-stage process:
    - Access an organizations systems
    - Identifying and accessing sensitive information on the network
    - Exfiltrating this data to systems under the attackers control

* When exfiltrating data stealth is essential
    - Defenders may block obvious data transfers
    - Data exfiltration may lead to malware detection and remediation

* MITRE Attack outines several methods for achieving data exfiltration:
    - Automated Exfiltration
    - Data Transfer Size Limits
    - Exfiltration Over alternative protocol
    - Exfiltration Over C2 channel
    - Exfiltration Over Other Network Medium
    - Exfiltration Over Physical Medium
    - Exfiltration Over Web Service
    - Scheduled Transfer
    - Transfer dat to Cloud Account

* This course applies Python to two techniques for data exfiltration
    1. Exfiltration over alternative protocols: Exfiltration over unencrypted/Obfuscated Non-C2 Protocol
    2. Non-Application layer protocol

## Alternative Protocols 
* Some Network protocols are designed for data transfer
    - This makes them easier to use for command and control and data exfiltration
    - It also makes them easier to detect

* Other network Protocols are capable of carrying data to an attacker
    - These alternatice protocols may be overlooked by those trying to identify command-and-control and adata exfiltration traffic


