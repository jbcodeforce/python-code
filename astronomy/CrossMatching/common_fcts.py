import numpy as np

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

def load_bss_catalog():
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
    print(f"Number of elements in BSS catalog= {len(tuples)}")
    print(f"First 10 elements in BSS catalog= {tuples[:10]}")
    print("-"*40)
    return tuples

def load_superCosmos():
    '''
    superCOSMOS all-sky catalog is a catalog of galaxies generated from several visible light surveys.
    1: Right ascension in decimal degrees
    2: Declination in decimal degrees
    3: Other data, including magnitude and apparent shape
    return a list of tuples containing the object's ID (an integer) and the coordinates in degrees.
    '''
    data = np.loadtxt('../data/AT20G/super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
    tuples = []
    for i in range(len(data)):
        tuples.append((i+1,data[i][0],data[i][1]))
    print(f"Number of elements in superCosmos catalog= {len(tuples)}")
    print(f"First 10 elements in superCosmos catalog= {tuples[:10]}")
    print("-"*40)
    return tuples