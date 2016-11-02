/**
 * LUBM Query 7
 * Author: Seokyong Hong
 * Email: shong3@ncsu.edu
 * Date: 03/21/2015 
 */

package main.scala.lubm

import java.io._
import org.apache.spark.rdd.RDD
import main.scala.operation.Query
import org.apache.spark.graphx._

class LUBMQuery7 (graphRDD: Graph[(String, String, String, String, Boolean, String, String), String]) extends Query(graphRDD) {
    val NAME = "LUBMQuery7"
    
    override def execute(directory: String) = {
//        val writer = new PrintWriter(new File(directory, NAME))
        
        val teacherOf: RDD[(Long, (String))] = graph.triplets.filter(triplet => (triplet.srcAttr._1 == "http://www.Department0.University0.edu/AssociateProfessor0" && triplet.attr == "teacherOf" && (triplet.dstAttr._2 == "Course" || triplet.dstAttr._2 == "GraduateCourse"))).map {
            triplet => (triplet.dstId, (triplet.dstAttr._1))
        }
        
        val takesCourse: RDD[(Long, (String))] = graph.triplets.filter(triplet => ((triplet.srcAttr._2 == "UndergraduateStudent" || triplet.srcAttr._2 == "GraduateStudent") && triplet.attr == "takesCourse" && (triplet.dstAttr._2 == "Course" || triplet.dstAttr._2 == "GraduateCourse"))).map {
            triplet => (triplet.dstId, (triplet.srcAttr._1))
        }
        
        val joined = teacherOf.join(takesCourse).map {
            case (courseID, ((course), (student))) => (student, course)
        }
                
	joined.saveAsTextFile(directory+"/"+NAME)
/*
        for((student, course) <- joined.collect())
            writer.println(student + "\t" + course)
        
        writer.close()
*/
    }
}
