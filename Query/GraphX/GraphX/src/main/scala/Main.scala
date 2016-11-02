/**
 * GraphX LUBM Benchmark Main
 * Author: Seokyong Hong
 * Email: shong3@ncsu.edu
 * Date: 03/20/2015 
 */

package main.scala

import org.apache.spark.graphx._
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import main.scala.lubm._
import main.scala.operation._

object Main {
    val NODE_PATH = "hdfs://192.168.0.121:9000/data/benchmark/university_nodes_5000.json"
    val EDGE_PATH = "hdfs://192.168.0.121:9000/data/benchmark/university_edges_5000.json"
   
    def main(args: Array[String]) {
        val conf = new SparkConf().setAppName("Spark LUBM Benchmark")
        val sc = new SparkContext(conf)
        val graphRDD :Graph[(String, String, String, String, Boolean, String, String), String] = loader.LUBMJSONLoader.loadDataset(sc, NODE_PATH, EDGE_PATH)
        var query: Query[(String, String, String, String, Boolean, String, String), String] = null
             
        query = new LUBMQuery2(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query2-1")

        query = new LUBMQuery2(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query2-2") 

        query = new LUBMQuery2(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query2-3") 

        query = new LUBMQuery2(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query2-4") 
    	 
        query = new LUBMQuery2(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query2-5") 
    	 
        query = new LUBMQuery4(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query4-1") 
    	 
        query = new LUBMQuery4(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query4-2") 
    	 
        query = new LUBMQuery4(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query4-3") 
    	 
        query = new LUBMQuery4(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query4-4") 
    	 
        query = new LUBMQuery5(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query5-1") 
    	 
        query = new LUBMQuery5(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query5-2") 
    	 
        query = new LUBMQuery5(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query5-3") 
    	 
        query = new LUBMQuery5(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query5-4") 
    	 
        query = new LUBMQuery6(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query6-1") 
    	 
        query = new LUBMQuery6(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query6-2") 
    	 
        query = new LUBMQuery6(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query6-3") 
    	 
        query = new LUBMQuery6(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query6-4") 
    	 
        query = new LUBMQuery7(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query7-1") 
    	 
        query = new LUBMQuery7(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query7-2") 

        query = new LUBMQuery7(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query7-3") 

        query = new LUBMQuery7(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query7-4") 

        query = new LUBMQuery8(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query8-1") 

        query = new LUBMQuery8(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query8-2") 
        query = new LUBMQuery8(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query8-3") 
        query = new LUBMQuery8(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query8-4") 
        query = new LUBMQuery9(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query9-1") 
        query = new LUBMQuery9(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query9-2") 
        query = new LUBMQuery9(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query9-3") 
        query = new LUBMQuery9(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query9-4") 
        query = new LUBMQuery12(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query12-1") 
        query = new LUBMQuery12(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query12-2") 
        query = new LUBMQuery12(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query12-3") 
        query = new LUBMQuery12(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query12-4") 
        query = new LUBMQuery14(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query14-1") 
        query = new LUBMQuery14(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query14-2") 
        query = new LUBMQuery14(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query14-3") 
        query = new LUBMQuery14(graphRDD)
        query.execute("hdfs://192.168.0.121:9000/data/benchmark/results/GraphX/Query14-4") 
    }
}
