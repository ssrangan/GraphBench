'''
Created on 2015. 4. 9.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

import operator
import networkx as nx
from query.AbstractQuery import AbstractQuery
from networkx.algorithms.traversal.depth_first_search import dfs_tree

class QueryF(AbstractQuery):    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM QueryF')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        source = 'http://www.University0.edu'
        university = nx.single_source_shortest_path_length(self.graph.to_undirected(), source, cutoff = 4)
        
        counts = dict() 
        for student in university.keys():
            if self.graph.node[student]['type'] == 'GraduateStudent':
                for dummy, course, edgeType in self.graph.edges_iter(nbunch = student, data = True):
                    if 'takesCourse' in edgeType['id'] and self.graph.node[course]['type'] == 'GraduateCourse':
                        if counts.has_key(course):
                            counts[course] += 1
                        else:
                            counts[course] = 1 
                
        sorted_list = sorted(counts.items(), key = operator.itemgetter(1), reverse = True)
        
        for index in range(0, 5):
            self.writer.writeLine(sorted_list[index][0] + ', ' + str(sorted_list[index][1]))
        
    def finalize(self):
        AbstractQuery.finalize(self)
        