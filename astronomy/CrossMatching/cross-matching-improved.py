'''
Cross matching to search object from two catalogs
For each source_A in the first catalog, we look through each source_B in the second catalog. 
We calculate the angular distance between each pair of sources, and if the angular distance is less than our search radius, and if that offset, is the lowest we've seen so far, for source_A, we consider that pair a match

Objects are referenced with right ascension and declination.

Source A from  the AT20G Survey http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775
'''
import numpy as np
import time

def angular_dist(ar1,dr1, ar2, dr2):
    '''
     calculates the angular distance between any two points on the celestial sphere given 
     their right ascension (a) and declination (d)
    '''
    p1 = np.sin( np.abs( dr1 - dr2 ) /2 )**2
    p2 = np.cos(dr1) * np.cos(dr2) * np.sin( np.abs( ar1 - ar2 ) /2 ) **2
    return 2 * np.arcsin( np.sqrt(  p1 + p2 ))
                

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
    data = np.loadtxt('../data/AT20G/bss.dat', usecols=range(1, 7))
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

def find_closest(catalog,RA,D):
    '''
    takes a catalogue and the position of a target source (a right ascension and declination) 
    and finds the closest match for the target source in the catalogue.
    return the ID of the closest object and the distance to that object
    '''
    minDistance = np.inf
    idx_obj = 0
    for i in range(len(catalog)):
        distance = angular_dist(RA,D,catalog[i][1],catalog[i][2])
        if distance < minDistance:
            idx_obj = catalog[i][0]
            minDistance = distance
    return idx_obj, minDistance

def crossmatch(bss_cat, super_cat, max_radius):
    '''
    how many of the bright radio sources in the BSS catalogue have a counterpart in the SuperCOSMOS catalogue
    The list of matches contains tuples of the first and second catalogue object IDs and their distance. The list of non-matches contains the unmatched object IDs from the first catalogue only. Both lists should be ordered by the first catalogue's IDs
    '''
    matches = []
    unmatches = []
    start = time.perf_counter()
    max_radius = np.radians(max_radius)
    # Extract only RA and Declination
    cat1=np.asarray(bss_cat)[:,1:3]
    cat2=np.asarray(super_cat)[:,1:3]
    # Convert coordinates to radians
    cat1 = np.radians(cat1)
    cat2 = np.radians(cat2)
    asc_dec = np.argsort(cat2[:,1])
    cat2_ordered = cat2[asc_dec]
    for bss, (ra1, dec1) in enumerate(cat1):
        minDistance = np.inf
        min_id2 = None
        max_dec = dec1 + max_radius
        for id2, (ra2, dec2) in enumerate(cat2_ordered):
            if dec2 > max_dec:
                break
            distance = angular_dist(ra1, dec1, ra2, dec2)
            if distance < minDistance:
                min_id2 = asc_dec[id2]
                minDistance = distance
        if min_id2 <= max_radius:
            matches.append(bss,min_id2,np.degrees(minDistance))
        else:
            unmatches.append(bss)
    time_taken = time.perf_counter() - start
    return matches,unmatches, time_taken


if __name__ == '__main__':
  ''' 
  print(hms2dec(23, 12, 6))   # should be 348.025

  print(dms2dec(22, 57, 18))

  print(dms2dec(-66, 5, 5.1))

  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  print(angular_dist(10.3, -3, 24.3, -29))
  '''
  bss_cat = import_bss()
  super_cat = import_super()
  # print(bss_cat)
  # print(super_cat)
  print(find_closest(bss_cat, 175.3, -32.5))

  max_dist = 40/3600
  matches, no_matches, timer = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
  print(timer)
  max_dist = 5/3600
  matches, no_matches, timer = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
  print(timer)