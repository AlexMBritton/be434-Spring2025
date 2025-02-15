#!/usr/bin/env python3
"""
Author : Alex <your email>
Date   : 2025-02-14
Purpose: Tetranucleotide frequency counter
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input DNA sequence or filename')

    return parser.parse_args()


# --------------------------------------------------
def read_dna(source):
    """Read DNA sequence from file or direct input"""

    try:
        if source and source.endswith(
                ('.txt', '.fa', '.fasta')):  # Wrapped onto two lines
            with open(source, 'rt',
                      encoding='utf-8') as file:  # Line length fixed
                return file.read().strip()
    except FileNotFoundError:
        print(f'Error: File "{source}" not found.', file=sys.stderr)
        sys.exit(1)

    return source  # If not a file, treat as direct sequence


# --------------------------------------------------
def count_bases(dna):
    """Count occurrences of A, C, G, and T in DNA sequence"""
    return dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')


# --------------------------------------------------
def main():
    """Main function"""

    args = get_args()
    dna_sequence = read_dna(args.DNA)
    a, c, g, t = count_bases(dna_sequence)
    print(a, c, g, t)


# --------------------------------------------------
if __name__ == '__main__':
    main()
