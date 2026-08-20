#!/usr/bin/env python3

import os
import platform
import socket
import subprocess
from datetime import datetime


def run_command(command):
    """Run a system command and return its output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout.strip()
    except Exception as error:
        return f"Error: {error}"


def get_ip_address():
    """Determine the host's primary IP address."""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except socket.error:
        return "Unable to determine IP address"


def main():
    print("=" * 60)
    print("SECURITY SYSTEM REPORT")
    print("=" * 60)

    print(f"Generated: {datetime.now().astimezone()}")
    print()

    print("[SYSTEM INFORMATION]")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Current User: {os.getlogin()}")
    print(f"Operating System: {platform.system()}")
    print(f"OS Release: {platform.release()}")
    print(f"Kernel: {platform.version()}")
    print(f"Architecture: {platform.machine()}")
    print()

    print("[NETWORK INFORMATION]")
    print(f"Primary IP: {get_ip_address()}")
    print()
    print("Network Interfaces:")
    print(run_command(["ip", "addr", "show"]))
    print()

    print("[ROUTING TABLE]")
    print(run_command(["ip", "route"]))
    print()

    print("[LISTENING TCP PORTS]")
    print(run_command(["ss", "-ltn"]))
    print()

    print("[DISK USAGE]")
    print(run_command(["df", "-h"]))
    print()

    print("[MEMORY USAGE]")
    print(run_command(["free", "-h"]))
    print()

    print("=" * 60)
    print("END OF REPORT")
    print("=" * 60)


if __name__ == "__main__":
    main()
