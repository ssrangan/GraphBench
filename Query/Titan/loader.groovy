
// for in-memory backend
//graph = TitanFactory.build().set('storage.backend', 'inmemory').open()
// for hbase backend
graph = TitanFactory.open('/usr/local/titan/conf/titan-hbase.properties') 

// creating property keys
mgmt = graph.getManagementSystem()
//mgmt.set("ids.block-size",500000000)

// node properties
type = mgmt.makePropertyKey('type').dataType(String.class).make()
uri = mgmt.makePropertyKey('uri').dataType(String.class).make()
researchAssistant = mgmt.makePropertyKey('researchAssistant').dataType(Boolean.class).make()
name = mgmt.makePropertyKey('name').dataType(String.class).make()
emailAddress = mgmt.makePropertyKey('emailAddress').dataType(String.class).make()
telephone = mgmt.makePropertyKey('telephone').dataType(String.class).make()
researchInterest = mgmt.makePropertyKey('researchInterest').dataType(String.class).make()

// edge labels
takesCourse = mgmt.makeEdgeLabel('takesCourse').make()
teacherOf = mgmt.makeEdgeLabel('teacherOf').make()
undergraduateDegreeFrom = mgmt.makeEdgeLabel('undergraduateDegreeFrom').make()
mastersDegreeFrom = mgmt.makeEdgeLabel('mastersDegreeFrom').make()
doctoralDegreeFrom = mgmt.makeEdgeLabel('doctoralDegreeFrom').make()
advisor = mgmt.makeEdgeLabel('advisor').make()
memberOf = mgmt.makeEdgeLabel('memberOf').make()
publicationAuthor = mgmt.makeEdgeLabel('publicationAuthor').make()
headOf = mgmt.makeEdgeLabel('headOf').make()
teachingAssistantOf = mgmt.makeEdgeLabel('teachingAssistantOf').make()
subOrganizationOf = mgmt.makeEdgeLabel('subOrganizationOf').make()
worksFor = mgmt.makeEdgeLabel('worksFor').make()

mgmt.commit()

//Loading
start = System.currentTimeMillis()
GraphMLReader.inputGraph(graph, new FileInputStream("/mnt/data/benchmark/LUBM/LUBM/data/university_2000.graphml"))
println(System.currentTimeMillis() - start)

System.exit(0)
