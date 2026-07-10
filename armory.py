# Import the Seq class from Biopython for representing biological sequences
from Bio.Seq import Seq

# Open the input file containing the DNA string
with open("rosalind_ini.txt") as f:
    # Read the first line and strip the trailing whitespace
    s = f.readline().strip()

# Wrap the raw string in a Biopython Seq object
my_seq = Seq(s)

# Count the number of adenine (A) bases in the sequence
a = my_seq.count("A")
# Count the number of cytosine (C) bases in the sequence
c = my_seq.count("C")
# Count the number of guanine (G) bases in the sequence
g = my_seq.count("G")
# Count the number of thymine (T) bases in the sequence
t = my_seq.count("T")

# Print the counts of A, C, G, T separated by spaces
print(a, c, g, t)
