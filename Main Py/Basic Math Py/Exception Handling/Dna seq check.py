class InvalidDNASequence(Exception):
    pass

dna_sequence = input("Enter a DNA sequence: ")

def check_dna_sequence(dna_sequence):
    for base in dna_sequence.upper():
        if base not in ['A', 'T', 'G', 'C']:
            raise InvalidDNASequence("Invalid DNA sequence: contains non-ATGC bases")

try:
    check_dna_sequence(dna_sequence)
    print("Valid sequence")
except Exception as e:
    print(e)
