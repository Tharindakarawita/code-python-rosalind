"""Calculating Expected Offspring"""

# Averages arise everywhere. In sports, we want to project the average number of games that a team is expected to win; in gambling, we want to project the average losses incurred playing blackjack; in business, companies want to calculate their average expected sales for the next quarter.

# Molecular biology is not immune from the need for averages. Researchers need to predict the expected number of antibiotic-resistant pathogenic bacteria in a future outbreak, estimate the predicted number of locations in the genome that will match a given motif, and study the distribution of alleles throughout an evolving population. In this problem, we will begin discussing the third issue; first, we need to have a better understanding of what it means to average a random process.

# Problem
# For a random variable X taking integer values between 1 and n, the expected value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.

# As a motivating example, let X be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

# More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die example to find that if X is a uniform random variable with minimum possible value a and maximum possible value b, then E(X)=a+b2. You may also wish to verify that for the dice example, if Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7.

# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

# Sample Dataset
# 1 0 0 1 0 1
# Sample Output
# 3.5


num_of_genotypes = '17309 17506 18847 16973 16518 19638'
num_of_genotypes_list =  [int(i) for i in num_of_genotypes.split()]
max_num = 0
min_num = 0
for location,item in enumerate(num_of_genotypes_list):
    if location == 0:
        max_num = num_of_genotypes_list[location]*2
        min_num = num_of_genotypes_list[location]*2
    elif location == 1:
        max_num += num_of_genotypes_list[location]*2
        min_num += num_of_genotypes_list[location]*2
    elif location == 2:
        max_num += num_of_genotypes_list[location]*2
        min_num += num_of_genotypes_list[location]*2
    elif location == 3:
        max_num += num_of_genotypes_list[location]*2
        min_num += num_of_genotypes_list[location]*1
    elif location == 4:
        max_num += num_of_genotypes_list[location]*2
        min_num += num_of_genotypes_list[location]*0
    elif location == 5:
        max_num += num_of_genotypes_list[location]*0
        min_num += num_of_genotypes_list[location]*0

print((max_num+min_num)/2)

