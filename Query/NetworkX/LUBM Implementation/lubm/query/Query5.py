'''
Created on 2015. 3. 16.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class Query5(AbstractQuery):
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query5')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        personTypes = ['AssistantProfessor', 'AssociateProfessor', 'FullProfessor', 'Lecturer', 'GraduateStudent', 'UndergraduateStudent']
        
        for node, properties in self.graph.nodes_iter(data = True):
            if properties['type'] in personTypes and self.graph.has_edge(node, 'http://www.Department0.University0.edu') and ('memberOf' in self.graph.edge[node]['http://www.Department0.University0.edu'].keys() or 'worksFor' in self.graph.edge[node]['http://www.Department0.University0.edu'].keys()):
                self.writer.writeLine(str(node))                     
    
    def finalize(self):
        AbstractQuery.finalize(self)
        