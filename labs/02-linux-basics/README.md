# Lab 02 – Linux Fundamentals

## Objective

Develop practical Linux administration and troubleshooting skills within the Ubuntu Server virtual machine established in Lab 01.

This lab focuses on navigating the Linux environment, identifying system and network information, understanding file permissions, working with shell commands, and using basic Bash automation.

---

## Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu 26.04 LTS (Resolute Raccoon) |
| Hostname | Ubuntu |
| User | abdul |
| Home Directory | `/home/abdul` |
| Shell | Bash |
| Virtualization | Oracle VirtualBox |

---

## System Identification

The Linux environment was examined using standard command-line utilities.

### Current User

```bash
whoami
```

Output:

```text
abdul
```

The `whoami` command identifies the user associated with the current shell session.

### Hostname

```bash
hostname
```

Output:

```text
Ubuntu
```

The `hostname` command identifies the system's configured hostname.

### Current Working Directory

```bash
pwd
```

Output:

```text
/home/abdul
```

The `pwd` command displays the current working directory.

---

## Network Identification

The Ubuntu server uses two network interfaces to support the home lab configuration.

```bash
ip addr
```

The Host-only interface was assigned:

```text
192.168.56.102
```

The NAT interface was assigned:

```text
10.0.2.15
```

The routing table was examined using:

```bash
ip route
```

The default route is:

```text
default via 10.0.2.2 dev enp0s3
```

The Host-only network is:

```text
192.168.56.0/24 dev enp0s8
```

This configuration allows the Ubuntu server to access external networks through the NAT interface while using the Host-only interface for communication within the isolated lab network.

---

## File and Directory Inspection

The contents of the user's home directory were examined using:

```bash
ls -la
```

This command displays files and directories, including hidden files, together with ownership and permission information.

The directory contained an `.ssh` directory as well as Bash scripts created during the lab:

```text
.ssh/
CyberLab/
network_report.sh
system_report.sh
test.txt
```

The `.ssh` directory is particularly relevant to secure remote administration because SSH configuration and authentication-related files are commonly stored within it.

---

## File Permissions

File and directory permissions were examined using:

```bash
ls -ld CyberLab network_report.sh system_report.sh test.txt .ssh
```

The output demonstrated Linux's ownership and permission model, including separate permissions for the file owner, group, and other users.

For example:

```text
drwx------ .ssh
-rwxrwxr-x network_report.sh
-rwxrwxr-x system_report.sh
-rw-rw-r-- test.txt
```

This provided practical experience interpreting Linux read (`r`), write (`w`), and execute (`x`) permissions.

---

## Bash Automation

Two Bash scripts were created to automate basic system information gathering:

- `network_report.sh`
- `system_report.sh`

The scripts were executed directly from the command line:

```bash
./network_report.sh
```

```bash
./system_report.sh
```

The network script collected information including:

- Hostname
- Current user
- IP addresses
- Routing information
- Listening network ports

The system script collected:

- Hostname
- Current user
- IP addresses
- Disk utilisation
- Memory utilisation

This demonstrated how Bash can be used to automate repetitive system administration and information-gathering tasks.

---

## Key Takeaways

This exercise provided practical experience with:

- Linux command-line navigation
- System identification
- Network configuration
- Routing
- File and directory permissions
- SSH-related directories
- Bash scripting
- Basic system information gathering