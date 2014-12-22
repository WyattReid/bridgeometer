#! /bin/sh

sudo dhclient eth1
sudo brctl addbr br0
sudo brctl addif br0 eth0
sudo brctl addif br0 eth1

exit 0