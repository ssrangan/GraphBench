'''
Created on 2015. 4. 8.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class QueryE(AbstractQuery):    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM QueryE')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        copiedGraph = self.graph.copy()
        targetTypes = ['GraduateStudent', 'UndergraduateStudent', 'Course', 'GraduateCourse', 'Publication']
        targetNodes = [node for node, properties in copiedGraph.nodes_iter(data = True) if properties['type'] in targetTypes]
        copiedGraph.remove_nodes_from(targetNodes)
       
        for source, target, edgeType in copiedGraph.edges_iter(nbunch = None, data = True):
            self.writer.writeLine(source + ', ' + edgeType['id'] + ', ' + target)
        
    def finalize(self):
        AbstractQuery.finalize(self)
        