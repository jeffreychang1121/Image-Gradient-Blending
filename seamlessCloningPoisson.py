'''
  File name: seamlessCloningPoisson.py
  Author:
  Date created:
'''

import numpy as np
from getIndexes import getIndexes
from getCoefficientMatrix import getCoefficientMatrix
from getSolutionVect import getSolutionVect
from reconstructImg import reconstructImg
from scipy.linalg import solve

def seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY):

	targetH, targetW, _ = targetImg.shape

	# get index matrix
	indexes = getIndexes(mask, targetH, targetW, offsetX, offsetY)
	print('Indexes size is %d by %d' % indexes.shape)

	# create coefficient matrix
	coeffA = getCoefficientMatrix(indexes)
	print('CoeffA size is %d by %d' % coeffA.shape)

	# create solution vector (RGB)
	# number of the replacement pixel
	N = mask.sum()
	SolutionVect = np.zeros((N,3))
	for i in range(3):
		# to make sure the shape are consistent
		SolutionVect[:,[i]] = getSolutionVect(indexes, sourceImg[:,:,i], targetImg[:,:,i], offsetX, offsetY)
	print('SolutionVect size is %d by %d' % SolutionVect.shape)
	# seperate into RGB
	red = SolutionVect[:,0]
	green = SolutionVect[:,1]
	blue = SolutionVect[:,2]

	# solve solution
	r = solve(coeffA, red)
	g = solve(coeffA, green)
	b = solve(coeffA, blue)

	# construct final image
	resultImg = reconstructImg(indexes, r, g, b, targetImg)
	print('Image reconstructed')

	return resultImg