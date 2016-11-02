'''
Created on 2015. 3. 16.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class Query9(AbstractQuery):
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query9')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        studentTypes = ['GraduateStudent', 'UndergraduateStudent']
        professorTypes = ['AssistantProfessor', 'AssociateProfessor', 'FullProfessor']
        courseTypes = ['GraduateCourse', 'Course']
        
        for node, properties in self.graph.nodes_iter(data = True):
            if properties['type'] in studentTypes:
                for dummy1, neighbor1, edgeType1 in self.graph.edges_iter(nbunch = node, data = True):
                    if 'advisor' in edgeType1['id'] and self.graph.node[neighbor1]['type'] in professorTypes:
                        for dummy2, neighbor2, edgeType2 in self.graph.edges_iter(nbunch = neighbor1, data = True):
                            if 'teacherOf' in edgeType2['id'] and self.graph.node[neighbor2]['type'] in courseTypes and self.graph.has_edge(node, neighbor2) and 'takesCourse' in self.graph.edge[node][neighbor2].keys():
                                self.writer.writeLine(str(node) + ', ' + str(neighbor1) + ', ' + str(neighbor2))
                        
    def finalize(self):
        AbstractQuery.finalize(self)
        