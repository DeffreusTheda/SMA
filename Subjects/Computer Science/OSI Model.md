---
tags: []
---
# Osi Model
Related: [[Network]]

Stand for Open System Interconnection.
For IB exams, know at least 3 out of the 7 layers; just need to know the name. ![[Screenshot 2023-11-21 at 21.55.55.png]]

Data is sent or received between the layer above or below a layer; The seven layers of OSI Model:
1. Physical (Please):
	Hardware.
	Receives and send converted [binary](Binary.md) data in the form of electrical pulses (wired) OR signals (wireless) that make up data transfer and transmit over a [network](Network).
2. Data link (Do):
	Focuses on the physical addressing of the transmission. 
	Adds physical (**[MAC](Media%20Access%20Control.md)**) address (linked with the computer's [[network interface card]] of the receiving endpoint to the packet from the [network layer](OSI Model#^050611) (that includes the IP address for the remote computer).
	Present the data in a format suitable for transmission.
	Checks if the received information is corrupted during transmission. ^91d623
3. Network (Not):
	Locate the **destination** of your request. 
	Referred to as Logical addressing—still software controlled—, used to provide order to networks, categorizing them and allowing proper sorting.
	Currently the most common form of logical addressing is the IPV4 format. ^050611
4. Transport (Throw):
	Serves numerous important functions.  ^1676bf
	- Choose the **[protocol](Obsidian/SMAPDA/Subject/ComSci/Internet%20Protocol.md)** for data transmission. 
	   Commonly use:
	   1. [TCP (Transmission Control Protocol)](Transmission%20Control%20Protocol.md).
	   2. [UDP (User Datagram Protocol)](User%20Datagram%20Protocol.md).
	- Divides the transmission up into byte-sized pieces (TCP call these segments; UDP call it datagrams), making successful message transmission easy.
5. Session (Sausage):
    Look for the possibility of setting up a connection with the other computer across the [network](Network). 
    If not then sends back an error and the process goes no further. 
    Session layer maintain established connection and co-operate with the session layer of the remote computer to synchronize communications, passing data to the transport layer.
    Allows multiple requests to different endpoints simultaneously without all the data getting mixed up.
6. Presentation (Pizza):
    Translates the data into a **standardized** format, handling any encryption/compression/other transformations to the data.
7. Application (Away):
	Provides networking options to programs running on a computer. 
	Works almost exclusively with applications, providing an interface for them to use in order to transmit data. 
	Accepts communication requests from applications.
	Example of the use of application layer is: 
		[FTP](File%20Transfer%20Protocol.md) protocol communicate with the application layer.