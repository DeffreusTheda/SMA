
# 2023-07-26
- Organize your files
- Computer Organization
	- Schematic:
		- CPU (Central Processing Unit)
		- ALU (Arithmetic Logic Unit)
			- Part of the CPU that does all the arithmetic (+/-) and logical (AND/OR) calculations.
		- MAR (Memory Address Register) ->AddressBus-> RAM (Random Access Memory) ->DataBus->
		- MDR (Memory Data Register) <-DataBus<- Cache <-DataBus<- RAM
		- CU (Control Unit)
			- Used to decode
		- Other Registers
			- ACC
			- CIR (Current Instruction Register)
			- PC (Program Counter)
	- CPU (Von Neumann model)
- Input (Data) -> Process <->/-> Storage/Output (Information)
- IOT: Internet of Things

# 2023-07-28
- FDE cycle / Machine Instruction Cycle:
	- PC > MAR > RAM > MDR > CIR/CU > ALU > Output
	- Fetch 1)-3)
	- Decode 4
	- Execute 6
	- ###### 2023-08-25
		- Store

# 2023-08-02
- Cache
	- Stores frequently used instructions from RAM
	- Processor checks cache first
	- L1 (Fastest) and L2 Cache
	- In between Primary memory and Processor (CPU)
	- ###### (2023-08-25)
		A type of small, high-speed memory inside the CPU used to hold frequently used data
- Secondary memory

- [x] Explain the purpose of cache memory and explain how cache memory affects system performances
- [x] State two reasons for having secondary memory as well as main (internal) memory

# 2023-08-04
- Lesson concluding questions in group
	- Explain the purpose of cache memory and explain how cache memory affect system performance!
		- To store instructions for quicker access performing frequently used instructions
		- Cache memory affect system performance because it is the first thing that the CPU (Central Processing Unit) check when performing an instructions, so that it'll be quicker to perform frequently done instructions, rather than going to RAM (Random Access Memory) which takes longer time to reach
		  This will improve system performance because the process to perform instructions became shorter, this is possible because the cache memory physical location is in between CPU and RAM, more precisely in the CPU itself
		  Although it can quicken the process of performing instructions, when the cache memory is full it'll instead make the process slower, usually because of multiple tasks
	- State two reasons for having secondary memory as well as main or internal memory!
		- Secondary memory and internal memory is permanent, so it can be used to save data for long-term needs
		- Secondary memory and internal memory is used to hold less used information or may be too large to fit as a whole in the primary memory
# 2023-08-09
- The very main purpose of storage is to store the operating system -- computer can turn on but can't operate
- Operating system:
	- 5 role:
		- User interface
		- Memory Management
		- Peripheral Management
		- Multitasking
		- Security
- Multitasking
	- Alfin; Tristan; Caecil; Sora; Auriel
	- ex. Benefit/Disadvantages; definition; explore it; current technology and development2

# 2023-08-11
- Process and steps of instruction:
	- PC (Program Counter): is an component, microprocessors inside the CPU --- It receives from inputs and send to processor
	- Address ("Soft file"): connected to other components by address bus; 
	- MAR (M Address R): component, sending to RAM; connected by date bus
###### 2023-08-25
			holds the memory address of the data to be used by the ALU, so that the ALU can fetch the corresponding content from the memory and process it accordingly.
	- MDR (M Data R):
	- LU (Logic Unit): send to output
	- Save to secondary storage: 
	- Binary digits is the very thing of everything in computer magic

- ROM (Read Only Memory); is an component, 
- RAM 
- After instruction cleared, it'll be a data, precisely file stored in folder/directory; Compress is making them into one
- Main word of multitasking 
- If RAM/ROM bigger then more instructions they're doing

# 2023-08-16
An application that is running on a computer system takes up resources. These resources include the amount of memory the application is occupying, or how much processor time it needs in order to function properly. An OS is responsible for the efficient allocation of resources so that an application can run as effectively as possible on a particular computer system.

Multiple applications may run on a computer system at any one time, appearing as though they are performing tasks simultaneously. Most computer systems however have a single CPU that can perform a single action at any particular time. That means that applications must share the CPU time in order to accomplish their goal. This is known as multitasking and it is a core OS service.

# 2023-08-23
- corrupted files is because there's something missing from the data
- when you send a files (for example images), it'll be fragmented (torn to pieces/bits) and send one by one to be decrypted in the destination and reformed again

# 2023-08-25
- IR (Instruction Register): something inside the Control Unit (CU) that

# 2023-09-01
- Binary, hexadecimal, and decimal
	- uses of mod to change decimal -> binary
	- decimal -> hexadecimal

# 2023-09-06
## Post-test Discussion
- why deleting cache doesn't necessarily improve performance / why full cache doesn't worsen performance
	- storage and ram is full - you just need to free up space here, not necessarily in cache
- 3a. spell checker
	- you're right!! yey!! completely concluded by yourself
- 3b. nothing to add,  I guess
# 2023-09-29
- Describe how data is transmitted by packet switching!
	- Data is broken down into data packets and be sent to the receiver, and these broken down data is reformed/restructured again on the side of the receiver.
	- Packet is a small unit of data that's used in a network, composed of a header, protocol & payload. The header contains the address of receiver and the address of sender, protocol define what kind of protocol is used to send and receive the packet, while the payload contains the datas that's in the form of binaries.
- Discuss the importance of protocols in ensuring the successful preparation, transmission, and delivery of data using packet switching!
	- Protocol is a set of rules (format & order of messages) to control how data is sent and received from entity to other entity(s) in a network.
	- Protocol is useful for achieving compatibility of communication and data transferring from a device to other device(s) in a network. Protocols ensure the data integrity, determine the order of the message (flow control), prevent [congestion] and [deadlock], and supply an agreed way of error checking.
		- Data integrity defined as how equal is the received data with the sent data; there might be some loss of data in the transferring process, which protocols prevent by ensuring the data integrity of a packet.
		- Flow control is the ways a server manage the flow of data traffic in a network, and is used to prevent fast connection user from overwhelming slow connection user.
# 2023-10-06
Roles of OS:
1. User Interface
2. Memory Management
3. Peripheral Management
4. Multitasking
5. Security
	- OS have protocols & feature to limit 
		- for example username & password, user permissions, permission to write/read on encrypted file

# 2023-11-08
Topics: 3. [[Network]]
