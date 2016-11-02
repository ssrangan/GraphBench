'''
Created on 2015. 3. 16.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class Query8(AbstractQuery):
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query8')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        studentTypes = ['GraduateStudent', 'UndergraduateStudent']
        
        for node, properties in self.graph.nodes_iter(data = True):
            if properties['type'] in studentTypes:
                for dummy, neighbor, edgeType in self.graph.edges_iter(nbunch = node, data = True):
                    if 'memberOf' in edgeType['id'] and self.graph.node[neighbor]['type'] == 'Department':
                        if self.graph.has_edge(neighbor, 'http://www.University0.edu') and 'subOrganizationOf' in self.graph.edge[neighbor]['http://www.University0.edu'].keys():
                            self.writer.writeLine(str(node) + ', ' + str(neighbor) + ', ' + properties['emailAddress'])
                            break
                        
    def finalize(self):
        AbstractQuery.finalize(self)
        