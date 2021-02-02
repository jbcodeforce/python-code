# Compute the median of a series 
import time, numpy as np
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

def running_stats(filenames):
  '''Calculates the running mean and stdev for a list of FITS files using Welford's method.'''
  n = 0
  for filename in filenames:
    hdulist = fits.open(filename)
    data = hdulist[0].data
    if n == 0:
      mean = np.zeros_like(data)
      stdDev = np.zeros_like(data)

    n += 1
    delta = data - mean
    mean += delta/n
    stdDev += delta*(data - mean)
    hdulist.close()

  stdDev /= n - 1
  np.sqrt(stdDev, stdDev)

  if n < 2:
    return mean, None
  else:
    return mean, stdDev



def  median_bins_fits(images, nb_of_bins):
    '''
    calculate  mean, standard deviation, median and bins across the stack of FITS files.
    mean and std are matrix
    '''
    mean,std = running_stats(images)
    # dimensions of the FITS image array
    dim = mean.shape
    left_bin = np.zeros(dim)
    bins = np.zeros((dim[0],dim[1],nb_of_bins))
    bin_width = (2 * std ) / nb_of_bins
    for image in images:
        hdulist = fits.open(image)
        data = hdulist[0].data
        for i in range(dim[0]):
            for j in range(dim[1]):
                value = data[i, j]
                meanImage = mean[i, j]
                stdImage = std[i, j]
                minval = meanImage - stdImage
                maxval = meanImage + stdImage
                if value < minval:
                    left_bin[i,j] += 1
                elif  value <  maxval:
                    binIdx = int((value - minval) / bin_width[i,j])
                    bins[i, j, binIdx] += 1
    return mean, std, left_bin, bins

     

def median_approx_fits(images, nb_of_bins):
    mean,std,left_bin,bins = median_bins_fits(images,nb_of_bins)
    dim = mean.shape
    # Position of the middle element over all files
    N = len(images)
    mid = ( N + 1) / 2
    bin_width = 2*std / nb_of_bins
    # Calculate the approximated median for each array element
    median = np.zeros(dim)   
    for i in range(dim[0]):
        for j in range(dim[1]):    
            count = left_bin[i, j]
            for b, bincount in enumerate(bins[i, j]):
                count += bincount
                if count >= mid:
                    # Stop when the cumulative count exceeds the midpoint
                    break
            median[i, j] = mean[i, j] - std[i, j] + bin_width[i, j]*(b + 0.5)
      
    return median


if __name__ == '__main__':
  print("---------- Play with some array of numbers -----------")
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 5, 7, 7, 3, 6,1,1], 4))
  print(median_approx([0,1],5))
  print("---------- estimate the median of each pixel from a set of astronomy images in FITS files. -----------")
  mean, std, left_bin, bins = median_bins_fits(['../images/image0.fits', '../images/image1.fits', '../images/image2.fits'], 5)
  median = median_approx_fits(['../images/image0.fits', '../images/image1.fits', '../images/image2.fits'], 5)
  print(mean[100,100])
  print(std[100,100])
  print(left_bin[100,100])
  print(bins[100,100,:])
  print(median[100,100])