/**
 * LUBM Query 14
 * Author: Seokyong Hong
 * Email: shong3@ncsu.edu
 * Date: 03/20/2015 
 */

package main.scala.lubm

import java.io._
import main.scala.operation.Query
import org.apache.spark.graphx._

class LUBMQuery14(graphRDD: Graph[(String, String, String, String, Boolean, String, String), String]) extends Query(graphRDD) {
    val NAME = "LUBMQuery14"
    
    override def execute(directory: String) = {
//        val writer = new PrintWriter(new File(directory, NAME))
        
        graph.vertices.filter(_._2._2 == "UndergraduateStudent").saveAsTextFile(directory+"/"+NAME)
/*
        for((key, (id, tp, name, email, isRA, interst, tel)) <- graph.vertices.filter(_._2._2 == "UndergraduateStudent").collect())
            writer.println(id)
        
        writer.close()
*/
    }
}
