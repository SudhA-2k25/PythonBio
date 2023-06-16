# Protein Hydrophobicity Plot
import matplotlib.pyplot as plt #or from matplotlib import pyplot as plt
import numpy as np

seq = "MLASASTRATHAN"
d = {
    "I": 4.5,
    "V": 4.2,
    "L": 3.8,
    "F": 2.8,
    "C": 2.5,
    "M": 1.9,
    "A": 1.8,
    "G": -0.4,
    "T": -0.7,
    "S": -0.8,
    "W": -0.9,
    "Y": -1.3,
    "P": -1.6,
    "H": -3.2,
    "E": -3.5,
    "Q": -3.5,
    "D": -3.5,
    "N": -3.5,
    "K": -3.9,
    "R": -4.5
}

x = range(1, len(seq) + 1)
l = []
for i in seq:
    l.append(d[i])

plt.plot(x, l)
plt.xlabel("Residue Number")
plt.ylabel("Hydrophobicity")
plt.title("Protein Hydrophobicity Plot")
plt.show()
