import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)
median = numpy.median(speed)
mode = stats.mode(speed)
std = numpy.std(speed)
var = numpy.var(speed)

print("Average is:  {} \nMedian is: {} \nMode is: {} \nStandard Deviation is: {} \nVariance is: {}".format(mean, median, mode, std, var))