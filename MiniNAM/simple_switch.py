from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        # Insialisasi topologi
        Topo.__init__(self)

        # Add host dan switch
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')

        # Add link
        self.addLink(s1, h1)
        self.addLink(s1, h2)

topos = {'mytopo': (lambda: MyTopo())}
locations = {'c0': (236,194), 'h1': (354,350), 'h2': (663,354), 's1': (525,193)}
