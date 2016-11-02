MATCH
	(student)-[:takesCourse]->(course),
	(professor)-[:teacherOf]->(course)
WHERE
	(student.type = 'UndergraduateStudent' or student.type = 'GraduateStudent') and
	(course.type = 'Course' or course.type = 'GraduateCourse') and
	professor.uri = 'http://www.Department0.University0.edu/AssociateProfessor0'
RETURN
	student.uri, course.uri;

