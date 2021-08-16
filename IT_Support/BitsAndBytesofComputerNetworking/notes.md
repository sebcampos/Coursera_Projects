# The Bits and bytes of Computer Networking

## TCP/IP Five Layer Network Model
* physical layer
    - represents the physcial devices that interconect computers
    - includes the specifications for the networking cables and connectors that join devices
    - how signals are sent over these connections
* Data link layer
    - network interface/network access layer
    - Ethernet (one of the most common protocols)
    - our first protocols
    - Responsible for defining a common way of interpreting these signals so network devices can communicate
    - - responsible for getting data across a single link
* Network layer
    - internet layer
    - allows different networks to communicate with each other through devices known as routers
    - a collection of networks connected together through routers is an internetwork. The most famous internetwork is the Internet
    - responsible for getting data across a collection of networks
    - most common protocol here is the IP protocol

* Transport layer
    - Sorts out which client and server programs are supposed to get the data brought in by the network layer
    - TCP is the most common protocol in this layer

* Application layer
    - Many different protocols at this layer

## Cables
* copper
    - Binary is transmited through these wires by changeing the voltage between two ranges. The recieving end will read these changes and translate to different forms of data
    - the most common forms of copper twisted-pair cables used in networking are Cat5, Cat5e, and Cat6
    - Crosstalk is an issue when an electrical pulse on one wire is accidently transmited to another wire

* fiber
    - Contain individual optical fibers, which are tiny tubes made out of glass about the width of a human hair
    - Fiber cables use pulses of light to represent binary data
    - Generally transport data faster, more reliably, and over longer distances than their copper counter parts. Electromagnetic activity surronding these wires will not effect them the same way it does copper wires.
    - These wires are much more expensive and fragile than copper wires

## Hubs and Switches
Hubs and switches are the primary devices used to connect computers on a single network usually referred to as a LAN, or local area network

Hubs are slower and more antiquated
Switches will inspect data and decide where to send it (which application, domain, etc) so that there are no collisions

## Routers
A device that knows how to forward data between independent networks
- Operated at layer 3 (network layer)
- inspects IP data to determine where to send information
- store internal tables on how to route traffic between lots of different networks all over the world
- Core routers are the backbone of the iternet -ISP routers send traffic around the world

## Servers and Clients
A server provides data to something requesting data. The One recieving the data is the client
Nothing really is only a client or a server usually the two are the same item
- computer is both a server and a client. But because usually it is recieveing data for a client it will more commonly be refered to as a client


## The Physical Layer
A bit is the smallest piece of data a computer can understand. It is a 1 or a 0
- modulation is the way of varying the voltage of a charge moving accross the cable
- modulation moves bits accross the wire
- The most common form of cabling used for connecting computers are called twisted pairs - copper wire
- In most modern computers there is Duplex communication across these wires. The concept that information can flow in both directions across the cable
- Simplex communication is where data can only be sent one direction
- Network ports are attached directly to the device

## The Data Link Layer
Ethernet and MAC addresses
- Ethernet connection is older but still prefered
- Ethernet solved our colisions issue allowing devices to detect when other computers where sending data and wait to send data so that two electrical pulses were not being sent at the same time

Unicast, multicast, Broadcast
- A unicast transmission is always meant for just one receiving address


## Network Layer
### IP Addresses
- IP addresses are 32 bit long numbers made up of four octets
- 8 bits of data or a single octed can represent all decimal numbers from 0 to 255
- IP adresses belong to the network and are assigned by the current network
- Dynamic host configuration protocol is when an IP address is automatically assigned via dynamic IP on modern devices

