# -*- coding: utf-8 -*-
"""
Created on Monday March 1 14:20:16 2021

@author: d338c921
"""
# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: \n -sample_size [Std. Normal disribution sample size] \n -DOF [degrees of freedom or # of Gaussian distributions to be used to construct the chi-square dist.] \n -plot [True/False: show histogram?] \n -output_file [filename]")
        print
        sys.exit(1)

  
    # default number of experiments
    sample_size = 100
    
    #default degrees of freedom
    DOF = 2
    
    #default histogram plot
    plot = False

    # output file defaults
    doOutputfile = False

    # read the user-provided values from the command line (if there)
    if '-sample_size' in sys.argv:
        p = sys.argv.index('-sample_size')
        sample_size = int(sys.argv[p+1])
    if '-DOF' in sys.argv:
        p = sys.argv.index('-DOF')
        DOF = int((sys.argv[p+1]))
    if '-plot' in sys.argv:
        p = sys.argv.index('-plot')
        plot = sys.argv[p+1]
    if '-output_file' in sys.argv:
        p = sys.argv.index('-output_file')
        output_file = str(sys.argv[p+1])
        doOutputFile = True

    #create the standard normal distributions according to the specified sample size/degrees of freedom
    data_gaussian = np.random.normal(0, 1, size= (sample_size, DOF))
    #create the chi_square distribution from the gaussian distributions; sum of the squares over the # of DOF
    data_chi = np.sum(data_gaussian**2, axis = 1)

    #output the file to given filename if provided; else print the data
    if doOutputFile:
        np.savetxt(output_file, data_chi)
    else:
        print(data_chi)

    #create histogram of the data_chi if plot = True
    if plot:
        plt.figure()
        #plot the data_chi histogram
        n, bins, patches = plt.hist(data_chi, 50, density=True, color='red', alpha=0.75, label = "Constructed $\chi^2$ Distribution")
        #plot the theoretical chi-distribution
        x = np.linspace(0, np.max(np.round(bins)), 10000)
        plt.plot(x, stats.chi2.pdf(x, df=DOF), color='b', label = "$\chi^2$ PDF w/ " + str(DOF) + " degrees of freedom")
        # plot formating options
        plt.xlabel('Number')
        plt.ylabel('Probability')
        plt.title('Chi-Square Distribution')
        plt.grid(True)
        plt.legend()
        plt.show()
        
    #calculate then print: mean, variance, ...
    mean = np.mean(data_chi)
    plt.axvline(mean, linestyle = "--", label = "Calculated Mean")
    plt.legend()
    print("The mean of this data set = " + str(mean))
    print("Theoretically, the mean should be equal to the number of degrees of freedom = " + str(DOF) + "\n")
    variance = np.var(data_chi)
    print("The variance of this data set = " + str(variance))
    print("Theoretically, the variance should be equal to double the number of degrees of freedom = " + str(2*DOF))