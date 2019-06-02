#!/bin/bash
iscsiadm -m node iqn.2002-10.com.infortrend:raid.sn8361730.301 --login
sleep 10
mount /dev/sdb1 /opt/backup