### IP datagrams and encapsulation
- a packet is also called a datagram , contains a header and a payload
- first fielt is 4 bits containing the version
- second field is 20 bytes containing the header length
- third is service type field, 8 bites that can be used to specify details about quality of service of QoS technologies, this helps computers determine which packets are most important
- fourth field is the total length field. indicates the length of the entire packet
- fifth field is the identification field a 16-bit number thats used to group messages together
- is the total amount of data that needs to be sent is larger than what we can fit in a single datagram (packet), the IP layer needs to slit this data up into many individual packets
- sixth field is the Time to Live (TTL) field an 8-bit field that indicates how many router hops a datagram can traverse before its thrown away - every time  a datagram encounters a new router this field decrements by one, once it hits 0 the router will not forward it anymore
- seventh field 8 bit is the protocol field that contains data bout what transport layer protocol is being used
- eigth field is the header checksum field, a checksum of the contents of the entire IP datagram header
- nineth field is the source IP address (32bits) 
- tenth field is the destination IP address (32bits)
- eleventh layer is the IP otptions field An optional field and is used to set special characteristics for datagrams primarily used for testing purposes
- twelve layer is the padding field a series of zeros used to ensure the header is correct total size

### IP Address Classes
9.100.100.100
octet = 9. or .100 (anything seperated by .)
network ID = 9
host ID = 100.100.100
- The address class system is a way of defining how th global IP address space is split up
- Three primary types of class adress:
    * Class A has the first octet used for the network ID and the last three are used for the host ID - 8 bits
    * Class B First two octets are used for the network ID and the second 2 are used for the host ID - 16 bits
    * Class C First three octets are used for the network ID and only the final octet is used for the host ID - 24 bits

### Address Resolution Protocol
ARP
- ARP is a protocol used to discover the hardware address of a node with a certain IP address
- ARP table is a list of IP addresses and the MAC addresses associated with them

### Subnetting
- The Process of taking a large network and splitting it up into many individual and smaller subnetwors or subnets
- incorrect subnetting setups are a common problem you might run into as an IT support specialist, so its important to have a strong understanding of how this works

### Subnet masks
A single 8 bit numver can represent 256 different numbers 0-255
each part of an IP address is an octet meaning it consists of eight bits, for IP adress:
`9.100.100.100`
we can see the bits represented in the binary representation of these numbers
`0001001.01100100.01100100`
subnet mask in binary
`11111111.11111111.11111111.00000000`
the begining of the subnet mask, the mask itself, tells us what we can ignore while computing a host ID the parts with the 0s tells us what to keep

a common mask used is the 
`255.255.255.0`
 

- some bits that would normally comprise of the host ID are actually used for the subnet ID
-  Subnet masks are 32 bit numbers that are normally written out as four octets in decimal

### Basic Binary Math
- base 2 is another work for binary
- 8 bit number is 2 ** 8 or 256 which means and eight bit number can represent 256 decimal numbers
- a subnet mask is a way for a computer to use and operators to determine if an IP address exists on the same network

### CIDR
- Classless inter-domain routing 
- Demarcation point is used to describe where on network or system ends and another one begins  


### Routing
- A router is a network device that forwards traffic depending on the destination address of that traffic
- a router recieves a data packet on one of its interfaces, it then examines the destination IP, then looks up the destination network in a routing table, the router then forwards that out to the destination

### Routing Tables
- columns:
    1. destination network
    2. Next Hop
    3. Total Hops 
    4. Interface

### Interior gateway protocol
Routing protocols fall into two main categories: interior gateway protocols and exterior gateway protocols
- Interior gateway protocols are further split into two catagories: Link state routing protocols and distance-vector protocols
- Interior gateway protocols are used by routers to shar information within a single autonomour system
- An autonomous system is a collection of networks that all fall under the control of a single network operator
- The two main types of interior gateway protocols are link state routing protocols and distance-vector protocols

### Exterior gateway protocols
communicate data to routers representing the edges of an autonomous system
- Internet Assigned Numbers Authority (IANA) is a nonprofit organization that helps manage things like IP address allocation
- Along with managing IP address allocation the IANA is also responsible for ASN or Autonomous System Number allocation

### Non-Routable Address space
They are ranges of IPs set aside for use by anyone that cannot be routed to
- Core routers cannot access them
- They can be used by anyone internally

