MATCH
	(person)-[:memberOf|:worksFor]->(department:Department{uri:'http://www.Department0.University0.edu'})
WHERE
	(person.type = 'UndergraduateStudent' or person.type = 'GraduateStudent' or person.type = 'Lecturer' or person.type = 'AssistantProfessor' or person.type = 'AssociateProfessor' or person.type = 'FullProfessor')
RETURN
	person.uri;

