#!/usr/bin/env python3

import argparse
import random
import sys

def make_sequence(length, gc_frac, seqtype):
    num_gc = round(length * gc_frac)
    num_at = length - num_gc
    gc_bases = 'GC' if seqtype == 'dna' else 'GC'
    at_bases = 'AT' if seqtype == 'dna' else 'AU'
    sequence = random.choices(gc_bases, k=num_gc) + random.choices(at_bases, k=num_at)
    random.shuffle(sequence)
    return ''.join(sequence)

def main():
    parser = argparse.ArgumentParser(description='Create synthetic DNA/RNA sequences')
    parser.add_argument('-o', '--outfile', type=str, default='out.fa', help='Output file (default: out.fa)')
    parser.add_argument('-t', '--seqtype', type=str, default='dna', choices=['dna', 'rna'], help='Sequence type (dna or rna)')
    parser.add_argument('-n', '--numseqs', type=int, default=10, help='Number of sequences to generate (default: 10)')
    parser.add_argument('-m', '--minlen', type=int, default=50, help='Minimum sequence length (default: 50)')
    parser.add_argument('-x', '--maxlen', type=int, default=75, help='Maximum sequence length (default: 75)')
    parser.add_argument('-p', '--pctgc', type=str, default="0.5", help='GC content percentage (0–1, default: 0.5)')
    parser.add_argument('-s', '--seed', type=int, default=None, help='Random seed (optional)')
    args = parser.parse_args()

    # Manual validation of pctgc with exact message and exit
    try:
        pctgc = float(args.pctgc)
        if not 0 <= pctgc <= 1:
            raise ValueError
    except ValueError:
        parser.print_usage()
        print(f'--pctgc "{float(args.pctgc)}" must be between 0 and 1')
        sys.exit(1)
        sys.exit(1)

    if args.seed is not None:
        random.seed(args.seed)

    with open(args.outfile, 'w') as out_f:
        for i in range(1, args.numseqs + 1):
            length = random.randint(args.minlen, args.maxlen)
            seq = make_sequence(length, pctgc, args.seqtype)
            out_f.write(f">seq{i}\n{seq}\n")
    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile}".')

if __name__ == '__main__':
    main()
