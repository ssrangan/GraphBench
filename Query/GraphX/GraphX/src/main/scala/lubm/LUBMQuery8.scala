/**
 * LUBM Query 8
 * Author: Seokyong Hong
 * Email: shong3@ncsu.edu
 * Date: 03/21/2015 
 */

package main.scala.lubm

import java.io._
import org.apache.spark.rdd.RDD
import main.scala.operation.Query
import org.apache.spark.graphx._

class LUBMQuery8 (graphRDD: Graph[(String, String, String, String, Boolean, String, String), String]) extends Query(graphRDD) {
    val NAME = "LUBMQuery8"
    
    override def execute(directory: String) = {
//        val writer = new PrintWriter(new File(directory, NAME))
        
        val memberOf: RDD[(Long, (String, String))] = graph.triplets.filter(triplet => ((triplet.srcAttr._2 == "UndergraduateStudent" || triplet.srcAttr._2 == "GraduateStudent") && triplet.dstAttr._2 == "Department" && triplet.attr == "memberOf")).map { 
            triplet => (triplet.dstId, (triplet.srcAttr._1, triplet.srcAttr._4))
        }
        
        val subOrganizationOf: RDD[(Long, (String))] = graph.triplets.filter(triplet => (triplet.srcAttr._2 == "Department" && triplet.attr == "subOrganizationOf" && triplet.dstAttr._1 == "http://www.University0.edu")).map {
            triplet => (triplet.srcId, (triplet.srcAttr._1))
        }
        
        val joined = memberOf.join(subOrganizationOf).map {
            case (deptID, ((student, email), (department))) => (student, department, email)
        }
                
	joined.saveAsTextFile(directory+"/"+NAME)
/*
        for((student, department, email) <- joined.collect())
            writer.println(student + "\t" + department + "\t" + email)
        
        writer.close()
*/
    }
}
