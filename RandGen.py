from random import *

X = 0
I = 1
L = 2
T = 3
E = 4
G = 5


def genMap():

	newMap = []
	
	while(len(newMap) < 10):
		newList = []
		while(len(newList) < 10):
			pos = randint(0, 5)
			if isValid(len(newMap), len(newList), pos, newMap, newList) > -1:
				newList.append(pos)
			print(newList)
		newMap.append(newList)



	return newMap


def isValid(x, y, val, newMap, newList):
	if val == X:
		# Ensure that no adjacent is G (5) 
		# Will not allow roads to nowhere
		# Rotation does not affect X
		if (x==0 or y==0 or x == 9 or y == 9):
			return -1
		if len(newMap) > 0 and newMap[x-1][y] == G:
			return -1
		if len(newList) > 0 and newList[y-1] == G:
			return -1

	elif val == I:
		# Along right or left wall
		if x == 0 or x == 9:
			# In a corner, can't have this tile
			if y == 0 or y == 9:
				return -1
			else: # just on a wall, display normally: |
				return 0
		elif y == 0 or y == 9: # On top or bottom row, rotate 90
			return 1

	"""elif newMap[x][y] == L:

	elif newMap[x][y] == T:

	elif newMap[x][y] == E:	

	else: # G
"""
	return 0

def main():

	newMap = genMap()
	for i in range(0, 10):
		print(newMap[i])

if __name__ == "__main__":
	main()