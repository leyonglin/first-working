#!/bin/bash
find /opt/backup/ -mtime +3 -name data_views* -type f |xargs rm -f
