/**
 * LUBM Query 6
 * Author: Seokyong Hong
 * Email: shong3@ncsu.edu
 * Date: 03/21/2015 
 */

package main.scala.lubm

import java.io._
import org.apache.spark.rdd.RDD
import main.scala.operation.Query
import org.apache.spark.graphx._

class LUBMQuery6 (graphRDD: Graph[(String, String, String, String, Boolean, String, String), String]) extends Query(graphRDD) {
    val NAME = "LUBMQuery6"
    
    override def execute(directory: String) = {
//        val writer = new PrintWriter(new File(directory, NAME))
        
        val students: RDD[(String)] = graph.vertices.filter( vertex => (vertex._2._2 == "UndergraduateStudent" || vertex._2._2 == "GraduateStudent")).map {
            vertex => (vertex._2._1)
        }
        
	students.saveAsTextFile(directory+"/"+NAME)
/*
        for((student) <- students.collect())
            writer.println(student)
        
        writer.close()
*/
    }
}
