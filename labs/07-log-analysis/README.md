# Lab 07 – SSH Log Analysis

## Objective

Perform a controlled log-analysis investigation against the Ubuntu Server using SSH authentication and service logs.

The objective was to identify authentication events, distinguish successful and failed login attempts, correlate source IP addresses, reconstruct a timeline, and classify observed activity using the context of the controlled cybersecurity laboratory.

---

## Scope

| Item | Details |
|---|---|
| Target | Ubuntu Server 26.04 LTS |
| Target IP | `192.168.56.102` |
| Analysis Host | Kali Linux |
| Analysis Host IP | `192.168.56.103` |
| Service | OpenSSH |
| Port | `22/tcp` |
| Network | VirtualBox Host-only |

All activity was performed within the controlled home laboratory.

---

## Investigation Methodology

The investigation followed these steps:

1. Reviewed SSH service events.
2. Examined authentication logs.
3. Identified successful authentication events.
4. Identified failed authentication events.
5. Correlated source IP addresses.
6. Examined SSH negotiation failures.
7. Reconstructed relevant events into a timeline.
8. Classified the activity using laboratory context.
9. Documented security recommendations.

---

## 1. SSH Service Baseline

The Ubuntu server was confirmed to be running the OpenSSH service.

Relevant service events included:

```text
Server listening on 0.0.0.0 port 22
Server listening on :: port 22
Started ssh.service
```

The logs also recorded service shutdown and restart events associated with VM activity.

Evidence:

```text
evidence/ssh-service-events.txt
```

---

## 2. Successful Authentication

The logs contained successful SSH authentication events such as:

```text
Accepted password for abdul from 192.168.56.103
```

The source address corresponds to the Kali Linux analysis VM.

A successful authentication event was therefore classified as expected laboratory activity.

Evidence:

```text
evidence/ssh-successful-logins.txt
```

---

## 3. Failed Authentication Investigation

A controlled failed SSH authentication attempt was generated from the Kali VM.

The Ubuntu authentication logs recorded:

```text
authentication failure
Failed password for abdul from 192.168.56.103
Connection closed by authenticating user abdul
```

### Event details

| Field | Value |
|---|---|
| Target user | `abdul` |
| Source IP | `192.168.56.103` |
| Source port | `36462` |
| Service | SSH |
| Protocol | SSH2 |
| Result | Authentication failed |

The events occurred between approximately:

```text
12:54:43 UTC
12:55:02 UTC
```

Evidence:

```text
evidence/ssh-auth-events.txt
```

---

## 4. SSH Negotiation Events

The SSH service logs also contained multiple connection attempts where the client and server could not agree on a key-exchange algorithm.

For example, the server reported:

```text
Unable to negotiate ... no matching key exchange method found
```

The logs identified the source as:

```text
192.168.56.103
```

Some attempts offered older key-exchange algorithms including:

```text
diffie-hellman-group1-sha1
```

The server rejected these negotiations.

### Security interpretation

These events correlate with the SSH cryptographic assessment performed in Lab 6.

The server's configuration prevented negotiation using algorithms that were not accepted by the server.

These events therefore demonstrate the practical effect of SSH cryptographic policy enforcement.

They should not be classified as malicious activity without additional context.

Evidence:

```text
evidence/ssh-event-correlation.txt
```

---

## 5. Timeline Reconstruction

A simplified timeline of relevant events is:

| Date | Event | Source | Result |
|---|---|---|---|
| Aug 12 | SSH authentication | `192.168.56.103` | Successful |
| Aug 12 | SSH negotiation attempts | `192.168.56.103` | Rejected |
| Aug 12 | SSH authentication | `192.168.56.103` | Successful |
| Aug 14 | SSH authentication failure | `192.168.56.103` | Failed |
| Aug 14 | Failed password | `192.168.56.103` | Rejected |
| Aug 14 | Pre-auth connection closed | `192.168.56.103` | Terminated |

The complete correlation evidence is stored in:

```text
evidence/ssh-event-correlation.txt
```

---

## 6. Analyst Assessment

From the perspective of a security monitoring system, the failed authentication and repeated SSH negotiation failures could warrant investigation.

However, contextual analysis changes the interpretation.

The source IP address:

```text
192.168.56.103
```

belongs to the authorized Kali Linux analysis VM.

The activity was deliberately generated or performed during authorized testing within the home laboratory.

### Classification

**Authorized security testing / simulated suspicious activity**

No evidence from this investigation indicates an external compromise.

---

## 7. Detection Logic

A basic SOC detection rule could identify repeated SSH authentication failures using indicators such as:

- Multiple `Failed password` events
- Repeated authentication failures from one source IP
- Attempts against multiple usernames
- Authentication failures followed by successful authentication
- Repeated SSH negotiation failures
- Unusual authentication times

For example:

```text
IF
    SSH authentication failures exceed a defined threshold
    from the same source IP
THEN
    generate an authentication-failure alert
    and investigate the source and target account.
```

The threshold should be tuned to the environment to reduce false positives.

---

## 8. Recommendations

### Authentication Monitoring

Monitor SSH authentication logs for:

- Repeated failed passwords
- Successful logins following multiple failures
- Unknown usernames
- Unusual source addresses
- Unusual authentication times

### Access Control

Consider:

- Restricting SSH access to trusted network segments
- Using SSH keys instead of password authentication where appropriate
- Applying least privilege
- Disabling unnecessary accounts

### Cryptographic Configuration

Continue reviewing SSH cryptographic algorithms and remove legacy algorithms where compatibility requirements permit.

This follows the SSH configuration assessment performed in Lab 6.

### Centralised Monitoring

For a production environment, forward authentication logs to a central logging or SIEM platform such as:

- Wazuh
- Splunk
- Elastic Security

Centralised collection allows analysts to correlate authentication events across multiple systems.

---

## 9. Limitations

This investigation has several limitations:

- Testing was performed against a controlled laboratory server.
- The observed source IP belongs to the Kali analysis VM.
- Only SSH-related logs were analysed.
- No production authentication data was available.
- No SIEM correlation engine was used.
- No real external attack was simulated.
- The investigation therefore demonstrates the analysis methodology rather than a real-world incident.

---

## Tools Used

- Ubuntu Server
- Kali Linux
- OpenSSH
- `journalctl`
- `grep`
- Linux authentication logs
- Oracle VirtualBox

---

## Skills Demonstrated

- Linux log analysis
- SSH authentication analysis
- Event correlation
- Timeline reconstruction
- Source IP identification
- Security event classification
- False-positive analysis
- Basic SOC detection logic
- Security monitoring
- Evidence collection
- Technical documentation

---

## Lessons Learned

This investigation demonstrated that individual log events must be interpreted in context.

A failed SSH authentication attempt may represent malicious activity, user error, or authorized security testing. Source IP correlation, timestamps, authentication outcomes, and surrounding service events provide the context required to distinguish these scenarios.

The investigation also demonstrated how host-based logs can be correlated with network and security-tool activity from earlier labs to develop a more complete understanding of system behaviour.

---

## Evidence

Raw investigation evidence is stored in:

```text
evidence/
├── ssh-auth-events.txt
├── ssh-successful-logins.txt
├── ssh-service-events.txt
└── ssh-event-correlation.txt
```

Visual evidence:

```text
screenshots/
└── kali-source-ip.png
```