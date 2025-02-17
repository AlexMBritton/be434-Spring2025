#!/usr/bin/env python3
import argparse
import sys
import os

def reverse_complement(dna: str) -> str:
    """Returns the reverse complement of a given DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                  'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}  # Preserve case
    return "".join(complement[base] for base in reversed(dna))

def main():
    """Main function to handle command-line arguments and process DNA input."""
    parser = argparse.ArgumentParser(description="Print the reverse complement of DNA")
    parser.add_argument("DNA", help="Input sequence or file")
    args = parser.parse_args()

    # Check if the input is a file and read contents
    file_path = args.DNA
    if os.path.isfile(file_path):  # Ensures we are correctly checking the file
        try:
            with open(file_path, "r") as file:
                dna = file.read().strip()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found", file=sys.stderr)
            sys.exit(1)
    else:
        dna = args.DNA  # Directly use the input if it's not a file

    # Validate DNA sequence
    if not all(base in "ATCGatcg" for base in dna):
        print("Error: Invalid DNA sequence (only A, T, C, G allowed)", file=sys.stderr)
        sys.exit(1)

    # Print the reverse complement
    print(reverse_complement(dna))

if __name__ == "__main__":
    main()
