from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        # Inisiasi topologi
        Topo.__init__(self)

        # Add host dan switch
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add link
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)
        self.addLink(s1, s2)

topos = {'mytopo': (lambda : MyTopo())}
locations = {'c0': (476,63), 'h4': (688,339), 'h2': (419,339), 'h3': (518,340), 'h1': (221,337), 's1': (328,204), 's2': (605,204)}
