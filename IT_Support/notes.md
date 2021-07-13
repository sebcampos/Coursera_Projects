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


