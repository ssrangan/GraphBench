'''
Created on 2015. 3. 16.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class Query7(AbstractQuery):
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query7')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        studentTypes = ['GraduateStudent', 'UndergraduateStudent']
        
        for node, properties in self.graph.nodes_iter(data = True):
            if properties['type'] in studentTypes:
                for dummy, neighbor, edgeType in self.graph.edges_iter(nbunch = node, data = True):
                    if 'takesCourse' in edgeType['id'] and (self.graph.node[neighbor]['type'] == 'Course' or self.graph.node[neighbor]['type'] == 'GraduateCourse'):
                        if self.graph.has_edge('http://www.Department0.University0.edu/AssociateProfessor0', neighbor) and 'teacherOf' in self.graph['http://www.Department0.University0.edu/AssociateProfessor0'][neighbor].keys():
                            self.writer.writeLine(str(node) + ', ' + str(neighbor))
                        
    def finalize(self):
        AbstractQuery.finalize(self)
        