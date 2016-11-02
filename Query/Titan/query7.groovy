
// for in-memory backend
//graph = TitanFactory.build().set('storage.backend', 'inmemory').open()
// for hbase backend
graph = TitanFactory.open('/usr/local/titan/conf/titan-hbase.properties') 


//[Query 7]
def benchmark = { closure -> 
	start = System.currentTimeMillis()
	closure.call()
	System.currentTimeMillis() - start
}

def duration = benchmark{
	course = null
	new File("/mnt/data/benchmark/results/Titan/Query7.txt").withWriter { f -> graph.V.has('uri', T.eq, 'http://www.Department0.University0.edu/AssociateProfessor0').out('teacherOf').filter{it.type == 'Course' || it.type == 'GraduateCourse'}.as('course').sideEffect {course = "${it.uri}"}.in('takesCourse').filter{it.type == 'UndergraduateStudent' || it.type == 'GraduateStudent'}.as('student').sideEffect { f << "$course, ${it.uri}\r\n"}.iterate() };

}


println "${duration} ms"

System.exit(0)


