'''
Created on Apr 17, 2015
North Carolina State University
@author: Seokyong Hong (shong3@ncsu.edu)
'''

class QueryError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message