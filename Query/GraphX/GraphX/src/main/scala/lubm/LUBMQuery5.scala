/**
 * LUBM Query 5
 * Author: Seokyong Hong
 * Email: shong3@ncsu.edu
 * Date: 03/21/2015 
 */

package main.scala.lubm

import java.io._
import org.apache.spark.rdd.RDD
import main.scala.operation.Query
import org.apache.spark.graphx._

class LUBMQuery5 (graphRDD: Graph[(String, String, String, String, Boolean, String, String), String]) extends Query(graphRDD) {
    val NAME = "LUBMQuery5"
    
    override def execute(directory: String) = {
//        val writer = new PrintWriter(new File(directory, NAME))
        
        val triplets: RDD[(String)] = graph.triplets.filter(triplet => ((triplet.srcAttr._2 == "AssistantProfessor" || triplet.srcAttr._2 == "AssociateProfessor" || triplet.srcAttr._2 == "FullProfessor" || triplet.srcAttr._2 == "Lecturer" || triplet.srcAttr._2 == "UndergraduateStudent" || triplet.srcAttr._2 == "GraduateStudent") && (triplet.attr == "worksFor" || triplet.attr == "memberOf") && triplet.dstAttr._1 == "http://www.Department0.University0.edu")).map {
            triplet => (triplet.srcAttr._1)
        }
        
	triplets.saveAsTextFile(directory+"/"+NAME)
/*
        for((person) <- triplets.collect())
            writer.println(person)
        
        writer.close()
*/
    }
}
