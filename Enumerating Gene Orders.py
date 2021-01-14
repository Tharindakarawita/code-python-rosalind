# Problem
# A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

# Given: A positive integer n≤7.

# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

# Sample Dataset

# 3

# Sample Output

# 6
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1





from itertools import permutations
num = 6 #open("C:/Users/Tharinda Karawita/Downloads/rosalind_prtm.txt", "r").read()
num_list = [i for i in range(1,num+1)]
print(len([n for n in permutations(num_list)]))
for n in permutations(num_list):
    print(" ".join(map(str,n)))

