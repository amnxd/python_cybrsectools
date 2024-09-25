import string
import itertools

def generate_wordlist(min_length, max_length, output_file):
    with open(output_file, "w") as f:
        for r in range(min_length, max_length + 1):
            for word in itertools.product(string.ascii_lowercase, repeat=r):
                f.write("".join(word) + "\n")

min_length = int(input("Enter the minimum word length: "))
max_length = int(input("Enter the maximum word length: "))
output_file = input("Enter the output file name: ")

generate_wordlist(min_length, max_length, output_file)