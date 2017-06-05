from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        #Inisiasi topo
        Topo.__init__(self)

        #Add host
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        #Add switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')

        #Add link
        self.addLink(s1, h1)
        self.addLink(h2, s11)
        self.addLink(s2, s1)
        self.addLink(s5, s1)
        self.addLink(s6, s1)
        self.addLink(s4, s2)
        self.addLink(s3, s2)
        self.addLink(s4, s3)
        self.addLink(s5, s3)
        self.addLink(s7, s3)
        self.addLink(s5, s6)
        self.addLink(s7, s5)
        self.addLink(s7, s6)
        self.addLink(s10, s7)
        self.addLink(s8, s6)
        self.addLink(s9, s8)
        self.addLink(s7, s9)
        self.addLink(s8, s12)
        self.addLink(s9, s12)
        self.addLink(s11, s9)
        self.addLink(s11, s12)
        self.addLink(s11, s10)
        self.addLink(s10, s9)


# Instansiasi topologi dengan nama mytopo sebagai paramater --topo
topos = {'mytopo': (lambda: MyTopo())}
# Definii posisi
locations = {
    'c0': (582, 64),
    'h2': (1083, 258),
    'h1': (56, 60),
    's1': (178, 60),
    's2': (146, 258),
    's3': (250, 395),
    's4': (119, 486),
    's5': (316, 257),
    's6': (477, 169),
    's7': (478, 470),
    's8': (691, 170),
    's9': (690, 317),
    's10': (774, 470),
    's11': (946, 258),
    's12': (947, 115)
}
