import org.apache.spark._
import org.apache.hadoop.fs._
import org.apache.spark.SparkContext._
import org.apache.spark.sql._
import org.apache.log4j._

// time utils in java
import java.time._
import java.time.format._
import java.time.temporal._

// scala max function
import scala.math.max

  
/** A function that splits a line of input into (IP, Time, url) **/
def parseLine(line: String) = {
    // split by empty space
    val fields = line.split(" ")
    val ip = fields(2).split(":")(0)
    val timestamp = fields(0)
    val url = fields(12)

    (ip, timestamp, url)

}

// take a compactBuffer of tuples, which represents all visits in a session
// return a tuple with 2 elements.
// In the returned tuple:
//      first element is the ip
//      second element is time duration in seconds
def calculateTimeDifference(buffer: List[Tuple3[String, String, String]]): Tuple2[String, Long] = {
     var tuples = buffer.sortBy(x => x._2)       // sortby visiting time
     if (tuples.length == 1) {
         (tuples(0)._1, 1)    // if the session only have one visit, we will just give a 1s visited time

     } else {
         val start_time = tuples(0)._2
         val end_time = tuples.last._2

         // now we have to some string manipulations to get the time difference
         val start_date = start_time.split("T")(0)
         val end_date = end_time.split("T")(0)

         val start_hour_min_second = start_time.split("T")(1).split("\\.")(0)
         val end_hour_min_second = end_time.split("T")(1).split("\\.")(0)

         val p = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss") //note months are MM

         val t1 = LocalDateTime.parse(start_date + " " + start_hour_min_second, p)
         val t2 = LocalDateTime.parse(end_date + " " + end_hour_min_second, p)

         val timeDiff = t1.until(t2, ChronoUnit.SECONDS)
         if (timeDiff == 0) {
             (tuples(0)._1, 1)
         } else {
             (tuples(0)._1, timeDiff)
         }
     }
}

def calculateUniqueURL(buffer: List[Tuple3[String, String, String]]): Tuple2[String, Int] = {
    var s: Set[String] = Set()
    for (t <- buffer) {
        s += t._3       // add the url to the set
    }
    (buffer(0)._1, s.size)
}



val data = sc.textFile("/home/ruijie/Desktop/projects/WeblogChallenge/data/2015_07_22_mktplace_shop_web_log_sample.log")

// convert the data to tuples
val rdd = data.map(parseLine)


// then we need to do group by operations by id.
// after that, we will do some counting
val sessions = rdd.groupBy(tuple => tuple._1)   // tuple._1 is the ip. First groupby ip
sessions.take(1).foreach(println)
// now we sort by time, and caculate the average session time
val sessionDurations = sessions.map(x => x._2.toList).map(calculateTimeDifference)

// now calculate the average of the session durations
sessionDurations.take(1).foreach(println)
val sumOfDuration = sessionDurations.map(x => (x._2, 1)).reduce((x,y) => (x._1 + y._1, x._2 + y._2))
val meanDurationSeconds = sumOfDuration._1 / sumOfDuration._2              // the duration of the sessions
val meanDurationMinutes = meanDurationSeconds / 60
println(s"the average duration of the sessions is $meanDurationSeconds seconds, which is roughly $meanDurationMinutes minutes")

// now let us count the urls
val urlsBySessions = sessions.map(x => x._2.toList).map(calculateUniqueURL)

// now let us calculate the average url hits per session and the max url for a session
val sumOfURL = urlsBySessions.map(x => (x._2, 1)).reduce((x, y) => (x._1 + y._1, x._2 + y._2))
val meanURLCount = sumOfURL._1 / sumOfURL._2
val maxURLCount = urlsBySessions.map(x => x._2).reduce((x, y) => max(x, y))
println(s"The average url counts per session is $meanURLCount, and the max url count in a session is $maxURLCount")

// now let us calculate the most active ip
val maxTimeSession = sessionDurations.reduce((x, y) => if (x._2 > y._2) x else y)
val mostActiveIp = maxTimeSession._1
val mostActiveTimeDuration = maxTimeSession._2
val mostActiveTimeDurationHours = mostActiveTimeDuration / 3600
println(s"The max session has IP $mostActiveIp, with the duration is $mostActiveTimeDuration seconds, which is roughly $mostActiveTimeDurationHours hours")