# PHSX815_Project1

This project is an introduction to the chi-square distribution. A chi-square distribution with k degrees of freedom can be constructed from a set of k independent, randomly generated standard normal (Gaussian) distributions. The chi-square distribution sets the foundation for the chi-squared statistic which is often used as a "goodness of fit" test when comparing data to models. 

Here, I use numpy.random.normal() to produce a set of k Gaussian distributions each of sample size n. The chi-square distribution is then just the sum over the degrees of freedom of the Gaussian distributions. Once the histograms are created using plt.hist(), I use scipy.stats.chi2.pdf() to plot a continuous probability distribution function of a corresponding degree k over each histogram to see how well it fits the data. I then use standard numpy functions like np.mean() and np.var() to calculate the mean and variance of the chi-square distrubution constructed from random Gaussian distributions. The code then outputs The mean and variance of the constructed chi-square distribution as well as the theoretical values.

To run using an iPython terminal, use the following command and input your desired values for each flag:

%run Chi_Squared_Generator.py -sample_size [int n] -DOF [int k] -plot [True/False] -output_file [filename]

Example: %run Chi_Squared_Generator.py -sample_size 1000 -DOF 9 -plot True -output_file H0.txt (Produces the right plot in Figure 2)

Note: Must use all input values for all parameters. I defined default values to be used in case no parameters are provided, however, the code will not run correctly unless all inputs are provided for some reason.
