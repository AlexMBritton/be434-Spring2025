#!/usr/bin/env python3
import argparse
import os
import sys

# Preprocess arguments to alias --out_dir to --outdir
if "--out_dir" in sys.argv:
    i = sys.argv.index("--out_dir")
    sys.argv[i] = "--outdir"

def transcribe_dna_to_rna(dna):
    return dna.replace('T', 'U').replace('t', 'u')

def process_file(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, os.path.basename(input_file))
    count = 0
    with open(input_file) as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            f_out.write(transcribe_dna_to_rna(line.strip()) + '\n')
            count += 1
    return count

def main():
    parser = argparse.ArgumentParser(description='Transcribe DNA into RNA')
    parser.add_argument('files', nargs='+', help='Input DNA file(s)')
    parser.add_argument('-o', '--outdir', default='out', help='Output directory (default: out)')
    args = parser.parse_args()

    try:
        total_seqs = 0
        for file in args.files:
            total_seqs += process_file(file, args.outdir)
        print(f'Done, wrote {total_seqs} sequence{"s" if total_seqs != 1 else ""} in {len(args.files)} file{"s" if len(args.files) != 1 else ""} to directory "{args.outdir}".')
    except FileNotFoundError as e:
        parser.print_help()
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()
