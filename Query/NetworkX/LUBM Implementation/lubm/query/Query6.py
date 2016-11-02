'''
Created on 2015. 3. 16.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class Query6(AbstractQuery):
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query6')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        studentTypes = ['GraduateStudent', 'UndergraduateStudent']
        
        for node, properties in self.graph.nodes_iter(data = True):
            if properties['type'] in studentTypes:
                self.writer.writeLine(str(node))                     
    
    def finalize(self):
        AbstractQuery.finalize(self)