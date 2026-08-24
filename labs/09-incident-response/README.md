# Lab 09 – SSH Authentication Log Analysis

## Overview

This lab demonstrates the analysis of Linux authentication and SSH service logs to identify successful logins, failed authentication attempts, SSH protocol negotiation failures, and connection activity.

The assessment was performed within the controlled cybersecurity home laboratory using an Ubuntu Server and Kali Linux. Linux authentication logs were examined using command-line tools, with particular attention given to SSH authentication activity.

The purpose of the exercise was to develop practical security monitoring and log-analysis skills relevant to Security Operations Centre (SOC) environments.

---

## Lab Environment

| Component | Configuration |
|---|---|
| Target | Ubuntu Server 26.04 LTS |
| Analysis System | Kali Linux |
| Virtualization | Oracle VirtualBox |
| Network | VirtualBox Host-only |
| Primary Service Analysed | OpenSSH |
| Log Sources | `/var/log/auth.log` and `journalctl -u ssh` |

All analysis was performed against systems within the controlled laboratory environment.

---

## Objectives

The objectives of this lab were to:

- Analyse Linux authentication logs
- Identify successful SSH authentication events
- Identify failed SSH authentication attempts
- Identify SSH protocol negotiation failures
- Correlate events from different log sources
- Identify source IP addresses associated with SSH activity
- Distinguish normal administrative activity from potentially suspicious events
- Produce structured evidence files
- Develop practical SOC-style log-analysis skills
- Understand how authentication logs support security investigations

---

## Log Sources

Two primary log sources were examined.

### `/var/log/auth.log`

The authentication log records security-related events including successful and failed authentication, PAM authentication activity, SSH authentication, `sudo` activity, and session events.

The log was queried using:

```bash
sudo grep -E "Accepted password|Accepted publickey|Failed password|authentication failure" /var/log/auth.log
```

### SSH Service Journal

The SSH service journal was examined using:

```bash
sudo journalctl -u ssh --no-pager | grep -E "Accepted|Failed|authentication|Unable to negotiate|banner exchange"
```

This provided additional SSH service-level information, including protocol negotiation failures and successful authentication events.

---

## Methodology

The investigation followed a structured log-analysis process:

1. Identify relevant authentication and SSH log sources.
2. Search for successful authentication events.
3. Search for failed authentication events.
4. Examine SSH protocol negotiation failures.
5. Identify source IP addresses and timestamps.
6. Compare successful and failed events.
7. Correlate activity across the available logs.
8. Classify the observed activity.
9. Document findings and security recommendations.
10. Preserve the relevant outputs as evidence.

---

# 1. Successful SSH Authentication

Successful SSH authentication events were identified in the SSH service journal.

Example:

```text
Aug 01 03:23:22 Ubuntu sshd-session[4620]: Accepted password for abdul from 192.168.56.103 port 34872 ssh2
Aug 01 03:40:49 Ubuntu sshd-session[5141]: Accepted password for abdul from 192.168.56.103 port 47478 ssh2
Aug 01 03:44:47 Ubuntu sshd-session[5339]: Accepted password for abdul from 192.168.56.103 port 54430 ssh2
Aug 01 03:50:06 Ubuntu sshd-session[5484]: Accepted password for abdul from 192.168.56.103 port 57202 ssh2
Aug 01 03:50:25 Ubuntu sshd-session[5536]: Accepted password for abdul from 192.168.56.103 port 57778 ssh2
```

Additional successful authentications were recorded on subsequent dates, including 4 August, 5 August, 7 August, 11 August, 12 August, and 14 August.

One successful authentication on 12 August was recorded as:

```text
Aug 12 22:58:14 Ubuntu sshd-session[4773]: Accepted password for abdul from 192.168.56.103 port 57688 ssh2
```

### Interpretation

The successful authentication events show that the account `abdul` successfully authenticated to the Ubuntu SSH service from `192.168.56.103`.

Because the activity occurred within the controlled home laboratory, the source address corresponds to the laboratory system used to connect to the Ubuntu server.

These events therefore represent expected administrative activity within the lab rather than confirmed unauthorised access.

---

# 2. Failed SSH Authentication

A failed authentication sequence was identified on 14 August.

```text
Aug 14 12:54:43 Ubuntu sshd-session[26687]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.103  user=abdul
Aug 14 12:54:44 Ubuntu sshd-session[26687]: Failed password for abdul from 192.168.56.103 port 36462 ssh2
Aug 14 12:55:02 Ubuntu sshd-session[26687]: Connection closed by authenticating user abdul 192.168.56.103 port 36462 [preauth]
```

### Interpretation

The sequence shows:

1. An authentication failure for the `abdul` account.
2. A failed password attempt from `192.168.56.103`.
3. The connection subsequently closed during the pre-authentication stage.

The evidence does not demonstrate account compromise. The activity occurred inside the controlled laboratory environment and was followed by connection termination.

A previous authentication sequence on 4 August also showed a failed password followed shortly afterwards by a successful password authentication:

