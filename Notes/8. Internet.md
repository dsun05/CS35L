# Comprehensive Notes on Internet Technologies & Protocols Leading to the Web

---

## Table of Contents

1. Introduction to Web Technology Evolution  
2. Fundamental Concepts of Networking  
   2.1 Circuit Switching vs. Packet Switching  
   2.2 Definition and Structure of Packets  
3. Protocols and Packet Switching Challenges  
   3.1 What Is a Protocol?  
   3.2 Challenges in Packet Switching  
   3.3 The Role of Protocols in Mitigating Issues  
4. Layered Network Architecture  
   4.1 Overview of Networking Layers  
   4.2 The Link Layer  
   4.3 The Internet Layer  
   4.4 The Transport Layer  
   4.5 The Application Layer  
5. Internet Protocol (IP)  
   5.1 IPv4 Overview  
   5.2 Fields in IPv4 Header  
   5.3 Addressing Schemes (IPv4 vs IPv6)  
   5.4 Checksums and Reliability  
6. Transport Layer Protocols  
   6.1 UDP – User Datagram Protocol  
   6.2 TCP – Transmission Control Protocol  
7. Protocol Specification – How to Create a Protocol  
8. The Web Fundamentals  
   8.1 Introduction and Web History  
   8.2 HTTP – Hypertext Transfer Protocol  
     - HTTP Basics and Example  
     - HTTP Headers  
     - Persistent Connections in HTTP 1.1  
     - HTTPS and Security  
   8.3 HTTP/2 – Performance Improvements  
   8.4 HTTP/3 and Real-Time Applications  
9. HTML – HyperText Markup Language  
10. Additional Questions and Examples

---

## 1. Introduction to Web Technology Evolution

- Focus: Understanding internet protocols culminating in web technologies.
- Context: Leads into practical usage in homework/project assignments, especially involving web services.
- Historical lens: Tracks early packet switching concepts all the way to dynamic web applications.

---

## 2. Fundamental Concepts of Networking

### 2.1 Circuit Switching vs. Packet Switching

- Circuit Switching: Dedicated path between endpoints (e.g., traditional telephony)
- Packet Switching: Data split into packets, independently routed through network

| Feature             | Circuit Switching       | Packet Switching         |
|---------------------|-------------------------|--------------------------|
| Path setup          | Required                | Not required             |
| Reliability         | More predictable        | Less predictable         |
| Efficiency          | Low (fixed path)        | High (dynamic routing)   |

### 2.2 Definition and Structure of Packets

- Packet: Data unit typically 1–2 KiB in size.
- Structure:  
  - Header: Control info (e.g., destination, protocol type); for routers
  - Payload: Application data; for recipient applications

Example Packet Composition:
| Field    | Purpose                                |
|----------|----------------------------------------|
| Header   | Routing, protocol type, TO/FROM        |
| Payload  | Email text, file content, etc.         |

---

## 3. Protocols and Packet Switching Challenges

### 3.1 What Is a Protocol?

- Protocol: Agreed rules for message transmission and processing
- Analogy: Diplomatic protocols required to speak to foreign leaders

Types of Protocol Behaviors:
- Message formats (e.g., header structures)
- Response behavior (e.g., what to do on success/failure)

### 3.2 Challenges in Packet Switching

| Issue             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Lost Packets     | Packets fail to reach destination, often due to buffer overflow in routers |
| Out-of-Order     | Packets received in different order than sent                               |
| Duplicated Packets | Same packet may be delivered more than once due to routing errors          |
| Corrupted Packets | Packet content changes due to hardware errors or misconfigurations         |

### 3.3 The Role of Protocols in Mitigating Issues

- Avoid solving at application level: Too inefficient, unscalable
- Solution: Define proper protocols (standardized)
- Must support interoperability (C++, Java, Python apps can work together)
- Use layered architecture to manage concerns

---

## 4. Layered Network Architecture

### 4.1 Overview

