"""
spanning_tree.py 
Custom opology creation for routing example.
"""
from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        "Create custom topo."
    
        #Initialize topology
        Topo.__init__( self )
    
        # Add hosts and switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
    
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')

        #Add links
        self.addLink(s2, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)
        self.addLink(s3, h4)
        self.addLink(s1, h5)
        self.addLink(s1, h6)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, s3)

topos = { 'mytopo': ( lambda: MyTopo() ) }


locations = {'c0':(485,67), 's1':(484,217), 's2':(330,350), 's3':(631,350),'h4': (691,455), 'h1': (254,463),'h2': (380,457), 'h5': (331,97), 'h3': (575,456), 'h6': (636,90)}

