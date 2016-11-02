'''
Created on 2015. 3. 16.

@author: Seokyong Hong
'''

class QueryError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message