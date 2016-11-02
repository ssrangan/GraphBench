MATCH
	(student)
WHERE
	(student.type = 'UndergraduateStudent' or student.type = 'GraduateStudent')
RETURN
	student.uri;
