fh=open("/content/fh.txt","r")
pdb=fh.readlines()
print(pdb)  # To read the contents of the file

import re
fh=open("/content/fh.txt","r")
pdb=fh.readlines()
li=[]
for i in pdb:
  re.sub("\n","",i)  # To avoid New line
  li.append(a)
print(li)

# Example

#Extracting cys resd
import re
fh=open("/content/fh.txt","r")
pdb=fh.readlines()
li=[]
for i in li:
  if re.search("^ATOM.*CYS",i):
     print(i)
	 
#Extracting cys resd
import re
import math
fh=open("/content/model_01 (2).pdb","r")
pdb=fh.readlines()
cys=[]
for i in pdb:
  a=re.sub("\n","",i)
  li.append(a)
for i in li:
   if re.search("^ATOM.*CA.*CYS",i):
     cys.append(i)
print(cys)
for i in range(len(cys)):
  for j in range(len(cys)):
    a1=re.findall("-?\d+\.\d{3}", cys[i])
    a2=re.findall("-?\d+\.\d{3}",cys[j])
    cord1= [float(ele) for ele in a1]  #ele-random var
    cord2= [float(ele) for ele in a2]
    #print(r1,r2)
    d=math.dist(cord1,cord2)
    atom1=re.findall("CYS\S+[A-Z]\s+\d+",cys[i])
    atom2=re.findall("CYS\S+[A-Z]\s+\d+",cys[j])
    print(atom1,atom2)
    print(atom1,atom2,"The distance is ",d)
    #print(round(d,4))
	

# Getting the atom coordinates

import re
import math
f=open("/content/2rec.pdb","r")
pdb=f.readlines()
#for i in pdb:
  #print(i)  # To read the file 

def centroid(chain):
    
    count=0
    chain=[]
    sumx=0
    sumy=0
    sumz=0
    for i in range(len(pdb)):
      if re.search("^ATOM\s+\d+\s+[A-Z]+\s+[A-Z]{3}\s+",pdb[i]): 
        count=count+1
        xyz=re.findall("-?\d+\.\d{3}",pdb[i])
        sumx=sumx+float(xyz[0])
        sumy=sumx+float(xyz[1])
        sumz=sumx+float(xyz[2])

    cx=round(sumx/count,3)
    cy=round(sumy/count,3)
    cz=round(sumz/count,3)
    return str(cx)+" "+str(cy)+" "+str(cz)

a=centroid("A")
print(a)
b=centroid("B")
print(b)
c=centroid("C")
print(c)
d=centroid("D")
print(d)
e=centroid("E")
print(e)
f=centroid("F")
print(f)

f=centroid("F")
print(f)






