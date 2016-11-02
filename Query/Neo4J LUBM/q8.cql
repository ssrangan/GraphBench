MATCH
	(student)-[:memberOf]->(department:Department),
	(department)-[:subOrganizationOf]->(university:University{uri:'http://www.University0.edu'})
WHERE
	(student.type = 'UndergraduateStudent' or student.type = 'GraduateStudent')
RETURN
	student.uri, department.uri, student.emailAddress;

