from __future__ import division
import os
from collections import namedtuple

_ntuple_diskusage = namedtuple('usage','total used free')

def disk_usage(path):
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return _ntuple_diskusage(total, used, free)

def format_usage(diskStatus):
    print diskStatus
    total = float("%.2f" % (((diskStatus[0]/1024)/1024)/1024))
    used = float("%.2f" % (((diskStatus[1]/1024)/1024)/1024))
    free = float("%.2f" % (((diskStatus[2]/1024)/1024)/1024))
    diskStatusformated = (total,used,free)
    return diskStatusformated


diskStatus = disk_usage('/')
dsf = format_usage(diskStatus)
print format("disk status --> total: %r GB used: %r GB free: %r GB" %(dsf[0],dsf[1],dsf[2])) 