MATCH 
	(professor)-[:worksFor]->(department:Department{uri:'http://www.Department0.University0.edu'}) 
WHERE 	
	(professor.type = 'AssistantProfessor' or professor.type = 'AssociateProfessor' or professor.type = 'FullProfessor')
RETURN
	professor.uri, professor.emailAddress, professor.telephone;
