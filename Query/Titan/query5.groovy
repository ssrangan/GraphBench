
// for hbase backend
graph = TitanFactory.open('/usr/local/titan/conf/titan-hbase.properties') 

//[Query 5]
def benchmark = { closure -> 
	start = System.currentTimeMillis()
	closure.call()
	System.currentTimeMillis() - start
}

def duration = benchmark{
	new File("/mnt/data/benchmark/results/Titan/Query5.txt").withWriter { f -> graph.V.filter{it.type == 'Department' && it.uri == 'http://www.Department0.University0.edu'}.in('memberOf', 'worksFor').filter{it.type == 'UndergraduateStudent' || it.type == 'GraduateStudent' || it.type == 'Lecturer' || it.type == 'AssistantProfessor' || it.type =='AssociateProfessor' || it.type == 'FullProfessor'}.dedup().as('person').sideEffect { f << "${it.uri}\r\n"}.iterate() }
}



println "${duration} ms"

System.exit(0)
