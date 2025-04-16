#!/usr/bin/env python3
import argparse
import os
import sys

def read_fasta_lengths(filename):
    lengths = []
    with open(filename) as f:
        current = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current:
                    lengths.append(len(''.join(current)))
                    current = []
            else:
                current.append(line)
        if current:
            lengths.append(len(''.join(current)))

    if not lengths:
        return (filename, 0, 0, "0.00", 0)

    avg_len = "{:.2f}".format(sum(lengths) / len(lengths))
    return (filename, min(lengths), max(lengths), avg_len, len(lengths))

def main():
    parser = argparse.ArgumentParser(description='Analyze FASTA files')
    parser.add_argument('files', nargs='+', help='FASTA files to process')
    args = parser.parse_args()

    for file in args.files:
        if not os.path.exists(file):
            parser.print_usage()
            print(f"No such file or directory: '{file}'")
            sys.exit(1)

    print("name    min_len    max_len    avg_len    num_seqs")
    for file in args.files:
        result = read_fasta_lengths(file)
        print("    ".join(map(str, result)))

if __name__ == '__main__':
    main()
