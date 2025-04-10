#!/usr/bin/env python3
import argparse
import sys
import os

def get_args():
    """Parse command-line arguments and handle file input."""
    parser = argparse.ArgumentParser(description="Print the reverse complement of DNA")
    parser.add_argument("DNA", metavar="DNA", help="Input sequence or file")
    args = parser.parse_args()

    # If DNA is a file, read its content
    if os.path.isfile(args.DNA):
        try:
            with open(args.DNA, "r") as file:
                args.DNA = file.read().strip()  # Read and strip whitespace
        except FileNotFoundError:
            print(f"Error: File '{args.DNA}' not found", file=sys.stderr)
            sys.exit(1)

    return args.DNA  # Return the DNA sequence

def reverse_complement(dna: str) -> str:
    """Returns the reverse complement of a given DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                  'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}  # Preserve case
    return "".join(complement[base] for base in reversed(dna))

def main():
    """Main function to process DNA input and print the reverse complement."""
    dna = get_args()  # Get DNA sequence from args

    # Validate DNA sequence
    if not all(base in "ATCGatcg" for base in dna):
        print("Error: Invalid DNA sequence (only A, T, C, G allowed)", file=sys.stderr)
        sys.exit(1)

    # Print the reverse complement
    print(reverse_complement(dna))

if __name__ == "__main__":
    main()
