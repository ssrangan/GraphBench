/**
 * Abstract Class for Queries
 * Author: Seokyong Hong
 * Email: shong3@ncsu.edu
 * Date: 03/20/2015 
 */

package main.scala.operation

import org.apache.spark.graphx._

abstract class Query[S, T](val graphRDD: Graph[S, T]) {
    var graph: Graph[S, T] = graphRDD
    
    def execute(directory: String)
}