'''
Cross matching to search object from two catalogs
For each source_A in the first catalogue, we look through each source_B in the second catalogue. 
We calculate the angular distance between each pair of sources, and if the angular distance is less than our search radius, and if that offset, is the lowest we've seen so far, for source_A, we consider that pair a match

Objects are referenced with 

Source A from  the AT20G Survey http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775
'''

catalogA = []

def angular_distance():
    pass