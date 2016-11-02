/**
 * LUBM Query 12
 * Author: Seokyong Hong
 * Email: shong3@ncsu.edu
 * Date: 03/21/2015 
 */

package main.scala.lubm

import java.io._
import org.apache.spark.rdd.RDD
import main.scala.operation.Query
import org.apache.spark.graphx._

class LUBMQuery12 (graphRDD: Graph[(String, String, String, String, Boolean, String, String), String]) extends Query(graphRDD) {
    val NAME = "LUBMQuery12"
    
    override def execute(directory: String) = {
//        val writer = new PrintWriter(new File(directory, NAME))
        
        val worksFor: RDD[(Long, (String))] = graph.triplets.filter(triplet => (triplet.attr == "headOf")).map {
            triplet => (triplet.dstId, (triplet.srcAttr._1))
        }
        val subOrganizationOf: RDD[(Long, (String))] = graph.triplets.filter(triplet => (triplet.srcAttr._2 == "Department" && triplet.attr == "subOrganizationOf" && triplet.dstAttr._1 == "http://www.University0.edu")).map {
            triplet => (triplet.srcId, (triplet.srcAttr._1))
        }
        
        val joined = worksFor.join(subOrganizationOf).map {
            case (deptID, ((person), (department))) => (person, department)
        }
 	joined.saveAsTextFile(directory+"/"+NAME)               
/*
        for((person, department) <- joined.collect())
            writer.println(person + "\t" + department)
        
        writer.close()
*/
    }
}
