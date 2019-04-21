#!/uer/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os
import sys
import time


class FixNoSections(object):
    def __init__(self, fp):
        self.fp = fp
        self.section_head = '[global]\n'

    def readline(self):
        if self.section_head:
            try:
                return self.section_head
            finally:
                self.section_head = None
        else:
            return self.fp.readline()


#curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = '/opt/apps/rsync/etc/rsyncd.conf'

#token = raw_input("please input siet token:")
#token = token.split()
if len(sys.argv) <= 1:
    print 'Usage: manager_rsyncd token1 token2 ...'
    exit()

else:
    token = sys.argv[1:]
    for t in token:
        if not t.isalnum():
            print 'token type error ! muste be num and str'
            exit()

def createdir(dir):
    os.system('mkdir -p /opt/backup/%s/data_views_nginx' %(dir))
    os.system('mkdir -p /opt/backup/%s/mysqlback' %(dir))


def restartrsyncd():
    os.system('pkill -9 rsync')
    time.sleep(2)
    os.system('sed -i /global/d %s'%(cfgpath))
    os.system('/opt/apps/rsync/bin/rsync --daemon --config=/opt/apps/rsync/etc/rsyncd.conf ')
    s = '\033[1;24;42m \t\t\t rsyncd restarting....\t\t\t \033[0m'
    print(s.center(100))

def manageconfig():
    conf = ConfigParser.ConfigParser()
    conf.readfp(FixNoSections(open(cfgpath)))

    sections = {}
    for i in token:
        sections[i] = {'%s_data_views_nginx' %(i) :'/opt/backup/%s/data_views_nginx/' %(i), '%s_mysql' %(i):'/opt/backup/%s/mysqlback/' %(i)}
    #print(sections)

    for k,v in sections.items():
        for k1,v1 in v.items():
            try:
                conf.add_section(k1)
                conf.set(k1,'path',v1)
                #conf.write(open(cfgpath, 'a'))
                with open(cfgpath, 'w') as f:
                    conf.write(f)
            except ConfigParser.DuplicateSectionError as e:
                s = '\033[1;5m \t\t\t This sit token %s is already exited !!\t\t\t \033[0m' %(k)
                print(s.center(100))
        createdir(k)

    restartrsyncd()


if __name__ == "__main__":
    manageconfig()
