'''
  File name: getIndexes.py
  Author:
  Date created:
'''
import numpy as np
import copy

def getIndexes(mask, targetH, targetW, offsetX, offsetY):
	# create a new target for indexing
	indexes = np.zeros((targetH, targetW)).astype(int) # index needs to be integer
	maskH, maskW = mask.shape

	# create an additional mask for indexing
	ind = copy.deepcopy(mask).astype(int)
	itr = 1
	for i in range(maskH):
		for j in range(maskW):
			if ind[i,j] == 1:
				ind[i,j] = itr
				itr = itr + 1

	# replace zeros with the indexed mask
	indexes[offsetY:offsetY+maskH, offsetX:offsetX+maskW] = ind

	return indexes