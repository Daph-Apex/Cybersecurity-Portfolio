# Cybersecurity Portfolio

## About Me

Hi, I'm **Abdul Fatawu Dawuda**, a Biomedical Engineer transitioning into Cybersecurity.

I am building practical experience across **Linux administration, networking, security monitoring, network reconnaissance, packet analysis, and security automation** through hands-on laboratory work.

This repository documents my progression through a self-built cybersecurity home lab, practical investigations, scripts, and technical documentation.

My current focus is developing the foundational skills required for **SOC Analyst and Cybersecurity Analyst** roles.

---

## Cybersecurity Home Lab

My laboratory environment is built using **Oracle VirtualBox** on a Windows 11 host.

### Environment

| Component | Configuration |
|---|---|
| Host OS | Windows 11 |
| Host Memory | 16 GB RAM |
| Virtualization | Oracle VirtualBox |
| Attacker / Analysis VM | Kali Linux |
| Target VM | Ubuntu 26.04 LTS |
| Network | NAT + Host-only |
| Host-only Network | `192.168.56.0/24` |

The Host-only network provides controlled communication between the virtual machines, while NAT provides separate Internet connectivity.

---

## Technical Skills Demonstrated

### Operating Systems

- Linux
- Windows
- Linux command-line administration
- Bash scripting

### Networking

- TCP/IP
- IPv4
- ICMP
- Network interfaces and routing
- SSH
- SCP
- Network reconnaissance
- TCP port scanning
- Service enumeration

### Security Tools

- Nmap
- Wireshark
- Oracle VirtualBox
- Git / GitHub

### Scripting

- Bash
- System and network information gathering
- Command-line automation

---

## Hands-on Labs

| Lab | Topic | Status |
|---|---|---|
| 01 | Home Lab Setup | Completed |
| 02 | Linux Fundamentals | Completed |
| 03 | SSH & SCP | Completed |
| 04 | Network Scanning & Service Enumeration | Completed |
| 05 | Wireshark Packet Analysis | Completed |
| 06 | Vulnerability Assessment | Planned |
| 07 | Log Analysis | Planned |
| 08 | Python Security Automation | Planned |
| 09 | Incident Response | Planned |
| 10 | Threat Hunting | Planned |
| 11 | Active Directory | Planned |

---

## Key Practical Work

### Network Reconnaissance

Performed controlled Nmap reconnaissance against the Ubuntu server.

Activities included:

- Verified host reachability
- Discovered TCP/22 and TCP/80
- Performed service and version detection
- Identified OpenSSH and Apache
- Validated the HTTP service using `curl`

Evidence is available in:

```text
labs/04-network-scanning/
```

### Packet Analysis

Captured and analysed ICMP traffic between Kali Linux and Ubuntu using Wireshark.

Activities included:

- Captured live network traffic
- Filtered ICMP packets
- Analysed Ethernet II
- Analysed IPv4
- Analysed ICMP
- Identified MAC addresses
- Identified source and destination IP addresses
- Examined ICMP Echo Requests and Echo Replies
- Analysed ICMP Type, Code, and Sequence fields

Evidence is available in:

```text
labs/05-wireshark/
```

### Linux Administration and Automation

Built Bash scripts for collecting system and network information:

```text
scripts/
├── network_report.sh
└── system_report.sh
```

The scripts demonstrate practical use of Linux commands for:

- System information gathering
- Network configuration
- Routing information
- Listening services
- Disk usage
- Memory usage

---

## Repository Structure

```text
Cybersecurity-Portfolio/
|
├── assets/
│   ├── diagrams/
│   ├── images/
│   └── screenshots/
|
├── certificates/
├── docs/
|
├── labs/
│   ├── 01-home-lab/
│   ├── 02-linux-basics/
│   ├── 03-ssh-and-scp/
│   ├── 04-network-scanning/
│   │   └── screenshots/
│   └── 05-wireshark/
│       └── screenshots/
|
├── reports/
|
├── scripts/
│   ├── network_report.sh
│   └── system_report.sh
|
├── .gitignore
├── LICENSE
└── README.md
```

---

## Current Learning Focus

I am continuing to develop practical skills in:

- Security Operations (SOC)
- Linux administration
- Network security
- Security monitoring
- Log analysis
- Vulnerability assessment
- Incident response
- Threat hunting
- Python security automation
- SIEM technologies

---

## Certifications and Training

- Google Cybersecurity Professional Certificate
- Additional cybersecurity and technical training documented in the `certificates/` directory

---

## Career Objective

To transition into an entry-level **SOC Analyst or Cybersecurity Analyst** role and apply my engineering background, analytical skills, and growing hands-on cybersecurity experience to security monitoring, investigation, incident response, and defensive security operations.

---

## Disclaimer

All security testing documented in this repository is performed against systems that I own or have explicitly configured for educational purposes within my isolated home laboratory.

The techniques and tools are used for learning, defensive security, and authorized testing.