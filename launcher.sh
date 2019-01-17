#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/ARPNLP
sudo python3 ratingbox.py
cd /
