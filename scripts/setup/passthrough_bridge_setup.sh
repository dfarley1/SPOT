#!/bin/bash

if [ "$EUID" -ne 0 ]
then echo "Must be root"
exit
fi

ADAPTER="eth0"

# Allow overriding from eth0 by passing in a single argument
if [ $# -eq 1 ]; then
    ADAPTER="$1"
fi

#Uncomment net.ipv4.ip_forward
sed -i -- 's/#net.ipv4.ip_forward/net.ipv4.ip_forward/g' /etc/sysctl.conf
#Change value of net.ipv4.ip_forward if not already 1
sed -i -- 's/net.ipv4.ip_forward=0/net.ipv4.ip_forward=1/g' /etc/sysctl.conf
#Activate on current system
echo 1 > /proc/sys/net/ipv4/ip_forward

iptables -t nat -A POSTROUTING -o $ADAPTER -j MASQUERADE  
iptables -A FORWARD -i $ADAPTER -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT  
iptables -A FORWARD -i wlan0 -o $ADAPTER -j ACCEPT

