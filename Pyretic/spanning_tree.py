from pyretic.lib.corelib import *

h1=IPAddr("10.0.0.1")
h2=IPAddr("10.0.0.2")
h3=IPAddr("10.0.0.3")
h4=IPAddr("10.0.0.4")
h5=IPAddr("10.0.0.5")
h6=IPAddr("10.0.0.6")

route1 = (match(dstip=h1) >> fwd(3)) + (match(dstip=h2) >> fwd(3)) + (match(dstip=h3) >> fwd(4)) + (match(dstip=h4) >> fwd(4)) + (match(dstip=h5) >> fwd(1)) + (match(dstip=h6) >> fwd(2))
route2 = (match(dstip=h1) >> fwd(1)) + (match(dstip=h2) >> fwd(2)) + (match(dstip=h3) >> fwd(4)) + (match(dstip=h4) >> fwd(4)) + (match(dstip=h5) >> fwd(3)) + (match(dstip=h6) >> fwd(3))
route3 = (match(dstip=h1) >> fwd(4)) + (match(dstip=h2) >> fwd(4)) + (match(dstip=h3) >> fwd(1)) + (match(dstip=h4) >> fwd(2)) + (match(dstip=h5) >> fwd(3)) + (match(dstip=h6) >> fwd(3))

policy = if_(match(switch=1), route1) + if_(match(switch=2), route2) + if_(match(switch=3), route3)

def main():
    return policy

