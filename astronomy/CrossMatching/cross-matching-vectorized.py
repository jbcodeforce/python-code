'''
Same Cross matching but with pre-computation of RA,D for each catalog objects
The improvement is in not to compute radian all the time, but compute upfront.
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
                

def crossmatch(cat1, cat2, max_dist):
    '''
    catalog is a list of (RA,declination) no index
    '''
    matches = []
    unmatches = []
    startT = time.perf_counter()
    max_dist= np.radians(max_dist)
    cat1 = np.radians(cat1)
    cat2 = np.radians(cat2)
    ra2s = cat2[:, 0]
    dec2s = cat2[:, 1]
    for idx1,(RA1,D1) in enumerate(cat1):
        dists = angular_dist(RA1, D1, ra2s, dec2s)
        minDistance = np.min(dists)
        if minDistance <= max_dist:
           matches.append((idx1,np.argmin(dists),np.degrees(minDistance)))
        else:
           unmatches.append(idx1)
    return matches,unmatches, (time.perf_counter() - startT)

if __name__ == '__main__':
 
  ra1, dec1 = np.radians([180, 30])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  cat2 = np.radians(cat2)
  ra2s, dec2s = cat2[:,0], cat2[:,1]
  dists = angular_dist(ra1, dec1, ra2s, dec2s)
  print(np.degrees(dists))

  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)