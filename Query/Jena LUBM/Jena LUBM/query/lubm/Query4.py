'''
Created on Apr 17, 2015
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery
from requests.exceptions import ConnectionError

class Query4(AbstractQuery):
    QUERY = ''' PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX ub: <http://test/univ.com#>
                SELECT ?X ?Y1 ?Y2 ?Y3
                WHERE
                {
                    { ?X rdf:type ub:AssistantProfessor . }
                    UNION 
                    { ?X rdf:type ub:AssociateProfessor . }
                    UNION
                    { ?X rdf:type ub:FullProfessor . }
                    ?X ub:worksFor <http://www.Department0.University0.edu> .
                    ?X ub:name ?Y1 .
                    ?X ub:emailAddress ?Y2 .
                    ?X ub:telephone ?Y3
                }'''
    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query4')
    
    def initialize(self):
        AbstractQuery.initialize(self)
    
    def process(self):
        try:
            results = self.connection.urika.query(self.name, Query4.QUERY)
            for result in results['results']['bindings']:
                self.writer.writeLine(result['X']['value'] + '\t' + result['Y1']['value'] + '\t' + result['Y2']['value'] + '\t' + result['Y3']['value'])
        except ConnectionError:
            print 'No connection could be made.'
        finally:
            self.writer.close()          
    
    def finalize(self):
        AbstractQuery.finalize(self)