# """Problem"""
# For positive integers a and n, a modulo n (written amodn in shorthand) is the remainder
# when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

# Modular arithmetic is the study of addition, subtraction, multiplication, and division 
# with respect to the modulo operation. We say that a and b are congruent modulo n if
# amodn=bmodn; in this case, we use the notation a≡bmodn.

# Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn
# and a×c≡b×dmodn. To check your understanding of these rules, you may wish to verify 
# these relationships for a=29, b=73, c=10, d=32, and n=11.

# As you will see in this exercise, some Rosalind problems will ask for a (very large) 
# integer solution modulo a smaller number to avoid the computational pitfalls that
# arise with storing such large numbers.

# Given: A protein string of length at most 1000 aa.

# Return: The total number of different RNA strings from which the protein could 
# have been translated, modulo 1,000,000. (Don't neglect the importance of the stop
# codon in protein translation.)

# Sample Dataset

# MA

# Sample Output

# 12
map = {"M":1,
    "W":1,
    "N":2,
    "D":2,
    "C":2,
    "Q":2,
    "E":2,
    "H":2,
    "K":2,
    "F":2,
    "Y":2,
    "I":3,
    "A":4,
    "G":4,
    "P":4,
    "T":4,
    "V":4,
    "R":6,
    "L":6,
    "S":6}




#n = 0
possible_count_of_seq = 1
AA_seq = open("C:/Users/Tharinda Karawita/Downloads/rosalind_mrna (6).txt", "r").read().rstrip()
#print(len(AA_seq),AA_seq)
for i  in AA_seq:
#    print(map.get(i),end=" ")
#    n += 1
    possible_count_of_seq *= map.get(i)
possible_count_of_seq *= 3
#print(possible_count_of_seq)
#print(n)
print(divmod(possible_count_of_seq,1000000)[1])