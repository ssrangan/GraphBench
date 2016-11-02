MATCH
	(graduateStudent:GraduateStudent)-[:memberOf]->(department:Department),
	(department)-[:subOrganizationOf]->(university:University),
	(graduateStudent)-[:undergraduateDegreeFrom]->(university)
RETURN
	graduateStudent.uri, university.uri, department.uri;

