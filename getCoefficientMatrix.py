'''
  File name: getCoefficientMatrix.py
  Author:
  Date created:
'''
import numpy as np

def getCoefficientMatrix(indexes):
	# number of the replacement pixel
	N = indexes.max()
	coeffA = np.eye(N)*4

	# coordinate of the matrix where is nonzero
	[row, col] = np.where(indexes>0)

	# loop through the mask where index > 0
	for i in range(N):
		# i represents the ith row of the coeffA
		# column represents the index
		r = row[i]
		c = col[i]

		# if indexed pixel around, mark -1 according to its coordinate
		# move downward
		if indexes[r+1, c] > 0:
			coeffA[i, indexes[r+1, c]-1] = -1
		# move upward
		if indexes[r-1, c] > 0:
			coeffA[i, indexes[r-1, c]-1] = -1
		# move right
		if indexes[r, c+1] > 0:
			coeffA[i, indexes[r, c+1]-1] = -1
		# move left
		if indexes[r, c-1] > 0:
			coeffA[i, indexes[r, c-1]-1] = -1

	return coeffA
