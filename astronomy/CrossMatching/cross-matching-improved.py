'''
Cross matching to search object from two catalogs
For each source_A in the first catalog, we look through each source_B in the second catalog. 
We calculate the angular distance between each pair of sources, and if the angular distance is less than our search radius, and if that offset, is the lowest we've seen so far, for source_A, we consider that pair a match

Objects are referenced with right ascension and declination.

Source A from  the AT20G Survey http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775
'''
import numpy as np
import time
from common_fcts import angular_dist, load_bss_catalog, load_superCosmos

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

    bss_cat = load_bss_catalog()
    super_cat = load_superCosmos()

    print(f"find_closest(bss_cat, 175.3, -32.5) = {find_closest(bss_cat, 175.3, -32.5)}")

    print("-"*40)
    print("Cross matching with a distance of 40 arcseconds")
    print("-"*40)
    max_dist = 40/3600
    matches, no_matches, timer = crossmatch(bss_cat, super_cat, max_dist)
    print(f"First 3 matches= {matches[:3]}")
    print(f"First 3 non-matches= {no_matches[:3]}")
    print(f"Time taken= {timer} seconds")
    print(f"Number of non-matches= {len(no_matches)}")

    print("-"*40)
    print("Cross matching with a distance of 5 arcseconds")
    print("-"*40)
    max_dist = 5/3600
    matches, no_matches, timer = crossmatch(bss_cat, super_cat, max_dist)
    print(f"First 3 matches= {matches[:3]}")
    print(f"First 3 non-matches= {no_matches[:3]}")
    print(f"Number of non-matches= {len(no_matches)}")
    print(f"Time taken= {timer} seconds")