```text
Aug 04 12:25:43 Ubuntu sshd-session[9748]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.103  user=abdul
Aug 04 12:25:44 Ubuntu sshd-session[9748]: Failed password for abdul from 192.168.56.103 port 54580 ssh2
Aug 04 12:25:56 Ubuntu sshd-session[9748]: Accepted password for abdul from 192.168.56.103 port 54580 ssh2
```

This demonstrates how authentication logs can be used to identify failed attempts and determine whether authentication subsequently succeeded.

---

# 3. SSH Protocol Negotiation Events

Several SSH negotiation events were identified.

For example:

```text
Aug 04 12:04:34 Ubuntu sshd-session[6481]: banner exchange: Connection from 192.168.56.103 port 42330: could not read protocol version
Aug 04 12:04:34 Ubuntu sshd-session[6483]: Unable to negotiate with 192.168.56.103 port 42350: no matching key exchange method found. Their offer: diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512,diffie-hellman-group-exchange-sha1,diffie-hellman-group-exchange-sha256 [preauth]
```

Similar events were recorded on 12 August:

```text
Aug 12 13:12:19 Ubuntu sshd-session[5501]: banner exchange: Connection from 192.168.56.103 port 39040: invalid format
Aug 12 13:12:22 Ubuntu sshd-session[5502]: Unable to negotiate with 192.168.56.103 port 39052: no matching key exchange method found. Their offer: diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512,diffie-hellman-group-exchange-sha1,diffie-hellman-group-exchange-sha256 [preauth]
Aug 12 13:15:28 Ubuntu sshd-session[5517]: Unable to negotiate with 192.168.56.103 port 52402: no matching key exchange method found. Their offer: diffie-hellman-group1-sha1 [preauth]
Aug 12 13:24:42 Ubuntu sshd-session[5610]: banner exchange: Connection from 192.168.56.103 port 48810: invalid format
Aug 12 13:24:42 Ubuntu sshd-session[5611]: Unable to negotiate with 192.168.56.103 port 48822: no matching key exchange method found. Their offer: diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512,diffie-hellman-group-exchange-sha1,diffie-hellman-group-exchange-sha256 [preauth]
```

### Interpretation

The server rejected several SSH connection attempts because the client and server could not agree on a compatible key-exchange method.

The client offered a number of older Diffie-Hellman algorithms, including:

- `diffie-hellman-group1-sha1`
- `diffie-hellman-group14-sha1`
- `diffie-hellman-group-exchange-sha1`

The log therefore provides evidence that the SSH server was not accepting these offered algorithms for negotiation.

This is a useful security observation because legacy cryptographic algorithms should generally be avoided where modern alternatives are available.

The events themselves do not establish malicious intent. They were generated from the laboratory source IP address `192.168.56.103`.

---

# 4. Event Correlation

The collected evidence demonstrates several different types of SSH activity originating from the same laboratory source:

| Event Type | Example Date | Source | Result |
|---|---|---|---|
| Successful authentication | 1 August | `192.168.56.103` | Accepted |
| SSH negotiation failure | 4 August | `192.168.56.103` | Rejected |
| Failed authentication | 4 August | `192.168.56.103` | Failed, then succeeded |
| Successful authentication | 5 August | `192.168.56.103` | Accepted |
| Successful authentication | 7 August | `192.168.56.103` | Accepted |
| SSH negotiation failure | 12 August | `192.168.56.103` | Rejected |
| Successful authentication | 12 August | `192.168.56.103` | Accepted |
| Failed authentication | 14 August | `192.168.56.103` | Failed |

### Correlation Assessment

The same source IP address appears throughout the authentication and SSH negotiation events.

Within the controlled lab, this is consistent with the Kali Linux system being used to interact with the Ubuntu server.

The logs also demonstrate an important SOC investigation principle: an isolated log entry may not provide enough context to determine what occurred. Correlating timestamps, source addresses, usernames, authentication results, and SSH service events provides a more complete picture.

---

# 5. Findings

| ID | Finding | Evidence | Classification |
|---|---|---|---|
| LA-01 | Multiple successful SSH authentications were recorded for the `abdul` account | `Accepted password` events | Informational |
| LA-02 | Failed SSH authentication attempts were identified | `Failed password` and `authentication failure` events | Security observation |
| LA-03 | SSH negotiation failures were recorded | `Unable to negotiate` events | Security observation |
| LA-04 | Legacy Diffie-Hellman SHA-1 algorithms were offered during failed negotiation attempts | SSH journal entries | Configuration observation |
| LA-05 | Activity originated from `192.168.56.103` throughout the analysed events | Authentication and SSH logs | Informational |
| LA-06 | The analysed activity occurred within the controlled cybersecurity laboratory | Lab environment context | Informational |

---

# 6. Risk Assessment

No confirmed compromise was identified from the analysed logs.

The failed authentication events demonstrate that authentication failures can occur during normal administration and testing. In isolation, a failed password attempt should not automatically be classified as an attack.

