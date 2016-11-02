'''
Created on Apr 17, 2015
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery
from requests.exceptions import ConnectionError

class Query9(AbstractQuery):
    QUERY = ''' PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX ub: <http://test/univ.com#>
                SELECT ?X ?Y ?Z
                WHERE
                {
                    { ?X rdf:type ub:UndergraduateStudent }
                    UNION
                    { ?X rdf:type ub:GraduateStudent }
                    ?X ub:advisor ?Y .
                    { ?Y rdf:type ub:AssistantProfessor . }
                    UNION 
                    { ?Y rdf:type ub:AssociateProfessor . }
                    UNION
                    { ?Y rdf:type ub:FullProfessor . }
                    ?Y ub:teacherOf ?Z .
                    { ?Z rdf:type ub:Course }
                    UNION
                    { ?Z rdf:type ub:GraduateCourse }
                    ?X ub:takesCourse ?Z
                }
            '''
    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query9')
    
    def initialize(self):
        AbstractQuery.initialize(self)
    
    def process(self):
        try:
            results = self.connection.urika.query(self.name, Query9.QUERY)
            for result in results['results']['bindings']:
                self.writer.writeLine(result['X']['value'] + '\t' + result['Y']['value'] + '\t' + result['Z']['value'])
        except ConnectionError:
            print 'No connection could be made.'
        finally:
            self.writer.close()          
    
    def finalize(self):
        AbstractQuery.finalize(self)