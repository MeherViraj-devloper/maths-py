# Program to calculate Mean, Median and Mode
from collections import Counter

data = [10.0,15.0,20.0,20.0,25.0,30.0,20.0,35.0]

# Calculate Mean
def mean(data):
    return sum(data) / len(data)

# Calculate Median
def median(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

# Calculate Mode
def mode(data):
    count = Counter(data)
    max_freq = max(count.values())
    return [x for x, freq in count.items() if freq == max_freq]

# Display Results
print("Dataset:", data)
print("Mean:", mean(data))
print("Median:", median(data))
print("Mode:", mode(data))
