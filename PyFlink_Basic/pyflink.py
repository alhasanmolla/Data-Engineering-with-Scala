from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import FlatMapFunction
from pyflink.common import Types

# Initialize the environment
env = StreamExecutionEnvironment.get_execution_environment()

# Define the data source (a list of sentences)
input_data = env.from_collection([
    "Apache Flink is a framework and distributed processing engine",
    "It is used for stateful computations over unbounded and bounded data streams",
    "PyFlink allows you to use Python to write Flink programs"
])

# Define a simple FlatMapFunction to split lines into words
class SplitWords(FlatMapFunction):
    def flat_map(self, value, collector):
        for word in value.split():
            collector.collect((word, 1))

# Apply transformations: split words, and sum counts by word
words = input_data.flat_map(SplitWords(), output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
word_counts = words.key_by(lambda x: x[0]) \
                   .sum(1)

# Print the output
word_counts.print()

# Execute the program
env.execute("Word Count Example")
