'''
Distributions
--------------------------------------------------------------------------
References/Links
1. https://numpy.org/doc/stable/reference/random/legacy.html
2. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html
3. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html (Check **kwargs for blending factor)
5. https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html
--------------------------------------------------------------------------
NumPy is also used widely for the various and commonly occurring mathematical and probabilistic distributions and sampling. Combined with PyPlot from Matplotlib, they give a good API for data analysis and interpretation.
Your task would be to sample each of the below six distributions S=1000000 times and then plot the frequency histograms for these samples. You need to create a single figure that has 6 subplots which should be arranged as 1, 2 in the first row, 3, 4 in second row and 5 and 6 in the third row (so 3x2 sub-plot).
For sampling each of them, the input size should be set to S. Larger the sample size, better the estimation of the distribution. You can go through the documentation reference (provided in the links) to find the appropriate parameter to set in the numpy functions.

Some clarifications for the terminology used below:
1. The parameters (a, b, scale, loc, etc) all refer to the statistical variables that are used to adjust the shape of the distributions (check the documentation and the formulae for them for more details as all these distributions are used very commonly)
2. The "values" are the outputs obtained from the distributions, so there will be S values for each of the distributions, and you need to scale them as indicated(by scaling we mean, multiplying by the factor as mentioned)
3. The "range" and "step" are both for the x-axis of the plots, and indicate the range of input, so the histogram will essentially tell you how many of the samples fell in which range
4. Apart from this we also mention the visual appeal of each of the subplots. Read through documentation to figure out how to achieve these.
5. Every subplot needs to have a title corresponding to the distribution being plotted as a histogram.

Use default figure size in pyplot: [6.4, 4.8] inches
(1) Beta. a = 4, b = 20. Multiply the values by 100. Range -5 to 50. Step 1. Color of histogram is red. Title = "Beta"
(2) Exponential. scale = 0.1. Multiply the values by 100. Range -1 to 50. Step 1. Color of histogram is green with 0.5 blending factor. Title = "Exponential"
(3) Gamma. scale = 0.1, shape = 2. Multiply the values by 100. Range -1 to 50. Step 1. Color of histogram is black with blending factor of 0.8 but orientation is horizontal. Title = "Gamma"
(4) Laplace. scale = 0.5, loc = 0. Multiply the values by 100. Range -1 to 50. Step 1. Color is orange. Title = "Laplace"
(5) Normal (Gaussian). loc = 0, scale = 3. Range -10 to 11. Step 1. Default color. Title = "Normal"
(6) Poisson. lam = 3. Range -1 to 11. Step 1. Default color. Title = "Poisson"


Expected output for this is given as expected_plot.png
NOTE:
You may notice, that the autograder is stochastic and possibly may give different marks on different runs. To make this deterministic, set a seed before you do the sampling from distributions.
Autograder may not be always correct. It may give you full score even when partially correct. You need to verify your generated plot.png by comparing against expected_plot.png.
'''

import numpy as np
from matplotlib import pyplot as plt

# Seeding for reproducibility
np.random.seed()

# sampling from each of the six distributions
SAMPLE_SIZE = 1000000
beta = np.random.beta(a=4, b=20, size=SAMPLE_SIZE)
exp = np.random.exponential(scale=0.1, size=SAMPLE_SIZE)
gamma = np.random.gamma(scale=0.1, shape=2, size=SAMPLE_SIZE)
lap = np.random.laplace(scale=0.5, loc=0, size=SAMPLE_SIZE)
nor = np.random.normal(loc=0, scale=3, size=SAMPLE_SIZE)
poi = np.random.poisson(lam=3, size=SAMPLE_SIZE)

# plotting histograms for each of the distributions
plt.subplot(3,2,1)
plt.title("Beta")
plt.hist(100*beta, bins= 55, range=(-5, 50), color="red")

plt.subplot(3,2,2)
plt.title("Exponential")
plt.hist(100*exp, bins= 51, range=(-1, 50), color=("green", 0.5))

plt.subplot(3,2,3)
plt.title("Gamma")
plt.hist(100*gamma, bins= 51, range=(-1, 50), color=("black", 0.8), orientation='horizontal')

plt.subplot(3,2,4)
plt.title("Laplace")
plt.hist(100*lap, bins= 51, range=(-1, 50), color="orange")

plt.subplot(3,2,5)
plt.title("Normal")
plt.hist(nor, bins= 21, range=(-10, 11))

plt.subplot(3,2,6)
plt.title("Poisson")
plt.hist(poi, bins= 12, range=(-1, 11))


# adjust the sub-plots to fit the titles and labels
plt.tight_layout()
# save the plot as plot.png
plt.savefig('plot.png')