## Introduction to the Transport and application Layers

### The Transport Layer
- multiplexing and demultiplexing is handled by the transport layer through ports
- a port is a 16 bit number thats used to direct traffic to specific services running on a networked computer
- 10.10.10:80 is a socket address / socket number. the :80 denotes that we are 'addressing' port 80 on this socket
- Ethernet
    - IP datagram
        - TCP segment
            * Source port - Destination field
            * sequence number is a 32 bit number thats used to keep track of where in a sequence of TCP segments this one is expected to be (1)
            * acknowlegement number is the number of the next expected segment (2)
            * Data offset field is a 4-bit number that communicates how long the TCP header for this segment is
            * 6 bits reserved for the Control flags
            * The TCP window specifies the range of sequence numbers that might be sent before an acknowledgement is required
            * TCP checksum Operates just like the checksum fields at the IP and ethernet level - calculates lost or corrupted data
            * Urgent Pointer Field used in conjunction with the one of the TCP control flags to point out particular segments that might be more important than others
            * Options is sometimes used for more complicated flow control protocols
            * Padding just added 0's to ensure that the data payload section begins at the expected location

### TCP Control Flags and the Three-way Handshake
- Control Flags
    * URG short for URGENT a value of 1 here indicates that the segment is considered urgent and that the urgent pointer field has more data about this
    * ACK (acknowledged) A value of one in this field means that the acknowledgement number field should be examined
    * PSH (push) The transmitting device wants the recieveing device to push currently-buffered data to the application on the receiving end as soon as possible
    * RST (reset) One of the sides in a TCP connection hasnt been able to properly recover from a series of missing or malformed segments
    * SYN (synchronize) used when first establishing TCP connection and makes sure the receiving end knows to exmine the sequence number field
    * FIN (finish) when this flag is set to 1 it means the transmitting computer doesnt have any more data to send and the connection can be closed

- Three way handshake
    - Computer 1 -> SYN -> Compupter 2
    - Computer 1 <- SYN/ACK <- Compupter 2
    - Computer 1 -> ACK -> Compupter 2
    - now computers can start a TCP connection setting segments back and forth

- A handshake is a way for 2 devices to ensure that they are speaking the same protocol and will be able to understand each other

- Four way handshake (closing connection)
    - Computer 1 <- FIN <- Compupter 2
    - Computer 1 -> ACK -> Compupter 2
    - Computer 1 -> FIN -> Compupter 2
    - Computer 1 <- ACK <- Compupter 2


### Socket States
- Socket is the instantiation of an end-point in a potential TCP connection
- Instantiation is the actual implementation of something defined elsewhere
- LISTEN: A TCP socket is ready and listening for incoming connections (serverside only)
- SYN_SENT: A synchronization request has been sent but the connection hasnt been established yet (client side only)
- SYN_RECIEVED: A socket previously in a LISTEN state has recieved a synchronization request and sent a SYN/ACK back (server side only)
- ESTABLISHED: The TCP Connection is in working order and both sides are free to send each other data
- FIN_WAIT: A FIN has been sent but the corresponding ACK from the other end hasnt been received yet
- CLOSE_WAIT: The connection has been closed at the TCP layer, but that the application that opened the socket hasnt released its hold on the socket yet
- CLOSED: THe connection has been fully terminated and that no further communication is possible

### Connection-Oriented and Connectionless protocols
- Establishes a connection and uses this to ensure that all data has been properly transmitted
- A good example of UDP is streaming video


### Firewalls
- A device that blocks traffic that meets certain criteria


### The application layer
- For web traffic the application layer protocol is known as HTTP


## OSI Model
- seven layers 
    * Application
    * Presentation
    * Session
    * Transport
    * Network
    * Data link
    * Physical

## Indroduction to Network Services
### Name Resolution

