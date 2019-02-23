'''
  File name: getSolutionVect.py
  Author:
  Date created:
'''
import numpy as np
from scipy.signal import convolve2d

def getSolutionVect(indexes, source, target, offsetX, offsetY):
	# number of the replacement pixel
	N = indexes.max()

	# coordinate of the matrix where is nonzero
	[row, col] = np.where(indexes > 0)

	# laplacian
	m = [[0,-1,0], [-1,4,-1], [0,-1,0]]
	new_source = convolve2d(source, m, 'same')

	# coordinate of the source
	rs = row - offsetY
	cs = col - offsetX
	# flatten the pixels to N x 1
	SolVectorb = new_source[rs,cs].reshape(-1,1)

	# check if out of boundary, add coefficient value
	for i in range(N):
		r = row[i]
		c = col[i]
		# up
		if indexes[r-1, c] == 0:
			top = target[r-1, c]
		else:
			top = 0
		# down
		if indexes[r+1, c] == 0:
			down = target[r+1, c]
		else:
			down = 0
		# left
		if indexes[r, c-1] == 0:
			left = target[r, c-1]
		else:
			left = 0
		# right
		if indexes[r, c+1] == 0:
			right = target[r, c+1]
		else:
			right = 0

		SolVectorb[i] = SolVectorb[i] + top + down + left + right

	return SolVectorb
