find# Go to unip,download seq relate to keratin , download all entries and put in a single file 
# load that into colab and rename file "antifreeze.fasta"
# use bp module to find foll:
# mol weight of every prot seq
# len of every prot seq
# find seqs which starts with 'A' and count no of occ of 'A'
# find longest seq among keratin  and write that seq into a file longest_keratin.fasta
# find no of seq whose having len<100 and write those entries into resp fasta files


from Bio.Seq import Seq
from Bio import SeqIO
import re
from Bio.SeqUtils.ProtParam import ProteinAnalysis
#  Bio.SeqUtils - used for calculations


antifreeze=SeqIO.parse("/content/antifreeze.fasta","fasta")
#print(antifreeze)  # op = obj iterator so loop

# mol weight of every prot seq

# i.seq = prints only seq  len(i.seq)

  # exception removal
for i in antifreeze:
  pseq=ProteinAnalysis(i.seq)
  if re.search("X",str(i.seq)):
    continue                                 # skipping exceptions
  else:
    print(pseq.molecular_weight())

# len of every prot seq
#print("length",len(i.seq))


for i in antifreeze:
   pseq=ProteinAnalysis(i.seq)
   if re.search("^A",str(i.seq)):
     print(("starts with A ",i.seq))


# find seqs which starts with 'A' and count no of occ of 'A'
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import re
antiffindreeze=SeqIO.parse("/content/antifreeze.fasta","fasta")
for i in antifreeze:
  pseq=ProteinAnalysis(i.seq)
  if re.search("^A",str(i.seq)):
    
    print(i.seq)

  

