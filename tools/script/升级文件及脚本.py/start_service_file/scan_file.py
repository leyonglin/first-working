#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: star -*-

######################################################################
# this's use for scanning the file which end with jsp or jspx file,
# and move files to /home/blog.
######################################################################

import os
import time
import commands


target_dir = '/opt/webapps/'
log_file = '/home/blog/scan.log'
danger_string_filter="-iname '*.jsp' -o -iname '*.jspx'  -o -iname '*.py' -o -iname '*.sh' -o -iname '*.php'"


def find_danger_files():
    danger_files=commands.getoutput('find %s -type f %s'%(target_dir, danger_string_filter))
    if danger_files:
        danger_files_list = danger_files.split('\n')
        for i in danger_files_list:
            os.system('mv %s /home/blog'%(i))
            with open(log_file, 'a') as f:
                            cur_time = time.ctime()
                            f.write(cur_time + '--' + i + '\n')

if __name__ == '__main__':
        while True:
                find_danger_files()
                time.sleep(60)
