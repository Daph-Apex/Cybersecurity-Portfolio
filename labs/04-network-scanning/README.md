# Lab 04 – Network Scanning and Service Enumeration

## Objective

Perform controlled network reconnaissance against the Ubuntu Server within the cybersecurity home lab.

The objectives were to:

- Verify network connectivity
- Identify an active host
- Discover open TCP ports
- Identify running services and versions
- Validate an exposed HTTP service

All scanning was performed against my own isolated virtual lab environment.

---

## Lab Environment

| System | Role | Host-only IP |
|---|---|---|
| Kali Linux | Scanning workstation | `192.168.56.103` |
| Ubuntu 26.04 LTS | Target server | `192.168.56.102` |

Network:

```text
192.168.56.0/24
```

The systems communicate through the Host-only network configured in the previous labs.

---

## 1. Verify Network Connectivity

Before scanning the target, connectivity was verified from Kali using ICMP:

```bash
ping -c 4 192.168.56.102
```

Result:

```text
4 packets transmitted, 4 received, 0% packet loss
```

The average round-trip time was:

```text
1.646 ms
```

This confirmed that the target was reachable over the Host-only network.

---

## 2. Basic Nmap Scan

A basic Nmap scan was performed against the Ubuntu server:

```bash
nmap 192.168.56.102
```

### Results

```text
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

Nmap reported:

```text
Host is up (0.012s latency).
Not shown: 998 closed tcp ports
```

The scan identified two open TCP services:

- TCP/22 – SSH
- TCP/80 – HTTP

The target's MAC address was also identified as an Oracle VirtualBox virtual NIC.

---

## 3. Service and Version Detection

Nmap service detection was performed using:

```bash
nmap -sV 192.168.56.102
```

### Results

| Port | Service | Detected Version |
|---|---|---|
| `22/tcp` | SSH | OpenSSH 10.2p1 Ubuntu 2ubuntu3.5 |
| `80/tcp` | HTTP | Apache httpd 2.4.66 |

Nmap identified the operating system family as Linux.

### Security Relevance

Service/version detection provides useful reconnaissance information for defenders and security analysts.

Knowing which services are exposed helps establish an asset's attack surface and provides information that can later be compared against approved software inventories and vulnerability databases.

A detected version should **not automatically be considered vulnerable**. Additional vulnerability assessment is required to determine whether a specific version is affected by a known vulnerability.

---

## 4. HTTP Service Validation

The HTTP service identified by Nmap was tested using:

```bash
curl -I http://192.168.56.102
```

The server returned:

```text
HTTP/1.1 200 OK
Server: Apache/2.4.66 (Ubuntu)
Content-Type: text/html
```

The `200 OK` response confirmed that the HTTP service was actively responding to requests.

---

## Reconnaissance Workflow

The investigation followed this sequence:

```text
Network connectivity
        ↓
Host discovery
        ↓
Port scanning
        ↓
Service/version detection
        ↓
HTTP service validation
```

This demonstrates a basic reconnaissance workflow using multiple tools and techniques.

---

## Security Observations

### SSH – TCP/22

SSH provides remote administration and is an important service to monitor.

Security considerations include:

- Strong authentication
- Restricting access to trusted networks
- Monitoring authentication attempts
- Keeping OpenSSH patched
- Avoiding unnecessary exposure

### HTTP – TCP/80

An HTTP service was exposed on the target.

Security considerations include:

- Understanding whether HTTP is required
- Reviewing the web server configuration
- Keeping Apache patched
- Monitoring web server logs
- Considering HTTPS where appropriate

These observations do not indicate that the services are vulnerable; they identify areas requiring further assessment.

---

## Tools Used

- Kali Linux
- Nmap 7.98
- `ping`
- `curl`
- Ubuntu Server
- Apache HTTP Server

---

## Commands Used

| Command | Purpose |
|---|---|
| `ping -c 4` | Verify network connectivity |
| `nmap <IP>` | Discover open TCP ports |
| `nmap -sV <IP>` | Identify services and versions |
| `curl -I <URL>` | Inspect HTTP response headers |

---

## Skills Demonstrated

- Network reconnaissance
- TCP port scanning
- Service enumeration
- Basic HTTP analysis
- Linux networking
- Nmap
- Command-line investigation
- Security-focused interpretation of scan results

---

## Lessons Learned

This lab demonstrated how a security analyst can progress from basic network connectivity testing to identifying exposed services and validating their responses.

The exercise also demonstrated the importance of interpreting scan results carefully. Discovering an open service or software version is an observation, not proof of a vulnerability. Further analysis is required before making security conclusions.

---

## Next Steps

Future exercises will examine the identified services in greater detail and introduce packet-level analysis using Wireshark.