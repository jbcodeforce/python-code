# Compute the median of a series 
import numpy as np

def median_bins(data, nb_of_bins):
    '''
    calculate the mean, standard deviation and the bins which include data between m - d and m + d 

    '''
    m = np.mean(data)
    d = np.std(data)
    minval = m - d
    maxval = m + d
    binwidth = (2 * d ) / nb_of_bins
    left_bin = 0
    bins = np.zeros(nb_of_bins)
    for v in data:
        if v < minval:
            left_bin +=  1
        elif v < maxval:
            i = int((v - minval) / binwidth)
            bins[i] += 1
    return m,d,left_bin,bins

def median_approx(data, nb_of_bins):
    '''
    sum the count the number of value of each bins up to the middle element.

    also return the mean
    '''
    mean,delta,left_bin,bins = median_bins(data,nb_of_bins)
    print(mean,delta,left_bin,bins)
    total = left_bin
    N = len(data)
    b = 0
    mid = ( N + 1) / 2
    for index, bincount in enumerate(bins):
        total += bincount
        if total >= mid:
            b = index
            break
    width = (2 * delta) / nb_of_bins
    print(total, b,width)
    median = mean - delta + width * (b + 0.5)
    return median
    

if __name__ == '__main__':
  # Run your functions with the first example in the question.
  # print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 5, 7, 7, 3, 6,1,1], 4))
  print(median_approx([0,1],5))