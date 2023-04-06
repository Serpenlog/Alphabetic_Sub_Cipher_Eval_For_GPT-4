import itertools
import random

def generate_permutations(n, output_file):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    random.seed(42)

    with open(output_file, "w", encoding='utf-8') as outfile:
        for _ in range(n):
            permutation = ''.join(random.sample(alphabet, len(alphabet)))
            outfile.write(permutation + "\n")
