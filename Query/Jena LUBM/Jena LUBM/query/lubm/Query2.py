'''
Created on Apr 17, 2015
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

from query.AbstractQuery import AbstractQuery
from requests.exceptions import ConnectionError

class Query2(AbstractQuery):
    QUERY = ''' PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX ub: <http://test/univ.com#>
                SELECT ?X ?Y ?Z
                WHERE
                {
                    ?X rdf:type ub:GraduateStudent .
                    ?Y rdf:type ub:University .
                    ?Z rdf:type ub:Department .
                    ?X ub:memberOf ?Z .
                    ?Z ub:subOrganizationOf ?Y .
                    ?X ub:undergraduateDegreeFrom ?Y
                }'''
    
    def __init__(self):
        AbstractQuery.__init__(self, 'LUBM Query2')
    
    def initialize(self):
        AbstractQuery.initialize(self)
    
    def process(self):
        try:
            results = self.connection.urika.query(self.name, Query2.QUERY)
            for result in results['results']['bindings']:
                self.writer.writeLine(result['X']['value'] + '\t' + result['Y']['value'] + '\t' + result['Z']['value'])
        except ConnectionError:
            print 'No connection could be made.'    
    
    def finalize(self):
        AbstractQuery.finalize(self)
        