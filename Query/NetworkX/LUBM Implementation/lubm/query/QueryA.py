'''
Created on 2015. 4. 8.
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery

class QueryA(AbstractQuery):
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM QueryA')
    
    def initialize(self, graph):
        AbstractQuery.initialize(self, graph)
    
    def process(self):
        source = 'http://www.Department0.University0.edu/GraduateStudent1'
        advisor = None
        classmates = set()
        students = set()
        
        for node in self.graph.successors(source):
            if self.graph.has_edge(source, node) and 'advisor' in self.graph.edge[source][node].keys():
                advisor = node
                break
        
        for student in self.graph.predecessors_iter(advisor):
            if student != source and self.graph.node[student]['type'] == 'GraduateStudent' and 'advisor' in self.graph.edge[student][advisor].keys():
                students.add(student)
                for dummy, course, edgeType in self.graph.edges_iter(nbunch = student, data = True):
                    if edgeType['id'] == 'takesCourse' and (self.graph.node[course]['type'] == 'Course' or self.graph.node[course]['type'] == 'GraduateCourse'):
                        for classmate in self.graph.predecessors_iter(course):
                            if 'takesCourse' in self.graph.edge[classmate][course].keys() and (self.graph.node[classmate]['type'] == 'UndergraduateStudent' or self.graph.node[classmate]['type'] == 'GraduateStudent') and classmate != source:
                                classmates.add(classmate)
        
        for classmate in classmates - students:
            self.writer.writeLine(str(classmate))
        
    def finalize(self):
        AbstractQuery.finalize(self)