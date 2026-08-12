#!/bin/bash

echo "===== NETWORK REPORT ====="

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

echo "Default gateway:"
ip route

echo

echo "Listening Ports:"
ss -tuln

