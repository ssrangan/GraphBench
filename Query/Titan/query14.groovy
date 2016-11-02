
// for in-memory backend
//graph = TitanFactory.build().set('storage.backend', 'inmemory').open()
// for hbase backend
graph = TitanFactory.open('/usr/local/titan/conf/titan-hbase.properties') 


// [Query 14]
def benchmark = { closure -> 
	start = System.currentTimeMillis()
	closure.call()
	System.currentTimeMillis() - start
}

def duration = benchmark{
	new File("/mnt/data/benchmark/results/Titan/Query14.txt").withWriter { f -> graph.V.filter{it.type == 'UndergraduateStudent'}.as('undergraduate').sideEffect { f << "${it.uri}\r\n"}.iterate() };

}

println "${duration} ms"

System.exit(0)

