'''
Created on 2015. 3. 16.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class Query4(AbstractQuery):
    NODE_WORKS_FOR = 'http://www.Department0.University0.edu'
    ATTRIBUTE_WORKS_FOR = 'worksFor'
        
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query4')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        professorTypes = ['AssistantProfessor', 'AssociateProfessor', 'FullProfessor']
        
        for node, properties in self.graph.nodes_iter(data = True):
            if properties['type'] in professorTypes and self.graph.has_edge(node, Query4.NODE_WORKS_FOR) and self.graph.edge[node][Query4.NODE_WORKS_FOR][Query4.ATTRIBUTE_WORKS_FOR] is not None:
                self.writer.writeLine(str(node) + ", " + properties['name'] + ", " + properties['emailAddress'] + ", " + properties['telephone'])                     
    
    def finalize(self):
        AbstractQuery.finalize(self)
        