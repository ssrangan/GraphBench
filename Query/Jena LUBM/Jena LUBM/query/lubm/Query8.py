'''
Created on Apr 17, 2015
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery
from requests.exceptions import ConnectionError

class Query8(AbstractQuery):
    QUERY = ''' PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX ub: <http://test/univ.com#>
                SELECT ?X ?Y ?Z
                WHERE
                {
                    { ?X rdf:type ub:UndergraduateStudent }
                    UNION
                    { ?X rdf:type ub:GraduateStudent }
                    ?Y rdf:type ub:Department .
                    ?X ub:memberOf ?Y .
                    ?Y ub:subOrganizationOf <http://www.University0.edu> .
                    ?X ub:emailAddress ?Z
                }
            '''
    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query8')
    
    def initialize(self):
        AbstractQuery.initialize(self)
    
    def process(self):
        try:
            results = self.connection.urika.query(self.name, Query8.QUERY)
            for result in results['results']['bindings']:
                self.writer.writeLine(result['X']['value'] + '\t' + result['Y']['value'] + '\t' + result['Z']['value'])
        except ConnectionError:
            print 'No connection could be made.'
        finally:
            self.writer.close()          
    
    def finalize(self):
        AbstractQuery.finalize(self)