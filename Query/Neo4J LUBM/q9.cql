MATCH
	(student)-[:advisor]->(professor),
	(professor)-[:teacherOf]->(course),
	(student)-[:takesCourse]->(course)
WHERE
	(student.type = 'UndergraduateStudent' or student.type = 'GraduateStudent') and
	(professor.type = 'AssistantProfessor' or professor.type = 'AssociateProfessor' or professor.type = 'FullProfessor') and
	(course.type = 'Course' or course.type = 'GraduateCourse')
RETURN
	student.uri, professor.uri, course.uri;