Four (Dr. Eggert’s view) abstraction layers:
1. Link Layer – Physical connection between two nearby nodes
2. Internet Layer – End-to-end routing and addressing (via IP)
3. Transport Layer – Data stream abstraction and reliability
4. Application Layer – Application-specific communication

Other models (e.g., OSI) define 7 layers (application, presentation, session, transport, network, data link, physical)

### 4.2 The Link Layer

- Hardware-specific protocols (e.g., Ethernet, Wi-Fi)
- Handles communication over a single, direct link

Example Link Layer Technologies:
| Technology  | Description                |
|-------------|----------------------------|
| Ethernet    | Wired LAN standard         |
| Wi-Fi       | Wireless communication     |
| USB         | Peripheral connections     |

### 4.3 The Internet Layer

- Primary protocol: IP (IPv4 or IPv6)
- Responsible for global addressing and packet routing via IP Addresses
- Stateless, best-effort delivery
- Introduces problems like loss, reordering, duplication

### 4.4 The Transport Layer

- Manages reliable delivery over unreliable internet layer
- Introduces concept of:
  - Data channels (logical streams)
  - Reliability
  - Ordering
  - Error Correction
- Protocols: TCP and UDP

### 4.5 The Application Layer

- Protocols meant for specific services (e.g., HTTP, FTP, SMTP)
- Builds on lower layers but focuses on the user’s domain concerns

---

## 5. Internet Protocol (IP)

### 5.1 IPv4 Overview

- Released: 1983  
- Inventor: Team including John Postel  
- Connectionless, packet-switching-oriented

### 5.2 Fields in IPv4 Header

| Field           | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Length          | Packet size in bytes                                                        |
| Protocol Number | Defines encapsulated protocol (e.g., TCP = 6; UDP = 17)                     |
| IP Addresses    | Source and destination (32-bit each)                                        |
| TTL             | Time-to-live to prevent infinite loops, decremented at each router hop      |
| Checksum        | Simple 16-bit checksum for packet corruption detection                      |

Notation: IP address written as dotted decimal e.g., 192.168.1.1 (4 x 8-bit)

### 5.3 Addressing Schemes – IPv4 vs IPv6

| Version | Address Size | Release Year | Supports |
|---------|--------------|--------------|----------|
| IPv4    | 32-bit       | 1983         | ~4.3B addresses |
| IPv6    | 128-bit      | 1998         | 2^128 addresses (future-proofing) |

Adoption status:
- IPv4 still widely used (60%)
- IPv6 rising (40%) due to address exhaustion

### 5.4 Checksums and Reliability

- Internet checksum (16-bits) for error detection
- Cannot stop malicious actors, not cryptographic
- Used to catch accidental data corruption
- End-to-End Principle: Each layer should do its error checking

---

## 6. Transport Layer Protocols

### 6.1 User Datagram Protocol (UDP)

- Barebones protocol
- Source Port & Destination Port
- No guarantees: Sender must handle ordering, errors, etc.
- Used in:
  - Streaming, DNS, real-time telemetry
  - Situations where speed > reliability

Use Case Example: IoT device sending temperature once every 10 minutes

### 6.2 Transmission Control Protocol (TCP)

- Reliable, connection-oriented
- Implements:
  - Flow control
  - Retransmission
  - Packet reassembly
- Guarantees:
  - In-order, lossless, error-checked delivery

Reliability Features Table:
| Challenge         | TCP Feature That Solves It |
|------------------|-----------------------------|
| Loss             | Retransmission              |
| Out-of-Order     | Reassembly                  |
| Duplication      | Sequence numbers, ACK       |
| Errors           | Checksums                   |

Common use cases:
- Submitting assignments
- Large data transfers
- Web traffic with HTTP(S)

---

## 7. Protocol Specification – How to Create a Protocol

- Define:
  - Packet formats and headers
  - Expected behaviors
- Documentation (spec), not code
- Analogy: Like C++ standard (C++23, C++26)
- Failing to follow spec = non-functional applications

Example:
- What headers are required?
- What order are fields?
- What responses to invalid requests?

