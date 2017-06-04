from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
#from pyretic.examples.mac import *
from pyretic.modules.mac_learner import *
################################################
# Translate from
#   client -> public address : client -> server
#   server -> client : public address -> client
################################################
def translate(c, s, p):
    cp = match(srcip=c, dstip=p)
    sc = match(srcip=s, dstip=c)

    return ((cp >> modify(dstip=s)) +
            (sc >> modify(srcip=p)) +
            (~cp & ~sc))

##############################################
# Simple weighted round-robin load balancing policy
##############################################
class wrrlb(DynamicPolicy):
    def __init__(self, clients, servers, public_ip):
        super(wrrlb,self).__init__()

        print("Servers ", servers)

        self.clients        = clients
        self.servers        = servers
        self.public_ip      = public_ip
        self.index          = 0
        self.current_weight = 0
        #self.switch = sw

        self.query     = packets(1,['srcip'])
        self.query.register_callback(self.update_policy)
        self.public_to_controller = (match(dstip=self.public_ip) >> self.query)
        self.lb_policy = None
        self.policy = self.public_to_controller


    def update_policy(self, pkt):


        client = pkt['srcip']
        dest = pkt ['dstip']

        # Becareful not to redirect servers on themselves
		#if client in self.servers: return
        if any (d['ip'] == client for d in self.servers): return

        server = self.next_server()
        #print server
        p = translate(client, server['ip'], self.public_ip)

        #print("Mapping c:%s to s:%s" % (client, server))

        if self.lb_policy:
            self.lb_policy = self.lb_policy >> p # >> dinamis()
        else:
            self.lb_policy = p
        self.policy = self.lb_policy + self.public_to_controller #+ self.query
	    #print self.policy
        #print "ini dari %s to %s" % (client,server)
    def next_server(self):
        cs_index = self.index % len(self.servers)
        #print "cw :" , self.current_weight

        if self.current_weight < self.servers[cs_index]['w']:
            server = self.servers[cs_index]
            self.current_weight += 1
            return server
        else:
            self.index += 1
            self.current_weight = 1
            server = self.servers[self.index % len(self.servers)]
            return server

        #print server
def main():

    public_ip = IP("10.0.0.100")
    print("public ip address is %s." % public_ip)

    client_ips = [IP("10.0.0.4"), IP("10.0.0.5"), IP("10.0.0.6"), IP("10.0.0.7"), IP("10.0.0.8"), IP("10.0.0.9"), IP("10.0.0.10")]
    #server_ips = [IP("10.0.0.1"),IP("10.0.0.2"), IP("10.0.0.3")]
    servers = [{'ip': IP("10.0.0.1"), 'w': 3},{'ip': IP("10.0.0.2"), 'w': 2},{'ip': IP("10.0.0.3"), 'w': 1}]

    return (wrrlb(client_ips, servers, public_ip) >> mac_learner())
