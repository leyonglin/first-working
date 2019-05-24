#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: star -*-

######################################################################
# this's use for scanning the file which end with jsp or jspx file,
# and move files to /home/blog.
######################################################################

import os
import time


target_dir = '/opt/webapps/'
log_file = '/home/blog/scan.log'
danger_string = ['jsp', 'jspx', 'php', 'sh', 'py']

def finder():
    for (dirpath, dirnames, filenames) in os.walk(target_dir):
        for file in filenames:
            for i in danger_string:
                if str(file).endswith(i) or str(file).endswith(i.upper()) or str(file).endswith(i.lower()):
                    item = os.path.join(dirpath, file)
                    os.system('chown blog %s' % item)
                    os.system('mv %s /home/blog' % item)
                    with open(log_file, 'a') as f:
                        cur_time = time.ctime()
                        f.write(cur_time + '--' + item + '\n') 

if __name__ == '__main__':
	while True:	
		finder()
		time.sleep(60)
