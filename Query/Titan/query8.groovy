
// for in-memory backend
//graph = TitanFactory.build().set('storage.backend', 'inmemory').open()
// for hbase backend
graph = TitanFactory.open('/usr/local/titan/conf/titan-hbase.properties') 


//[Query 8] 
def benchmark = { closure -> 
	start = System.currentTimeMillis()
	closure.call()
	System.currentTimeMillis() - start
}

def duration = benchmark{
	department = null
	new File("/mnt/data/benchmark/results/Titan/Query8.txt").withWriter { f -> graph.V.has('uri', T.eq, 'http://www.University0.edu').in('subOrganizationOf').filter{it.type == 'Department'}.as('department').sideEffect {department = "${it.uri}"}.in('memberOf').filter{it.type == 'UndergraduateStudent' || it.type == 'GraduateStudent'}.as('student').sideEffect { f << "$department, ${it.uri}, ${it.emailAddress}\r\n"}.iterate() };

}


println "${duration} ms"

System.exit(0)
