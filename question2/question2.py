# Using any image available in the dgsamples pypi package:
#
# 1. retrieve all bands from the image
# 2. compute the covariance matrix of the image bands
# 3. plot the covariance matrix and save the figure to disk in
#    png format

# You may use the initial few lines of code below if you like

# I'm assuming that each of the 8 sheafs is a separate band
# I averaged over one of the dimensions; the answer should be the same if averaged over the other

import dgsamples
from osgeo import gdal
import numpy as np
# I had to be tricky for this to run online.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

o = gdal.Open(dgsamples.bayou_chip.extract_test)

d = o.ReadAsArray()

covMat = np.zeros([8,8,246], dtype = float)

for n in range(0,245):
	covMat[:,:,n] = np.cov(d[:,:,n])

covAvg = np.average(covMat, axis = 2)
fig = plt.figure()
covMatplot = plt.pcolor(covAvg)
plt.show(covMatplot)
fig.savefig('Image_band_Covariance.png')

