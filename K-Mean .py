# KMean clustering
import math
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 4, 5])
y = np.array([1, 1, 3, 4])


min_dist = 8  # random
# Find nearest pt
for i in range(3):
  dist = math.sqrt((x[i] - x[i+1]) ** 2 + (y[i] - y[i+1]) ** 2)
  if dist < min_dist:
    p1x, p1y = x[i], y[i]
    p2x, p2y = x[i+1], y[i+1]
    min_dist = dist
print("\nmin Dist : ",min_dist)

# Assigning points
c1 = []  # column 1 
c2 = []
for i in range(4):
    dist1 = round( math.sqrt((x[i]-p1x)**2 + (y[i]-p1y)**2), 1 )
    dist2 = round( math.sqrt((x[i]-p2x)**2 + (y[i]-p2y)**2), 1 )
    if dist1 < dist2: 
      cluster = "X"  # compare both <--> take lowest
      c1.append([x[i], y[i]])
    else:
      cluster = "Y"
      c2.append([x[i], y[i]])
    print(dist1, "\t", dist2, "\t", cluster)

#  Centroid Calc
centroid_x = round(sum(point[0] for point in c2) / len(c2),2)
centroid_y = round(sum(point[1] for point in c2) / len(c2),2)
centroid = [centroid_x, centroid_y]

print("centroid : ",centroid)