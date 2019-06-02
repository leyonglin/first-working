#!/bin/bash
find /opt/backup/ -mtime +3 -name data_views* -type f |xargs rm -f
find /opt/apps/cdn_back/ -mtime +7 -type f |xargs rm -f
find /opt/backup/ -mindepth 3 -maxdepth 3 -type d  -mtime +4 -name 2019* |xargs rm -rf
