import numpy as np
from scipy import stats
from collections import Counter
from operator import itemgetter

# Creating a 10K normally distributed random array centered around 27K and standard deviation of 15K
input = np.random.normal(27000, 15000, 10000)

# Adding an outlier to see how stats are skewed
input = np.append(input, [1000000000])

# Calculating MEAN using Numpy
print "Mean using Numpy: ", np.mean(input)


# Calculating MEAN manually
def mean_calc(input):
    return float(sum(input)) / len(input)


print "Mean using simple Python: ", mean_calc(input)

# Calculating MEDIAN using Numpy
print "Median using Numpy: ", np.median(input)


# Calculating MEDIAN manually
def median_calc(input):
    sorted_input = sorted(list(input))
    if len(sorted_input) % 2 != 0:
        return sorted_input[len(sorted_input) / 2]
    else:
        return (sorted_input[len(sorted_input) / 2] + sorted_input[len(sorted_input) / 2 - 1]) / 2.0


print "Median using simple Python: ", median_calc(input)

# Calculating MODE using Scipy
print "Mode using Scipy: ", stats.mode([int(x) for x in input])


# Calculating MODE manually
def mode_calc(input):
    int_input = [int(x) for x in input]
    c = Counter(int_input)
    max_count = c.most_common(1)[0][1]

    max_list = [i for i in c.most_common() if i[1] == max_count]

    return sorted(max_list, key=itemgetter(0))[0]


print "Mode using simple Python: ", mode_calc(input)

