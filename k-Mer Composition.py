from Bio import SeqIO
from collections import Counter

Fasta_seqs = ''
# for record in SeqIO.parse("C:/Users/nayan/Desktop/new 7.txt", 'fasta'):
for record in SeqIO.parse("D:/trash/rosalind_kmer.txt", 'fasta'):
    Fasta_seqs += record.seq
    
list = []
# print(Fasta_seqs)


for i in range(len(Fasta_seqs)-4+1):
    list.append(Fasta_seqs[i:i+4])
list.sort()

# print(list)


for i in Counter(list).values():
    print(i,end=" ")