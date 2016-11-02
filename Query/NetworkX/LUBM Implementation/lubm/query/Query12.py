'''
Created on 2015. 3. 17.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class Query12(AbstractQuery):
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query12')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        for node, properties in self.graph.nodes_iter(data = True):
            isHead = False
            department = None
            for dummy, neighbor, edgeType in self.graph.edges_iter(nbunch = node, data = True):
                if 'headOf' in edgeType['id']:
                    isHead = True
                if 'worksFor' in edgeType['id'] and self.graph.node[neighbor]['type'] == 'Department':
                    department = neighbor
            
            if isHead == True and department is not None and self.graph.has_edge(department, 'http://www.University0.edu') and 'subOrganizationOf' in self.graph.edge[department]['http://www.University0.edu'].keys():
                self.writer.writeLine(str(node) + ', ' + str(department))
                        
    def finalize(self):
        AbstractQuery.finalize(self)
        