# Decoys
## Introduction to decoys
"All warefare is based on deception"
- Sun Tzu

* Cyberattackers commonly use deceptive tactics to hide their activities. Active defenders can employ deception as well:
    - Honeypots: decoy systems and data
    - Honey data: Fake data designed to distract and misdirect

* Deception and decoys provide a number of benefits for active defense:
    - Waste the attackers time
    - Allows the defender to control the attackers actions
    - Simplifies detection of threats on a system
    - Provides intelligence about an attackers TTPs

## Decoys for active defense
* Decoys can be used in active defense in several different ways. This course demonstrates three applications of decoys for active defense
    1. Decoy Processes
    2. Decoy content
    3. Decoy credentials

## Decoy Process for active defense
* A decoy process is a program masquerading as something else. Decoy proccesses can be applied to several active defense use cases:
    - Creation of artifacts directing attackers to decoy system
    - Making a system seem more vulnerable or enticing to an attacker
    - Influence an attackers behaviour based on processes present on a system


## Decoy content for active defense
* Decoy Content is misleading data placed on a system. Some applications of decoy content include:
    - Directing an attacker toward decoy systems
    - Observing an attackers presence on a system
    - Make decoy systems look more legitimate to an attacker


## Decoy credentials for active defense
* A defender can seed a system with fake credentials for an attacker to discover. This sets up a number of use cases including:
    - Directing an attacker to decoy systems 
    - Treacking an attackers access
    - Causing an attacker to steal fake data
    - wasting an attackers time with invalid credentials


# Network
## Active defense on a network
* The network is a valuable resource for attackers and defenders alike
    - Most cyberattacks occur over the network
    - Network traffic is an easily accessible source of data

* Using the network for data analysis and building decoys supports active defense
    - Data collection and active response are essential to active defense
    - Analysis of network-level data provides intelligence on attacker TTPs

## Network-level active defense
* This course explores the use of Python for three forms of network-level active defense:
    - PCAP collection
    - Protocol decoding
    - Burn-in

## PCAP collection for active defense
* PCAP collection supports active defense in a few different ways:
    - Collection of network traffic from a compromised system
    - Detection of traffic abnormalities signaling data obfuscation
    - Analysis of C2 and data exfiltration traffic

## Protocol Decoding
* Malware authors commonly encode or encrypt their C2 traffic to make it more difficult for defenders to analyze. Implementing automated protocol decoding can be applied to active defense use cases:
    - Malware reverse engineering can produce C2 traffic decoders
    - Decoding and decryption of network traffic enables C2 traffic analysis


## Burn-in
* A key part of deception is making the decoy look plausible and desirable. Burn-in can be applied to active defense in a few ways:
    - Creation and use of a decoy account to create legitimate-looking system artifacts
    - Use of a set of decoy sites to create cookies for adversaries to harvest and use
    - Perform web browsing to set up a fake browsing history for a decoy user

# Monitoring
## Introduction to monitoring
* Monitoring is essental to active defense
    - Active defense requires identified threats
    - Monitoring provides the data for threat identification

* Monitoring Also supports other actice defense efforts
    - Enables defenders to track the efficacy of deception, etc.

* This course explores three applicatoins of monitoring for active defense:
    1. Network monitoring
    2. System activity monitoring
    3. Behavioral analytics

## Network monitoring for active defense
* Many cyberattacks occur over the network. Network monitoring can be applied to several network defense use cases:
    - Identification of malicious traffic
    - Detection of unusual traffic encapsulation (RDP over TCP, etc)
    - Monitoring for anomalous traffic patterns

