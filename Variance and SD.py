import math
data=[10.0,12.0,14.0,16.0,18.0]
def calculate_mean(data):
    return sum(data) / len(data)
def calculate_variance(data,mean):
    squared_diffs = [(x-mean)**2 for x in data]
    return sum(squared_diffs) / len(data)

def calculate_standard_deviation(variance):
    return math.sqrt(variance)

mean = calculate_mean(data)
variance = calculate_variance(data, mean)
standard_deviation = calculate_standard_deviation(variance)
print("Dataset:", data  )
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", f"{standard_deviation:.4f}")