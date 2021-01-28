# Python programming for astronomy.

The [dockerfile]() defines a python env with astropy, matplotlib, numpy,scipy...

## Pulsars

The goal is to answer: *how many pulsars are detected in images taken with the Murchison Widefield Array telescope?* 
The array telescope, detects radio emission at frequencies between 80 and 300 megahertz. It has a very large field of view, which means it's great for doing large survey projects.
Images has using a grayscale to measure the flux density of emission from astronomical objects. Black is high flux density and gray is the background noise. Radio frequencies don't have color. These color maps are just used to accentuate different aspects of the intensity scale.

In radio astronomy, flux density is measured in units of Janskys, which is equivalent to 10 to the power of -26 watts per square meter per hertz.

  <img src="https://latex.codecogs.com/gif.latex?1&space;Jy&space;=&space;10^{-26}\frac{W}{m^{2}.Hz}" title="1 Jy = 10^{-26}\frac{W}{m^{2}.Hz}" />)

Astronomy images are usually stored in a file format called FITS, and to view them you can download software like DS9 or use an online tool like [Aladin](https://aladin.u-strasbg.fr/).

We typically call something a detection if the flux density is more than five standard deviations higher than the noise in the local region.

To search from non-detection, a special approach is used called **Stacking** which  measures the statistical properties of a population we can't detect. Stacking works because the noise in a radio image is roughly random, with a Gaussian distribution centered on zero. When you add regions of an image that just have noise, the random numbers cancel out. But when you add regions of an image in which there are signals, the signals add together, increasing what we call the signal to noise ratio.

Introduction to Pulsars (from CSIRO) Hobbs, M. (n.d.) from [http://www.atnf.csiro.au/outreach/education/everyone/pulsars/index.html](http://www.atnf.csiro.au/outreach/education/everyone/pulsars/index.html)

Pulsar Properties (from NRAO, advanced) National Radio Astronomy Observatory. (2010) from [http://www.cv.nrao.edu/course/astr534/Pulsars.html](http://www.cv.nrao.edu/course/astr534/Pulsars.html)

## Calculating the mean / median stack of a set of FITS images

In Flexible Image Transport System (FITS) the image is stored in a numerical array, which we can load into a NumPy array. Opening a FITS file in `astropy` returns a HDU (Header/Data Unit) list. Each HDU stores headers and (optionally) image data. Here is a program to find the point in the image with the maximum intensity:

```python
from astropy.io import fits
def search_brightest_pixel(fname):
  hdulist = fits.open(fname)
  data = hdulist[0].data
  nb_row,nb_col = data.shape
  max = 0
  x , y = (0,0)
  for r in range(0,nb_row):
    for c in range(0,nb_col):
      if data[r][c] > max :
          x = r
          y = c
          max = data[r][c]
  return x,y
```

A better approach is to use the median (the middle of the sorted data set), as the mean is easily skewed by outliers. But getting median could get computational intensive and consuming a lot of memory as calculating the median requires all the data to be in memory at once. This is an issue in typical astrophysics calculations, which may use hundreds of thousands of FITS files. To compute the median we can use the statistics library, or the following:

```python
fluxes = [17.3, 70.1, 22.3, 16.2, 20.7]
fluxes.sort()
mid = len(fluxes)//2
median = fluxes[mid]
# or for an even number of elements
median = (fluxes[mid - 1] + fluxes[mid])/2
```

or using `numpy`: 

```python
data = load_stack(fnames)
stack = np.dstack(data)
median = np.median(stack, axis=2)
```

To avoid loading all the data in memory, we can use the [binapprox algorithm](http://www.stat.cmu.edu/~ryantibs/papers/median.pdf) to approximate the current median. The idea behind it is to find the median from the data's histogram.
Starting from the left, if we sum up the counts in the histogram bins until we get to just over the expected mediam then we know the last bin we added must have contained the median. In fact it is better to search in bins around the standard devision of the mean. See [Stacking/binapprox.py](https://github.com/jbcodeforce/python-code/blob/master/astronomy/Stacking/binapprox.py) code.

## AGN: Active Galactic Nucleus

Our eyes can only detect light and the visible part of the electromagnetic spectrum.  Galaxy has Xray, visible and radio waves. At the center of the galaxy is a black hole, which has a huge impact on the galaxy's growth and formation. In cases where there is a lot of gas in the central region of the galaxy, this material can be accreted on to the black hole via an Accretion Disk, releasing a lot of energy in the process. This is what we call, an Active Galactic Nucleus. The radiation produced by the AGN is so bright that it can outshine the entire galaxy, producing far more energy than all of the galaxy's stars combined. It may form huge jets of strong magnetic fields emanating out from around the black hole. Here is an image of combined wave length from visible, xray and radio

![Galaxy in 3 wave lengths](./images/galaxy-3w.png)

The material that accretes onto a black hole produce x-rays, because particle are becoming very hot. We can assess the presence of supermassive black hole by measuring powerful jets coming from a compact core, rapid changes in the luminosity of the galaxy nucleus, very high speed orbital motions of stars in the galactic nucleus.

## Cross-matching

When investigating astronomical objects, like active galactic nuclei (AGN), astronomers compare data about those objects from different telescopes at different wavelengths. This requires positional cross-matching to find the closest counterpart within a given radius on the sky.

To create a catalog of object from survey images, the source-finding software uses the same technics of going through all the pixels and find peaks that are statistically significant. 

How to calculate distance in the sky? Two objects in the same image are not in the same plan, we can compute the angular distance but they may be far aways on those line.

