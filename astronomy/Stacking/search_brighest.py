'''
Search brighest point in a set of image, using stacking technics on the mean of pixels in the same position
TO DO: to tune when we have image
'''
from astropy.io import fits
import numpy as np
import sys, time

def load_stack(fnames):
    '''
    return a matrix of pixels for each image
    '''
    data = []
    for fname in fnames:
        hdulist = fits.open(fname)
        # hdulist[0].data is a matrix (may be 200x200 pixels)
        data.append(hdulist[0].data)
        hdulist.close()
    return data


def raw_mean_fits(fnames):
  start = time.perf_counter()
  data = load_stack(fnames)
  nb_stack = len(data) 
  nb_col = len(data[0][0])  # 4
  nb_row = len(data[0])  # 3
  memused = (sys.getsizeof(data) / 1024)
  for r in range(0,nb_row):
      for c in range(0,nb_col):
          cell = []
          for s in range(0,nb_stack):
              cell.append(data[s][r][c])
          data[0][r][c] = np.mean(cell)
  return data[0],time.perf_counter() - start, memused


def median_fits(fnames):
  '''
  Stack the images loaded from folder, and compute the median of the bright (3nd dimension)
  return the mediam, the time to compute it, and the memory used for the data
  '''
  start = time.perf_counter()
  data = load_stack(fnames)
  stack = np.dstack(data)
  median = np.median(stack, axis=2)
  memused = (stack.nbytes / 1024)
  runtime =  time.perf_counter() - start
  return data[0],runtime,memused

if __name__ == '__main__':
  
  # Test your function with examples from the question
  data,t,m  = raw_mean_fits(['../images/image0.fits', '../images/image1.fits', '../images/image2.fits'])
  print(data[100,100],t,m)
  data,t,m  = median_fits(['../images/image0.fits', '../images/image1.fits', '../images/image2.fits','../images/image3.fits', '../images/image4.fits'])
  print(data[100, 100],t,m)

  # Expected results 
  # 0.017356586332122486 0.7255405000178143 0.1015625
  # 0.012338057160377502 0.2552497999276966 1562.5

  # You can also plot the resulting image:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()