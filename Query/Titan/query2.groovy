
// for in-memory backend
//graph = TitanFactory.build().set('storage.backend', 'inmemory').open()
// for hbase backend
graph = TitanFactory.open('/usr/local/titan/conf/titan-hbase.properties') 


//[Query 2]
def benchmark = { closure -> 
	start = System.currentTimeMillis()
	closure.call()
	System.currentTimeMillis() - start
}

def duration = benchmark{
	new File("/mnt/data/benchmark/results/Titan/Query2.txt").withWriter { f -> graph.V.filter{it.type == 'GraduateStudent'}.as('graduate_student').out('memberOf').filter{it.type == 'Department'}.out('subOrganizationOf').filter{it.type == 'University'}.inE('undergraduateDegreeFrom').outV.retain('graduate_student').sideEffect { f << "${it.uri}\r\n"}.iterate() }
}


println "${duration} ms"

System.exit(0)
