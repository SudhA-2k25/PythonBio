# HMM
import numpy as np
np.random.seed(9)
h=['hydrophobic','hydrophillic']
aa=['leucine','arginine']

for k in range(10):
  ran1=np.random.choice(h,size=1,replace=True,p=[0.5,0.5])
  ran2=np.random.choice(aa,size=1,replace=True,p=[0.6,0.4])

  print(ran1)
  print(ran2)