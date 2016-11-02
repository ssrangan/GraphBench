'''
Created on 2015. 4. 8.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

import networkx as nx
from query.AbstractQuery import AbstractQuery

class QueryC(AbstractQuery):    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM QueryC')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        source = 'http://www.University0.edu'
        hops = 3
        reversedGraph = nx.reverse(self.graph, copy = True)
        nodes = set([source])
        neighbors = set()
       
        for distance in range(0, hops):
            for node in nodes:
                neighbors |= set(reversedGraph[node].keys())
            
            if distance != hops - 1:
                nodes.clear()
                nodes |= neighbors
                neighbors.clear()
        
        for node in neighbors:
            self.writer.writeLine(node)
        
    def finalize(self):
        AbstractQuery.finalize(self)
        