from multiprocessing import Lock
from pyretic.lib.query import *
from pyretic.core import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.modules.priority import priorityDictionary


def build_dic(sip,dip,path):
    dic={}
    dic[sip]={dip:path}
    return dic

class  build_path():
    def __init__(self,topology,switch,dstswitch,dstport,wG=None):
        self.topology=topology
        self.srcswitch=switch
        self.dstswitch = dstswitch
        self.dstport = dstport
        self.wG = wG


    def dij_routing(self):
        pathlist=[]
        dist, pred = self.dijalg(self.topology,str(self.srcswitch),self.wG)
        print self.topology
        if pred:
            v = self.dstswitch
            while(v != self.srcswitch):
                pathlist.append(Location(pred[v],self.topology[pred[v]][v][pred[v]]))
                v = pred[v]
            pathlist.append(Location(self.dstswitch,self.dstport))
        print pathlist
        return pathlist

    def dijalg(self,G,source,wG=None,huge=1e30000):
        dist={}
        pred={}
        Q = priorityDictionary()
        Q[source] = 0
        if wG == None:
            for u in G.edge:
                dist[u]={}
                for v in G.edge:
                    if G.has_edge(u,v):
                        dist[u][v] = 1
                    else:
                        dist[u][v]=huge
                dist[u][u]=0
        else:
            dist = wG
        D = {}
        for v in Q:
            D[v] = Q[v]
            if v == None or not dist.has_key(int(v,10)) : break
            for w in dist[int(v,10)]:
                vwlength = D[v]+dist[int(v,10)][w]
                if str(w) in D:
                    if vwlength < D[str(w)]:
                       raise ValueError
                elif str(w) not in Q or vwlength < Q[str(w)]:
                    Q[str(w)] = vwlength
                    pred[w] = int(v,10)
	print dist

        return D,pred


class build_flowtable(DynamicPolicy):

    def __init__(self,dic, weight = None):

        self.weight = weight
        self.switch = None
        self.port = None
        self.forward = drop
        self.dic=dic
        self.topology = drop
        super(build_flowtable,self).__init__()

    def set_network(self, network):
        if not network is None:
            for sip in self.dic.keys():
                for dip in self.dic[sip].keys():
                    for loc in self.dic[sip][dip]:
                        self.forward = if_(match(switch = loc.switch, srcip=sip,dstip=dip),fwd(loc.port_no),self.forward)
            self.policy = self.forward
