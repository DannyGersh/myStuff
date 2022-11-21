#!/bin/sh
cd /main/myStuff
git pull
hostname -I > ip
python3 extractIp.py
git add -A
git commit -m "auto push"
git push origin master
