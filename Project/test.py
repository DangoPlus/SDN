from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."
    
    def __init__( self ):
        "Create custom topo."
        
        # Initialize topology
        Topo.__init__( self )
        
        # Add hosts and switches
        host_1 = self.addHost( 'h1' )
        host_2 = self.addHost( 'h2' )
        host_3 = self.addHost( 'h3' )
        host_4 = self.addHost( 'h4' )
        switch_1 = self.addSwitch( 's1' )
        switch_2 = self.addSwitch( 's2' )
        switch_3 = self.addSwitch( 's3' )
        switch_4 = self.addSwitch( 's4' )
        
        # Add links
        self.addLink( host_1, switch_1 )
        self.addLink( switch_1, switch_2 )
        self.addLink( switch_1, switch_3 )
        self.addLink( switch_2, switch_3 )
        self.addLink( switch_2, switch_4 )
        self.addLink( switch_2, host_2)
        self.addLink( switch_3, host_3)
        self.addLink( switch_4, host_4)

topos = { 'mytopo': ( lambda: MyTopo() ) }
