from pyretic.lib.corelib import *

IP1 = IPAddr("10.0.0.1")
IP2 = IPAddr("10.0.0.2")
IP3 = IPAddr("10.0.0.3")
IP4 = IPAddr("10.0.0.4")
IP5 = IPAddr("10.0.0.5")
IP6 = IPAddr("10.0.0.6")
IP7 = IPAddr("10.0.0.7")
IP8 = IPAddr("10.0.0.8")

sw1= (match(dstip=IP1) >> fwd(1)) + (match(dstip=IP2) >> fwd(1)) + (match(dstip=IP3) >> fwd(2)) + (match(dstip=IP4) >> fwd(2)) + (match(dstip=IP5) >> fwd(3)) + (match(dstip=IP6) >> fwd(3)) + (match(dstip=IP7) >> fwd(4)) + (match(dstip=IP8) >> fwd(4))
sw2= (match(dstip=IP1) >> fwd(1)) + (match(dstip=IP2) >> fwd(2)) + (match(dstip=IP3) >> fwd(4)) + (match(dstip=IP4) >> fwd(4)) + (match(dstip=IP5) >> fwd(3)) + (match(dstip=IP6) >> fwd(3)) + (match(dstip=IP7) >> fwd(5)) + (match(dstip=IP8) >> fwd(5))
sw3= (match(dstip=IP1) >> fwd(4)) + (match(dstip=IP2) >> fwd(4)) + (match(dstip=IP3) >> fwd(1)) + (match(dstip=IP4) >> fwd(2)) + (match(dstip=IP5) >> fwd(5)) + (match(dstip=IP6) >> fwd(5)) + (match(dstip=IP7) >> fwd(3)) + (match(dstip=IP8) >> fwd(3))
sw4= (match(dstip=IP1) >> fwd(3)) + (match(dstip=IP2) >> fwd(3)) + (match(dstip=IP3) >> fwd(4)) + (match(dstip=IP4) >> fwd(4)) + (match(dstip=IP5) >> fwd(1)) + (match(dstip=IP6) >> fwd(2)) + (match(dstip=IP7) >> fwd(5)) + (match(dstip=IP8) >> fwd(5))
sw5= (match(dstip=IP1) >> fwd(4)) + (match(dstip=IP2) >> fwd(4)) + (match(dstip=IP3) >> fwd(3)) + (match(dstip=IP4) >> fwd(3)) + (match(dstip=IP5) >> fwd(5)) + (match(dstip=IP6) >> fwd(5)) + (match(dstip=IP7) >> fwd(1)) + (match(dstip=IP8) >> fwd(2))

forward = if_(match(switch=1), sw1) + if_(match(switch=2), sw2) + if_(match(switch=3), sw3) + if_(match(switch=4), sw4) + if_(match(switch=5), sw5) 

def main():
    return forward
