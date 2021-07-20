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