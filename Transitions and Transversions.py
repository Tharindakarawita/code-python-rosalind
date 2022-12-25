# Problem
# For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

# Return: The transition/transversion ratio R(s1,s2).

# Sample Dataset
# >Rosalind_0209
# GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
# AGTACGGGCATCAACCCAGTT
# >Rosalind_2200
# TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
# GGTACGAGTGTTCCTTTGGGT
# Sample Output
# 1.21428571429


from Bio import SeqIO

Fasta_seqs = []
# for record in SeqIO.parse("C:/Users/nayan/Desktop/new 7.txt", 'fasta'):
for record in SeqIO.parse("D:/trash/rosalind_kmer.txt", 'fasta'):
    Fasta_seqs.append(str(record.seq))


def ratio_counter(DNA):
    s1 = 0
    s2 = 0
    for i in range(len(DNA[0])-1):
        if DNA[0][i] != DNA[1][i]:
        
            if DNA[0][i] == 'A':
                if DNA[1][i] == 'G':
                    s1 += 1
                elif DNA[1][i] == 'C'or'T':
                    s2 += 1

            if DNA[0][i] == 'G':
                if DNA[1][i] == 'A':
                    s1 += 1
                elif DNA[1][i] == 'C'or'T':
                    s2 += 1

            if DNA[0][i] == 'C':
                if DNA[1][i] == 'T':
                    s1 += 1
                elif DNA[1][i] == 'A'or'G':
                    s2 += 1

            if DNA[0][i] == 'T':
                if DNA[1][i] == 'C':
                    s1 += 1
                elif DNA[1][i] == 'A' or 'G':
                    s2 += 1
            
    return s1/s2

print(ratio_counter(Fasta_seqs))

