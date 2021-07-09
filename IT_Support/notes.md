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
Hubs are slower and more antiquated
Switches will inspect data and decide where to send it (which application, domain, etc) so that there are no collisions

