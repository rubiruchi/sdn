#from pyretic.modules.test2 import *
from pyretic.modules.routedijkstra import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
import urllib, json
import thread
import time

class dijkroute(DynamicPolicy):
    """Standard MAC-learning logic"""
    def __init__(self):
        super(dijkroute,self).__init__()
        self.routedic = {}
        self.topology = None
        self.dic={}
        self.wG = None
        self.forward= drop
        self.set_initial_state()
#

    def set_initial_state(self):
        self.query = packets(1,['srcip'])
        self.query.register_callback(self.buildflow)
        self.forward = drop
        self.policy = self.forward + self.query
        self.u_policy()

    def set_network(self,network):
        if self.topology and self.topology==network.topology:
            pass
        else:
            self.topology=network.topology
        self.set_initial_state()


    def u_policy(self):
        """Update the policy based on current forward and query policies"""
        self.policy = self.forward + self.query
    def buildflow(self,pkt):
        if pkt['srcip']!=IPAddr("10.0.0.1"):
            p1=build_path(self.topology,1,pkt['switch'],pkt['inport'])
            path1=p1.dij_routing()
            dc=build_dic(IPAddr("10.0.0.1"),pkt['srcip'],path1)
            if self.dic.has_key(IPAddr("10.0.0.1")):
                self.dic[IPAddr("10.0.0.1")].update(dc[IPAddr("10.0.0.1")])
            else:
                self.dic.update(dc)
            p2=build_path(self.topology,pkt['switch'],1,1)
            path2=p2.dij_routing()
            dc=build_dic(pkt['srcip'],IPAddr("10.0.0.1"),path2)
            if self.dic.has_key(pkt['srcip']):
                self.dic[pkt['srcip']].update(dc[pkt['srcip']])
            else:
                self.dic.update(dc)
            self.forward =build_flowtable(self.dic)
        self.u_policy()


def main():
    return dijkroute()
