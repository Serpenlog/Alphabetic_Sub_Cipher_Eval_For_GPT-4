import itertools
import random

def generate_permutations():
    n = int(input("Enter the number of permutations: "))
    output_file = input("Enter the output file name: ")

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    with open(output_file, "w") as outfile:
        for _ in range(n):
            perm = ''.join(random.sample(alphabet, len(alphabet)))
            outfile.write(perm + "\n")
