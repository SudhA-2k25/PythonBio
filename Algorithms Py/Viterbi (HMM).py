# Viterbi algorithm
import math as m
seq = "GGCACTGAA"

H = {"A":m.log(0.2,2),"C":m.log(0.3,2),"G":m.log(0.3,2),"T":m.log(0.2,2)}
L = {"A":m.log(0.3,2),"C":m.log(0.2,2),"G":m.log(0.2,2),"T":m.log(0.3,2)}

start_H=m.log(0.5,2) # =-1
start_L=m.log(0.5,2)

hh= m.log(0.5,2)
ll= m.log(0.6,2)

h_l= m.log(0.5,2)
l_h= m.log(0.4,2)

h1 = round(start_H + H[seq[0]], 2)
l1 = round(start_L + L[seq[0]], 2)

high_list = [h1]  # Appending
low_list = [l1]

for i in range(1, len(seq)):
  h_value = round(H[seq[i]] + max(high_list[i-1]+hh, low_list[i-1]+l_h), 2)
  high_list.append(h_value)
  l_value = round(L[seq[i]] + max(high_list[i-1]+h_l, low_list[i-1]+ll), 2)
  low_list.append(l_value)

print("high_list : ",list(high_list))
print("low_list : ",list(low_list))


# back trace 

output = ""
for i in range(len(seq)):
  if high_list[i] == low_list[i]  or seq[i] == "G"  or seq[i] == "C" or high_list[i] > low_list[i]:
    output += 'H'
  else:
    output += 'L'

print("Back Tracing : ",output) 