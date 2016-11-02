This LUMB implementation based on GraphX was developed with Eclipse (Luna) and 
Scala-IDE Plugin. In order to open the project file, those development tools 
are required. Compiling and executing executables can be done in Linux terminal.

To build the project, run
$ sbt package

To execute the project, run
$ spark-submit --class main.scala.Main --master local[4] target/scala-2.10/spark-lubm-benchmark_2.10-1.0.jar