The repeated SSH negotiation failures are also not evidence of compromise. However, they provide useful information about the interaction between the SSH client and server and demonstrate that the server rejected incompatible cryptographic proposals.

The most significant security-monitoring value of this exercise is the ability to distinguish:

- Successful authentication
- Failed authentication
- Protocol negotiation failure
- Normal administrative activity
- Potentially suspicious activity requiring further investigation

In a production environment, repeated failed authentication attempts, especially from unknown external addresses or against multiple accounts, would warrant further investigation.

---

# 7. Security Recommendations

### SSH Authentication Monitoring

Monitor SSH authentication logs for:

- Repeated failed authentication attempts
- Authentication attempts against disabled or non-existent accounts
- Successful logins following repeated failures
- Logins from unexpected source addresses
- Unusual login times
- Repeated connections from the same source

### Cryptographic Configuration

Review SSH cryptographic configuration regularly and maintain modern key-exchange, cipher, host-key, and MAC algorithms.

Legacy algorithms should only be enabled where there is a documented compatibility requirement.

### Account Security

Use strong authentication controls and consider stronger authentication mechanisms such as SSH public-key authentication where appropriate.

Password-based SSH authentication should be reviewed according to the security requirements of the environment.

### Centralised Monitoring

In a production SOC environment, SSH and authentication logs could be forwarded to a central logging or SIEM platform.

This would make it possible to create detections for patterns such as:

```text
Multiple failed SSH attempts
        ↓
Successful authentication
        ↓
Unexpected source address
        ↓
Potential security incident
```

---

# 8. Evidence

The following evidence files were produced during the lab:

```text
labs/
└── 09-log-analysis/
    ├── README.md
    └── evidence/
        ├── failed-authentication.txt
        ├── ssh-authentication-analysis.txt
        └── successful-authentication.txt
```

### `failed-authentication.txt`

Contains the identified failed SSH authentication events, including the 14 August failed authentication sequence.

### `successful-authentication.txt`

Contains successful SSH password authentication events identified during the analysis.

### `ssh-authentication-analysis.txt`

Contains the broader SSH authentication and service-event analysis, including successful authentications, failed authentication attempts, and SSH negotiation events.

The evidence files preserve the raw or extracted command output used to support the findings documented in this README.

---

# 9. Commands Used

### Search authentication events

```bash
sudo grep -E "Accepted password|Accepted publickey|Failed password|authentication failure" /var/log/auth.log
```

### Search SSH service events

```bash
sudo journalctl -u ssh --no-pager | grep -E "Accepted|Failed|authentication|Unable to negotiate|banner exchange"
```

### Inspect authentication log

```bash
sudo tail -n 20 /var/log/auth.log
```

### Inspect SSH service journal

```bash
sudo journalctl -u ssh --no-pager -n 20
```

These commands were used for targeted log retrieval rather than modifying the underlying authentication logs.

---

# 10. Limitations

The assessment has several limitations:

- Analysis was performed against a controlled laboratory server.
- The source IP address belonged to the laboratory environment.
- The investigation focused primarily on SSH and authentication events.
- No production SIEM was used.
- No endpoint detection platform was used.
- No external threat-intelligence enrichment was performed.
- Log analysis alone cannot establish malicious intent.
- The presence of a failed authentication event does not by itself indicate compromise.
- The available evidence does not establish that any observed activity was performed by an unauthorised party.

These limitations should be considered when interpreting the results.

---

# 11. Skills Demonstrated

This lab demonstrates practical experience in:

- Linux log analysis
- SSH authentication analysis
- Authentication event identification
- Failed-login investigation
- Successful-login investigation
- SSH protocol analysis
- Event correlation
- Source-IP analysis
- Command-line investigation
- Evidence collection
- Security monitoring
- SOC-style investigation
- Risk classification
- Security documentation
- Security hardening recommendations

---

# 12. Lessons Learned

This exercise demonstrated that effective security monitoring requires more than simply searching for the word `Failed`.

Authentication logs contain multiple event types that must be interpreted together.

For example, a failed authentication followed by a successful authentication provides different context from repeated failed authentication attempts with no successful login.

Similarly, SSH negotiation failures provide information about the cryptographic capabilities being offered by a connecting client and the algorithms accepted by the server.

The investigation also demonstrated the importance of correlating:

- Timestamp
- Username
- Source IP
- Source port
- Authentication result
- SSH session information
- Protocol negotiation result

This approach provides a more reliable understanding of security events than analysing individual log entries in isolation.

---

# 13. Conclusion

Lab 09 demonstrated a practical SSH authentication log-analysis workflow using Ubuntu Server command-line tools.

The investigation identified successful authentication events, failed password attempts, SSH protocol negotiation failures, and the source IP associated with the observed activity.

No confirmed compromise was identified. The observed events were consistent with activity within the controlled cybersecurity laboratory.

The exercise strengthened practical skills in Linux authentication monitoring, SSH analysis, event correlation, evidence preservation, and SOC-oriented security investigation.

The resulting evidence files provide a reproducible record of the analysis and support the findings documented in this report.