---

## 8. The Web Fundamentals

### 8.1 Introduction and Web History

- Invented by Tim Berners-Lee (CERN, early 1990s)
- First web server hosted on his workstation (CERN)
- Protocol: HTTP, Markup: HTML

### 8.2 HTTP – Hypertext Transfer Protocol

#### HTTP Basics

- Built on top of TCP
- Request-response model (initially one request per TCP connection)
- HTTP Request Example:
```http
GET / HTTP/1.0
[Empty line]
```

#### HTTP Header Fields (Example)

| Field           | Purpose                                            |
|----------------|----------------------------------------------------|
| Date           | Timestamp of response                              |
| Server         | Web server software (e.g., Apache)                 |
| Last-Modified  | When resource last changed                         |
| E-Tag          | Resource identifier/version                        |
| Content-Length | Byte count of body                                 |
| Content-Type   | Media type (e.g., text/html, image/jpeg)           |
| Connection     | Whether connection should be closed after response |

#### Persistent Connections in HTTP 1.1

- Enables multiple requests per TCP connection
- Connection: Keep-alive
- Improves network efficiency
- Requires Host header (for virtual hosting)

#### HTTPS and Security

- Used today predominantly
- Encrypts HTTP using TLS
- Prevents:
  - Packet inspection (privacy)
  - Packet tampering (integrity)
- Tools: GnuTLS CLI, OpenSSL

### 8.3 HTTP/2 – Performance Improvements

- Launched 2015
- 59% adoption
- Goals: Efficiency, speed, parallelism

| Feature         | Description                                           |
|------------------|-------------------------------------------------------|
| Header Compression | Reduces redundant header data                      |
| Server Push       | Server can send unsolicited resources               |
| Pipelining        | Multiple requests before responses                  |
| Multiplexing      | Async request/response over single connection       |

Example Multiplex Order:

| Request | Response |
|---------|----------|
| A       | B        |
| B       | D        |
| C       | A        |

### 8.4 HTTP/3 and Real-Time Applications

- Uses QUIC over UDP (Not TCP)
- Developed by Google, 2022
- 32% adoption
- Advantage: Designed for real-time (Zoom, games)

Avoids:
- "Head-of-line" blocking issues in TCP
- Enables partial packet loss (good for video)

Characteristics of QUIC:
| Feature             | Benefit                    |
|---------------------|----------------------------|
| Built on UDP        | Lower latency              |
| Multiplexed streams | Reduced stream interference |
| Reliable and Unreliable modes | Optimized for application need     |

---

## 9. HTML – HyperText Markup Language

- Based on SGML (Standard Generalized Markup Language)
- HTML: Simplified + includes "hypertext" (links, interactivity)
- Uses angle-bracket tags:
```html
<p>This is a paragraph</p>
```
- Lowercase convention (vs SGML's uppercase)

Elements:
- Tags: \<p>, \<a href>, \<h1>, \<img src>, etc.
- DOM structure: Tree of nested elements

HTML Example:
```html
<html>
  <head><title>My Web Page</title></head>
  <body>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

---

## 10. Additional Questions and Examples

1. Why is pipelining/multiplexing useful?
   - Reduces latency (particularly with async data)
   - Lets humans interact without waiting

2. Why can TCP be inefficient for video?
   - Retransmitted packets introduce delay/stutter. QUIC solves this.

3. Why don't all use IPv6?
   - Legacy hardware, software
   - Institutional inertia (IPv4 still works)

4. What is head-of-line blocking?
   - If one lost packet blocks all subsequent ones from being processed

---

# Summary

This lecture covers the evolution of networking, focusing on how packet-switching and layered protocols culminate in modern web technologies. From basic packet delivery mechanisms and IP addressing through reliable transport via TCP to application-specific protocols like HTTP, each layer introduces abstraction and problem-solving to enable internet-scale communication. With the rise of real-time applications, newer technologies (HTTP/3, QUIC, HTML5) continue to push the boundaries of what the web can do efficiently and securely.