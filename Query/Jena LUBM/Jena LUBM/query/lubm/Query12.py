'''
Created on Apr 17, 2015
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery
from requests.exceptions import ConnectionError

class Query12(AbstractQuery):
    QUERY = ''' PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX ub: <http://test/univ.com#>
                SELECT ?X ?Y
                WHERE
                {
                    ?X ub:headOf [] .
                    ?Y rdf:type ub:Department .
                    ?X ub:worksFor ?Y .
                    ?Y ub:subOrganizationOf <http://www.University0.edu>
                }
            '''
    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query12')
    
    def initialize(self):
        AbstractQuery.initialize(self)
    
    def process(self):
        try:
            results = self.connection.urika.query(self.name, Query12.QUERY)
            for result in results['results']['bindings']:
                self.writer.writeLine(result['X']['value'] + '\t' + result['Y']['value'])
        except ConnectionError:
            print 'No connection could be made.'
        finally:
            self.writer.close()          
    
    def finalize(self):
        AbstractQuery.finalize(self)