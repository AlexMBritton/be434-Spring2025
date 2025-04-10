#!/usr/bin/env python3
import argparse
import sys

def read_fasta(filehandle):
    sequences = {}
    current_id = None
    for line in filehandle:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            sequences[current_id] = ""
        else:
            sequences[current_id] += line
    return sequences

def gc_content(seq):
    gc = sum(1 for base in seq if base in "GCgc")
    return (gc / len(seq)) * 100 if seq else 0

def main():
    parser = argparse.ArgumentParser(description="Compute GC content")
    parser.add_argument("file", nargs="?", help="Input sequence file")
    args = parser.parse_args()

    try:
        if args.file:
            with open(args.file) as file:
                sequences = read_fasta(file)
        else:
            sequences = read_fasta(sys.stdin)
    except FileNotFoundError as e:
        parser.print_help()
        print(e)
        exit(1)

    best_id, best_gc = max(sequences.items(), key=lambda item: gc_content(item[1]))
    print(f"{best_id} {gc_content(sequences[best_id]):.6f}")

if __name__ == "__main__":
    main()
