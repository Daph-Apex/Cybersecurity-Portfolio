# Lab 01 – Building a Cybersecurity Home Lab

## Objective

Build a secure virtual lab for learning Linux administration, networking, remote access, packet analysis, and cybersecurity tools.

---

## Lab Environment

### Host Machine

| Component | Details |
|----------|---------|
| Operating System | Windows 11 |
| Memory | 16 GB RAM |
| Processor | AMD Processor |

### Virtualization Platform

- Oracle VirtualBox

### Virtual Machines

| Machine | Purpose |
|---------|---------|
| Kali Linux | Attacker / Administration workstation |
| Ubuntu Server 26.04 LTS | Target Linux server |

---

## Network Configuration

Each virtual machine was configured with:

- **NAT Adapter** to provide internet connectivity for software updates and package installation.
- **Host-only Adapter** to enable isolated communication between the virtual machines without exposing the lab directly to the external network.

This configuration created a controlled environment suitable for practicing networking and cybersecurity tasks.

---

## Tasks Completed

- Installed Oracle VirtualBox
- Installed Kali Linux
- Installed Ubuntu Server
- Configured virtual networking
- Verified network connectivity
- Connected from Kali to Ubuntu using SSH
- Successfully transferred files using SCP

## Configuring VirtualBox

The virtual environment consists of two virtual machines connected using NAT and Host-only networking.

![VirtualBox](screenshots/01-virtualbox-overview.png)

---

## Verifying Connectivity

Network connectivity between Kali Linux and Ubuntu Server was verified using the `ping` command.

Successful ICMP echo replies confirmed that the two virtual machines could communicate over the Host-only network before configuring SSH.

![Ping](screenshots/07-successful-ping.png)

---

## Remote Access

SSH was enabled on the Ubuntu Server, allowing secure remote administration from the Kali Linux virtual machine.

After verifying connectivity, an SSH session was established successfully and later used for secure file transfers with SCP.

![SSH](screenshots/08-ssh-login.png)

---

## Commands Used

| Command | Purpose |
|---------|---------|
| `ip addr` | Display network interface information |
| `ping` | Verify network connectivity |
| `ssh` | Establish a secure remote connection |
| `scp` | Transfer files securely between virtual machines |

---

## Tools Used

- Oracle VirtualBox
- Kali Linux
- Ubuntu Server
- SSH
- SCP
- Linux Terminal

---

## Skills Demonstrated

- Virtualization
- Linux Administration
- Network Configuration
- Remote Access
- Secure File Transfer
- Basic Troubleshooting

---

## Lessons Learned

Building a home lab provides a safe environment for learning and testing cybersecurity concepts. During this lab, I gained practical experience configuring virtual machines, establishing secure remote connections with SSH, and transferring files using SCP. This environment will serve as the foundation for future networking, security monitoring, and penetration testing labs.