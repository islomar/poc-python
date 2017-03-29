# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

#ro = red circles
#b- = solid blue lines
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.ylabel('alpha')
plt.xlabel('number of processors')

plt.savefig('mi-grapfica.png')
plt.savefig('mi-grapfica.pdf')