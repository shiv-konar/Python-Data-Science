import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter
from operator import itemgetter


input = np.random.normal(27000,15000,10000)
input = np.append(input, [1000000000])

print "Mean using Numpy: ", np.mean(input)

def mean_calc(input):
    return float(sum(input)) / len(input)

print "Mean using simple Python: ",mean_calc(input)

print "Median using Numpy: ",np.median(input)

def median_calc(input):
    sorted_input = sorted(list(input))
    if len(sorted_input) % 2 != 0:
        return sorted_input[len(sorted_input) / 2]
    else:
        return (sorted_input[len(sorted_input) / 2] + sorted_input[len(sorted_input) / 2 - 1])/2.0

print "Median using simple Python: ",median_calc(input)

#plt.hist(incomes,50)
#plt.show()

print "Mode using Scipy: ",stats.mode([int(x) for x in input])

def mode_calc(input):
    int_input = [int(x) for x in input]
    c = Counter(int_input)
    max_count = c.most_common(1)[0][1]

    max_list = [i for i in c.most_common() if i[1] == max_count]

    return sorted(max_list, key=itemgetter(0))[0]

print "Mode using simple Python: ", mode_calc(input)
