#!/bin/bash

sudo apt install synergy
touch /etc/lightdm/lightdm.conf
sudo echo $'[Seat:*]\nautologin-user=\n[SeatDefaults]\ngreeter-setup-script=/usr/bin/synergyc --name <host_name> <x.x.x.x>' > /etc/lightdm/lightdm.conf
