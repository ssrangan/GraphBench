'''
Created on 2015. 4. 9.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

import operator
import networkx as nx
from query.AbstractQuery import AbstractQuery
from networkx.algorithms.traversal.depth_first_search import dfs_tree

class QueryG(AbstractQuery):    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM QueryG')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        universities = [node for node, properties in self.graph.nodes_iter(data = True) if properties['type'] == 'University' and 'name' in properties]
        for university in universities:
            professorCount = self.count(university)
            self.writer.writeLine(university + ', ' + str(professorCount))
    
    def finalize(self):
        AbstractQuery.finalize(self)
    
    def count(self, university):
        targetTypes = ['Lecturer', 'AssistantProfessor', 'AssociateProfessor', 'FullProfessor']
        professors = set()
        each = nx.single_source_shortest_path_length(self.graph.to_undirected(), university, cutoff = 2)
       
        for node in each.keys():
            if self.graph.node[node]['type'] in targetTypes:
                for dummy, course, edgeType in self.graph.edges_iter(nbunch = node, data = True):
                    if 'teacherOf' in edgeType['id']:
                        professors.add(node)
        
        return len(professors)