#!/bin/bash

echo "===== SYSTEM REPORT ====="

echo

echo "Hostname:"
hostname

echo

echo "Current User:"
whoami

echo

echo "IP Address:"
hostname -I

echo

echo "Disk Usage:"
df -h

echo

echo "Memory Usage:"
free -h
