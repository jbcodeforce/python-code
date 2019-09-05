import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.stats import norm

'''
Present the gaussian curve and its area, and play with probability
'''



def parseArguments():
    mu = 998.8 
    sigma = 73.10
    lowerBound = 900
    upperBound = 1100
    if len(sys.argv) > 1:
        for idx in range(1, len(sys.argv)):
            arg=sys.argv[idx]
            if arg == "--mean":
                mu=sys.argv[idx+1]
            elif arg == "--sigma":
                sigma=sys.argv[idx+1]
            elif arg == "--lower":
                lowerBound=sys.argv[idx+1]
            elif arg == "--upper":
                upperBound=sys.argv[idx+1]
    return (mu,sigma,lowerBound,upperBound)
    




if __name__ == "__main__":
    (mu,sigma,lowerBound,upperBound)=parseArguments()
    # calculate the z-transform
    z1 = ( lowerBound - mu ) / sigma
    z2 = ( upperBound - mu ) / sigma
    x = np.arange(z1, z2, 0.001) # range of x in spec
    x_all = np.arange(-10, 10, 0.001) # entire range of x, both in and out of spec
    # mean = 0, stddev = 1, since Z-transform was calculated
    y = norm.pdf(x,0,1)
    y2 = norm.pdf(x_all,0,1)
    # build the plot
    fig, ax = plt.subplots(figsize=(9,6))
    plt.style.use('fivethirtyeight')
    ax.plot(x_all,y2)

    ax.fill_between(x,y,0, alpha=0.3, color='b')
    ax.fill_between(x_all,y2,0, alpha=0.1)
    ax.set_xlim([-4,4])
    ax.set_xlabel('# of Standard Deviations Outside the Mean')
    ax.set_yticklabels([])
    ax.set_title('Normal Gaussian Curve')

    plt.savefig('normal_curve.png', dpi=72, bbox_inches='tight')
    plt.show()