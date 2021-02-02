'''
Cross matching to search object from two catalogs
For each source_A in the first catalogue, we look through each source_B in the second catalogue. 
We calculate the angular distance between each pair of sources, and if the angular distance is less than our search radius, and if that offset, is the lowest we've seen so far, for source_A, we consider that pair a match

Objects are referenced with 

Source A from  the AT20G Survey http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775
'''
import numpy as np
from astropy.io import fits



catalogA = []

def angular_dist(a1,d1, a2, d2):
    '''
     calculates the angular distance between any two points on the celestial sphere given their right ascension (a) and declination (d)
    '''
    # transform to radians
    ar1 = np.radians(a1)
    ar2 = np.radians(a2)
    dr1 = np.radians(d1)
    dr2 = np.radians(d2)
    p1 = np.sin( np.abs( dr1 - dr2 ) /2 )**2
    p2 = np.cos(dr1) * np.cos(dr2) * np.sin( np.abs( ar1 - ar2 ) /2 ) **2
    return np.degrees(2 * np.arcsin( np.sqrt(  p1 + p2 )))
                

def hms2dec(h, m, s):
    '''
    convert hour minutes second to declination
    '''
    return 15 * (h +  m / 60 + s / 3600)

def dms2dec(d,m,s):
    '''
    convert Degrees minutes second to declination
    '''
    if ( d < 0):
        v = (d -  m / 60 - s / 3600)
    else:
        v = (d +  m / 60 + s / 3600)
    return  v

def import_bss():
    '''
    Load AT20G bright source sample survey first
    1: Object catalogue ID number (sometimes with an asterisk)
    2-4: Right ascension in HMS notation
    5-7: Declination in DMS notation
    8-: Other information, including spectral intensities
    return a list of tuples containing the object's ID (an integer) and the coordinates in degrees.
    '''
    data = np.loadtxt('../data/AT20G/table2.dat', usecols=range(1, 7))
    tuples = []
    for i in range(len(data)):
        tuples.append((i+1,hms2dec(data[i][0],data[i][1],data[i][2]),dms2dec(data[i][3],data[i][4],data[i][5])))
    return tuples

def import_super():
    '''
    superCOSMOS all-sky catalogue is a catalogue of galaxies generated from several visible light surveys.
    1: Right ascension in decimal degrees
    2: Declination in decimal degrees
    3: Other data, including magnitude and apparent shape
    return a list of tuples containing the object's ID (an integer) and the coordinates in degrees.
    '''
    data = np.loadtxt('../data/AT20G/super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
    tuples = []
    for i in range(len(data)):
        tuples.append((i+1,data[i][0],data[i][1]))
    return tuples

if __name__ == '__main__':
  # The first example from the question
  print(hms2dec(23, 12, 6))

  # The second example from the question
  print(dms2dec(22, 57, 18))

  # The third example from the question
  print(dms2dec(-66, 5, 5.1))

  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  print(angular_dist(10.3, -3, 24.3, -29))

  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)