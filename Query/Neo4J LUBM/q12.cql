MATCH
	(person)-[:headOf]->(),
	(person)-[:worksFor]->(department:Department),
	(department)-[:subOrganizationOf]->(university:University{uri:'http://www.University0.edu'})
RETURN
	person.uri, department.uri;
