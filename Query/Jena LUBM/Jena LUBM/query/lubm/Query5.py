'''
Created on Apr 17, 2015
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery
from requests.exceptions import ConnectionError

class Query5(AbstractQuery):
    QUERY = ''' PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX ub: <http://test/univ.com#>
                SELECT ?X
                WHERE
                {
                    { ?X rdf:type ub:AssistantProfessor . }
                    UNION
                    { ?X rdf:type ub:AssociateProfessor . }
                    UNION
                    { ?X rdf:type ub:FullProfessor . }
                    UNION
                    { ?X rdf:type ub:GraduateStudent . }
                    UNION
                    { ?X rdf:type ub:Lecturer . }
                    UNION
                    { ?X rdf:type ub:UndergraduateStudent . }  
                    { ?X ub:memberOf <http://www.Department0.University0.edu> }
                    UNION
                    { ?X ub:worksFor <http://www.Department0.University0.edu> } 
                }'''
    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query5')
    
    def initialize(self):
        AbstractQuery.initialize(self)
    
    def process(self):
        try:
            results = self.connection.urika.query(self.name, Query5.QUERY)
            for result in results['results']['bindings']:
                self.writer.writeLine(result['X']['value'])
        except ConnectionError:
            print 'No connection could be made.'
        finally:
            self.writer.close()          
    
    def finalize(self):
        AbstractQuery.finalize(self)