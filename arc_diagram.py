"""
Very simple application  for vizualizing the arc diagrams
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Arc, Circle
import numpy as np
from sys import argv


def _arc(i, j, width=1):
	"""
	Creating a single arc from i to j
	"""
	# arc = Wedge(((i+j)/2., 0), (abs(i-j)/2.), 5, 175, linewidth=width, edgecolor='black', fill=False, linestyle='--')
	return Arc(((i+j)/2., 0), abs(i-j), abs(i-j), 0, 0, 180, linewidth=width, edgecolor='black', fill=False, linestyle='--')

def _circle(i, r=.05):
	"""
	Create a small filled circle with center at (i, 0) and radius r
	"""
	return Circle((i, 0), r, fill=True, color='black')

def arc_diagram(x):
	ax = plt.gca()
	plt.plot([0, len(x)-1], [0, 0], color='black', linewidth=.7)
	plt.axis('off')
	for i in range(len(x)):
		j = x[i]
		ax.add_patch(_circle(i))
		if j != -1:
			c = _arc(i, j)
			ax.add_patch(c)
	
	plt.axis('scaled')
	plt.show()


if __name__ == '__main__':
	a = [10, 9, 8, -1, -1, -1, -1, -1, 2, 1, 0, -1, -1, -1, -1, -1, -1, 22, 21, 20, 19, 18, 17]
	arc_diagram(a)

