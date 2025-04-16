#!/usr/bin/env python3
import argparse
import os
import sys

def get_sequences(file):
    with open(file) as f:
        return [line.strip() for line in f if line.strip()]

def compare_sequences(seqs):
    consensus = []
    for chars in zip(*seqs):
        consensus.append('|' if all(c == chars[0] for c in chars) else 'X')
    return ''.join(consensus)

def main():
    parser = argparse.ArgumentParser(description='Find conserved sequence positions')
    parser.add_argument('file', help='FASTA-like input file')
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"No such file or directory: '{args.file}'")
        sys.exit(1)

    seqs = get_sequences(args.file)
    if len(seqs) < 2:
        print("Need at least two sequences")
        sys.exit(1)

    for seq in seqs:
        print(seq)
    print(compare_sequences(seqs))

if __name__ == '__main__':
    main()