- DNS Domain Name System:
    * A global and highly distributed network service that resolves strings of letters into IP addresses for you
    * converting a name into a ip address is known as name resolution ie www.website.com -> DNS -> 123.645.432.65

- There are five primary types of DNS servers:
    1. Caching name servers
    2. Recursive name servers
    3. Root name servers
    4. TLD name servers
    5. Authoritative name servers 

- Caching and recursive name servers purpose is to store known domain name lookups for a certain amount of time

- Recursive Name servers perform Full DNS resolution requests

- TTL Time to live
    * A value in seconds that can be configured by the owner of a domain name for how long a name server is allowed to cache an entry before it should discard it and perform a full resolution look up again.

- Anycast
    * A technique that is used to route traffic to different destinations depending on factors like location, congestion, or link health

- TLD = Top level domain the ".com" portion of a domain name


- DNS is an application layer that uses UDP for the transport layer instead of TCP
    * This is becuase UDP is `connectionless` , that is to say no connection needs to be made to send the datagrams. Overall less traffic will occur with these look ups even  so this can still generate a lot of traffic

    * Computer -> UDP -> Caching/recursive name server 
    * Caching/recursive name server -> UDP -> 13 rootservers
    * Caching/recursive name server <- UDP <- 13 rootservers
    * Caching/recursive name server -> UDP -> TLD name servers
    * Caching/recursive name server <- UDP <- TLD name servers
    * Caching/recursive name server -> UDP -> Thousands of name servers
    * Caching/recursive name server <- UDP <- Thousands of name servers

    * total of 8 packets. No connections made to be opened and closed ie TCP = computer SYN/ACK -> Caching/recursive being sent back and forth with every other server in process multiplce handshakes would occur


- Resource and Record Types
    * Most common type of record is an `A Record` and it is used to point a certain domain name at a certain IPv4 IP address
    * a list of IPs are held [IP1, IP2, IP3, IP4], when queried for a DNS they will attempt to connect with IP1 if that fails they will move to IP2, if that succeds the list will change to [IP2, IP3, IP4, IP1]
    * another common record is the `quad A (AAAA)` record which points to an IPv6 address
    * `CNAME` record redirects traffic from one domain to another. Resolves to a different network microsoft.com == www.mircrosoft.com both will take you to www.microsoft.com
    * `SRV` record returns specifics of many different service types.
    * `txt` record type was written for humans to read arbitrary specifics of the network. But it is also used to communicate data to other computers/network services such as additional service configurations


- Anatomy of a Domain name 
    * www -> subdomain/hostname
    * google 
    * com -> TLD Top level domain name (.com .net .edu .de .cn etc)
    * www.something.com -> Fully Qualified Domain Name or (FQDN). When you combine all of these parts together


- DNS Zones
    * Hierchical concept
    * Responsible for the zone specific to its TLD
    * Allow for easier control over multiple levels of a domain

- Zone Files are Simple configuration files that declare all resource records for a particular Zone

- Start of Authority (SOA) Delcares the zone, and the name of the name server that is authoritative for it

- NS records indicate other name servers that might also be responsible for this zone

- Reverse Look up zone Files: These let DNS resolvers ask for an IP and get the FQDN associated with it returned

- PTR Poinrter resource record Resolves an IP to a name

## Overview of DHCP
* IP address
* Subnet mask
* Gateway
* Name server

- DHCP Dynamic Host Configuration Protocol is an Application Layer protocol that automates the configuration process of hosts on a network

- DHCP can configure a range of IP addresses thats set aside for client devices. This ensures that any of these devices can obtain an IP address when they need one but also solves the problem of having to maintain a list of every node on the network and its corresponding IP

- Automatic Allocation is when a range of IP Addresses is set aside for assignment purposes

- Fixed Allocation Requires a manually specified list of MAC addresses and their corresponding IP addresses

- NTP servers, Network Time Protocol, used to keep all compiters on a network synchronized in time

- DHCP discovery
    * The process by which a client configured to use DHCP attempts to get network configuration information
