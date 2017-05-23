from pyretic.lib.corelib import *

IP1 = IPAddr("10.0.0.1")
IP2 = IPAddr("10.0.0.2")

switch = (match(dstip=IP1) >> fwd(1)) + (match(dstip=IP2) >> fwd(2))

def main():
    return switch
