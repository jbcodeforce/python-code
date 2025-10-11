'''
Cross matching to search object from two catalogs
For each source_A in the first catalog, we look through each source_B in the second catalog. 
We calculate the angular distance between each pair of sources, and if the angular distance is less than our search radius, and if that offset, is the lowest we've seen so far, for source_A, we consider that pair a match

Objects are referenced with right ascension and declination.

Source A from  the AT20G Survey http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775
'''
import numpy as np
from .common_fcts import angular_dist, hms2dec, dms2dec, load_bss_catalog, load_superCosmos

catalogA = []


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

def crossmatch(bss_cat, super_cat, max_dist):
    '''
    how many of the bright radio sources in the BSS catalogue have a counterpart in the SuperCOSMOS catalogue
    The list of matches contains tuples of the first and second catalogue object IDs and their distance. The list of non-matches contains the unmatched object IDs from the first catalogue only. Both lists should be ordered by the first catalogue's IDs
    '''
    matches = []
    unmatches = []
    for bss in range(len(bss_cat)):
        RA,D = bss_cat[bss][1],bss_cat[bss][2]
        idx,distance = find_closest(super_cat,RA,D)
        if distance <= max_dist:
           matches.append((bss_cat[bss][0],idx,distance))
        else:
           unmatches.append(bss_cat[bss][0])
    return matches,unmatches


if __name__ == '__main__':
    print("-"*40)
    print("Basic cross matching algorithm")
    print("-"*40)

    print(f"hms2dec(23, 12, 6) = {hms2dec(23, 12, 6)}")   # should be 348.025

    print(f"dms2dec(22, 57, 18) = {dms2dec(22, 57, 18)}")

    print(f"dms2dec(-66, 5, 5.1) = {dms2dec(-66, 5, 5.1)}")

    print(f"angular_dist(21.07, 0.1, 21.15, 8.2) = {angular_dist(21.07, 0.1, 21.15, 8.2)}")

    print(f"angular_dist(10.3, -3, 24.3, -29) = {angular_dist(10.3, -3, 24.3, -29)}")

    bss_cat = load_bss_catalog()
    super_cat = load_superCosmos()
    print(f"find_closest(bss_cat, 175.3, -32.5) = {find_closest(bss_cat, 175.3, -32.5)}")

    print("-"*40)
    print("Cross matching with a distance of 40 arcseconds")
    print("-"*40)
    max_dist = 40/3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(f"First 3 matches= {matches[:3]}")
    print(f"First 3 non-matches= {no_matches[:3]}")

    print(f"Number of non-matches= {len(no_matches)}")

    print("-"*40)
    print("Cross matching with a distance of 5 arcseconds")
    print("-"*40)
    max_dist = 5/3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(f"First 3 matches= {matches[:3]}")
    print(f"First 3 non-matches= {no_matches[:3]}")
    print(f"Number of non-matches= {len(no_matches)}")