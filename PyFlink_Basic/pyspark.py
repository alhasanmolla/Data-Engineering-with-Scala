from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# SparkContext সেটআপ
sc = SparkContext(appName="WordCountExample")
ssc = StreamingContext(sc, batchDuration=5)  # ব্যাচ ইন্টারভ্যাল ৫ সেকেন্ড

# ডাটা সোর্স (এখানে একটি simulated RDD ব্যবহার করা হচ্ছে)
rddQueue = [
    sc.parallelize(["Apache Spark is a unified analytics engine", 
                    "It provides high-level APIs in Java, Scala, Python, and R",
                    "PySpark allows you to use Python to write Spark programs"])
]

# Streaming RDD
input_stream = ssc.queueStream(rddQueue)

# ওয়ার্ড স্প্লিট এবং কাউন্ট
words = input_stream.flatMap(lambda line: line.split(" ")) \
                    .map(lambda word: (word, 1)) \
                    .reduceByKey(lambda x, y: x + y)

# কনসোলে আউটপুট
words.pprint()

# স্ট্রিমিং শুরু করা এবং শেষ করা
ssc.start()  # স্ট্রিমিং প্রসেসিং শুরু
ssc.awaitTermination()  # শেষ না হওয়া পর্যন্ত অপেক্ষা
