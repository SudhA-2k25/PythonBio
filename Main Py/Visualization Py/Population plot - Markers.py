# Markers in matlab
# [marker][line style][colour]

# create a py chart for ploting population in india
# 1990 - 2000
# x=year, y=population in cr

from matplotlib import pyplot as plt
import numpy as np
xa=np.array([1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000])
ya=np.array([700000,600000,700000,8000000,8000000,8000000,8000000,8000000,8000000,88000000,98000000])
plt.plot(xa,ya,"^-r")  # marker o--g    
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population chart")
plt.show()