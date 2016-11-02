'''
Created on 2015. 4. 8.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class QueryB(AbstractQuery):    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM QueryB')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        source = 'http://www.Department0.University0.edu/GraduateStudent1'
        hops = 3
        nodes = set([source])
        neighbors = set()
       
        for distance in range(0, hops):
            for node in nodes:
                neighbors |= set(self.graph[node].keys())
            
            if distance != hops - 1:
                nodes.clear()
                nodes |= neighbors
                neighbors.clear()
        
        for node in neighbors:
            self.writer.writeLine(node)
        
    def finalize(self):
        AbstractQuery.finalize(self)
        