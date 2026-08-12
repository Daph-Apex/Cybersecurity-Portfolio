# Lab 03 – SSH and SCP

## Objective

Configure and test secure remote administration and file transfer between Kali Linux and Ubuntu Server within the isolated cybersecurity home lab.

The lab demonstrates:

- SSH service verification
- Remote authentication
- Secure remote shell access
- SCP file transfer
- Verification of transferred files

---

## Lab Environment

| System | Role | Host-only IP |
|---|---|---|
| Kali Linux | Administration workstation | `192.168.56.103` |
| Ubuntu 26.04 LTS | Remote server | `192.168.56.102` |

The systems communicate through the Host-only network configured in Lab 01.

---

## 1. Verify SSH Service

The SSH service was checked on the Ubuntu server using:

```bash
sudo systemctl status ssh
```

The service reported:

```text
Active: active (running)
```

The SSH daemon was also confirmed to be listening on TCP port 22:

```text
Server listening on 0.0.0.0 port 22.
Server listening on :: port 22.
```

This confirmed that the Ubuntu server was ready to accept SSH connections.

---

## 2. Establish an SSH Connection

From Kali Linux, an SSH connection was initiated using:

```bash
ssh abdul@192.168.56.102
```

Authentication was successful and a remote shell was established:

```text
abdul@Ubuntu:~$
```

The Ubuntu login banner also recorded the source address:

```text
Last login: ... from 192.168.56.103
```

This confirmed that the SSH connection originated from the Kali Linux Host-only interface.

---

## 3. Secure File Transfer Using SCP

A test file was created on Kali Linux:

```bash
echo "SCP test from Kali" > scp-test.txt
```

The file was transferred to the Ubuntu user's home directory using:

```bash
scp scp-test.txt abdul@192.168.56.102:/home/abdul/
```

Authentication was completed using the Ubuntu user's credentials.

---

## 4. Verify the File Transfer

After reconnecting to Ubuntu through SSH, the transferred file was verified:

```bash
ls -l scp-test.txt
```

Output:

```text
-rw-rw-r-- 1 abdul abdul 19 ... scp-test.txt
```

The contents were then checked:

```bash
cat scp-test.txt
```

Output:

```text
SCP test from Kali
```

The successful file listing and matching contents confirmed that the SCP transfer was completed successfully.

---

## Security Concepts Demonstrated

### SSH

SSH provides encrypted remote administration between systems. In this lab it was used to securely access the Ubuntu server from Kali Linux.

### SCP

SCP is a file-copy mechanism that operates over SSH, providing encrypted transport for file transfers. It was used to transfer a file from the Kali Linux workstation to the Ubuntu server.

### Authentication

The SSH and SCP operations required authentication to the Ubuntu user account. In this lab, authentication was performed using the account credentials configured on the Ubuntu server.

### Network Segmentation

The SSH and SCP communication in this exercise occurred over the Host-only network:

```text
192.168.56.0/24
```

This keeps the lab communication separate from the external network while the NAT interface provides Internet connectivity.

---

## Commands Used

| Command | Purpose |
|---|---|
| `systemctl status ssh` | Check SSH service status |
| `ssh user@host` | Establish a remote SSH session |
| `scp file user@host:path` | Securely transfer a file |
| `ls -l` | Verify file existence and permissions |
| `cat` | Display file contents |

---

## Skills Demonstrated

- SSH administration
- Linux remote access
- Secure file transfer
- Linux networking
- Authentication
- File verification
- Basic troubleshooting
- Command-line administration

---

## Lessons Learned

This lab demonstrated how SSH can be used to securely administer a remote Linux server and how SCP can be used to transfer files through the SSH infrastructure.

Verifying the transferred file on the destination reinforced the importance of validating the result of an administrative operation rather than relying solely on the absence of an error message.

---

## Next Steps

Future labs will build on this environment by examining network services, scanning hosts with Nmap, and analysing network traffic with Wireshark.