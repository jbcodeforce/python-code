# Compute the median of a series 
import numpy as np
from astropy.io import fits
'''
binapprox algorithm to caculate mediam of a list of numbers. The idea behind it is to find the median from the data's histogram. 
'''
def median_bins(data, nb_of_bins):
    '''
    data is a histogram of values
    calculate the mean, standard deviation of all those values
    set the bounds as min and max val: one standard deviation from the mean.
    ignore every  values > max and < min
    return the bins which include the number of elements in data between m - d and m + d, for example
    the first bin is minval <= value < minval + width
    '''
    m = np.mean(data)
    d = np.std(data)
    minval = m - d
    maxval = m + d
    binwidth = (2 * d ) / nb_of_bins
    left_bin = 0
    bins = np.zeros(nb_of_bins)
    # print(minval, maxval, binwidth)
    for v in data:
        if v < minval:
            left_bin +=  1
        elif v < maxval:
            i = int((v - minval) / binwidth)
            bins[i] += 1
    return m,d,left_bin,bins

def median_approx(data, nb_of_bins):
    '''
    Count the number of values that falls into each bin
    Sum the count until reaching the bin if the middle. 
    return the midpoint of the bin
    '''
    mean,delta,left_bin,bins = median_bins(data,nb_of_bins)
    print(mean,delta,left_bin,bins)
    total = left_bin
    N = len(data)
    b = 0
    mid = ( N + 1) / 2
    print(mid)
    for index, bincount in enumerate(bins):
        total += bincount
        if total >= mid:
            b = index
            break
    width = 2 * delta / nb_of_bins
    print(total, b, width)
    median = mean - delta + width * (b + 0.5)
    return median

def load_stack(fnames):
    data = []
    for fname in fnames:
        hdulist = fits.open(fname)
        data.append(hdulist[0].data)
        hdulist.close()
    return data

def  median_bins_fits(images, nb_of_bins):
    return 

if __name__ == '__main__':
  print("---------- Play with some array of numbers -----------")
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 5, 7, 7, 3, 6,1,1], 4))
  print(median_approx([0,1],5))
  print("---------- Play with images -----------")
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)