'''
Created on 2015. 4. 8.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery
from networkx.generators.ego import ego_graph

class QueryD(AbstractQuery):    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM QueryD')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        center = 'http://www.Department0.University0.edu/GraduateStudent0'
        egograph = ego_graph(self.graph, center, radius = 2, center = False, undirected = False, distance = None)
        
        for node in egograph:
            self.writer.writeLine(node)
        
    def finalize(self):
        AbstractQuery.finalize(self)
        