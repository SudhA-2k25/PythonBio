from IPython.utils.sysinfo import pprint
# Input a seq  THRO bp AND FIND the FOLL using bp module
# melt pt
# use comp stand to find trans()
# use vertibrate mit as std genetic table and find translate() coding seq
# find GC % 
# Also find Comp of bases count
# search for patten ( without regEx) -
# Write all op in a file calc.txt


# 1)  MELT POINT
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
s=Seq("ACGAAGGACG")   
a= "melting point is : "+str(mt.Tm_GC(s))
#print("melting point is : ",mt.Tm_GC(s)) 
print(a)

# 2) using comp stand to find trans()
code_strand=Seq("ACGAAGGACG")
print(code_strand.reverse_complement()) # reverse_complement()=template_strand
b="Transcribed seq : "+str(code_strand.transcribe())
#print("Transcribed seq : ",code_strand.transcribe())
print(b)

# rev_comp.transcribe()=code_strand.transcribe()


# 3) using vertibrate mitochondria as std genetic table and find translate() coding seq
from Bio.Seq  import Seq
seq=Seq("ACGAAGGACG")
c= "Translated seq : "+str(seq.translate(("Vertebrate Mitochondrial")))
# print(seq.translate(("Vertebrate Mitochondrial")))   # vertibrate mitochondria code 
# This or this any way b done
dna=Seq("ACGAAGGACG")
mess=dna.translate(table="Vertebrate Mitochondrial")
print("Translated Seq : ",mess)


# 4) find GC % 
from Bio.Seq  import Seq 
from Bio.SeqUtils import GC
g_c=Seq("ACGAAGGACG")
#print(" GC % : ",GC(g_c))
gc=" GC % : "+str(GC(g_c))

# 5) find Count of bases 
s="ACGAAGGACG"    # str for count 
print(s.count('A')," - No of A",s.count('C')," - No of C",s.count('G')," - No of G",s.count('T')," - No of T")

 


# 6) search for patten ( without regEx) -

from Bio.Seq  import Seq    
from Bio import SeqUtils
SeqUtils.nt_search(s,p) # nucleotide
s="ACGAAGGACGAAGAAT"
p="AA"
print("PATTERN SEARCH : ",(SeqUtils.nt_search(s,p)))  # list op
pattern="PATTERN SEARCH : "+str( (SeqUtils.nt_search(s,p)) )
# Write all op in a file calc.txt

 # Write all op in a file calc.txt

op=open("calculation.txt","w")
op.write(a)
op.write("\n")
op.write(b)
op.write("\n")
op.write(c)
op.write("/n")
op.write(gc)
op.write("/n")
op.write(pattern)
op.close()


f=open("calculation.txt","r")
f.readlines()