'''
Created on Sep 18, 2013

@author: panshul
'''
import sys
from multiprocessing import Process
import time
from mainpackage.DiskChecker import disk_usage, format_usage
from sys import argv
from mainpackage.EmailUtil import sendDiskFullMail

panshul = "panshul@innoplexia.com"
christian = "christian@innoplexia.com"
rene = "rene@innoplexia.com"

recepients = [panshul,christian,rene]

machineName, usage_alert_level,path = "panplexiaSuper",5.0,'/run/user'

#script, machineName, usage_alert_level, path = argv

def is_disk_full(dsf):
    free = dsf[2]
    print free
    print usage_alert_level
    if free<usage_alert_level:
        print "Alert Disk Space Low"
        return True
    return False

def doWork():
    while True:
        diskStatus = disk_usage(path)
        dsf = format_usage(diskStatus)
        checkTime = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime())
        if is_disk_full(dsf):
            print "Send Mail"
            sendDiskFullMail(dsf,recepients,machineName)
        print format("%r : disk status on %r --> total: %r GB used: %r GB free: %r GB" %(checkTime,machineName,dsf[0],dsf[1],dsf[2])) 
        time.sleep((60*60*3))

#sys.path.append('/home/panshul/Development/workingfiles/workspace/com.innoplexia.diskchecker/src/mainpackage')
p = Process(target=doWork)
p.start()

#doWork()


