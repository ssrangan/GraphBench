'''
Created on 2015. 3. 16.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class Query2(AbstractQuery):
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query2')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        for node, properties in self.graph.nodes_iter(data = True):
            if properties['type'] == 'GraduateStudent':
                university = None
                department = None
                for dummy, neighbor, edgeType in self.graph.edges_iter(nbunch = node, data = True):
                    if 'memberOf' in edgeType['id']:
                        department = neighbor
                    if 'undergraduateDegreeFrom' in edgeType['id']:
                        university = neighbor
                    if university is not None and department is not None:
                        break
                
                if university is not None and department is not None:
                    if self.graph.node[university]['type'] == 'University' and self.graph.node[department]['type'] == 'Department':
                        if self.graph.has_edge(department, university) and self.graph.edge[department][university]['subOrganizationOf'] is not None:
                            self.writer.writeLine(str(node) + ', ' + str(university) + ', ' + department)          
    
    def finalize(self):
        AbstractQuery.finalize(self)
        