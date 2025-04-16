
#!/usr/bin/env python3
"""Parse blast file"""

import argparse
import csv
import os
import sys


def read_hits(file):
    """Read BLAST hits from file"""
    if not os.path.isfile(file):
        print(f"No such file or directory: '{file}'")
        sys.exit(1)
    with open(file) as f:
        return [line.strip().split('\t') for line in f if line.strip()]


def read_metadata(file):
    """Read metadata from CSV file"""
    if not os.path.isfile(file):
        print(f"No such file or directory: '{file}'")
        sys.exit(1)
    meta = {}
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        if 'query' not in reader.fieldnames:
            print(f"No such file or directory: '{file}'")
            sys.exit(1)
        for row in reader:
            meta[row['query']] = row
    return meta


def guess_delimiter(filename, user_delim=None):
    """Guess the delimiter based on file extension"""
    if user_delim:
        return user_delim
    if filename.endswith(('.tsv', '.tab', '.txt')):
        return '\t'
    return ','


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                       '--blasthits',
                       metavar='FILE',
                       help='BLAST -outfmt 6',
                       required=True)

    parser.add_argument('-a',
                       '--annotations',
                       metavar='FILE',
                       help='Annotations file',
                       required=True)

    parser.add_argument('-o',
                       '--outfile',
                       metavar='FILE',
                       help='Output file',
                       default='out.csv')

    parser.add_argument('-d',
                       '--delimiter',
                       metavar='DELIM',
                       help='Output field delimiter')

    parser.add_argument('-p',
                       '--pctid',
                       help='Minimum percent identity',
                       type=float,
                       default=0.0)

    return parser.parse_args()


def main():
    """Make a jazz noise here"""
    args = get_args()
    hits = read_hits(args.blasthits)
    metadata = read_metadata(args.annotations)

    results = []
    for fields in hits:
        query_id = fields[0]
        pident = float(fields[2])
        if pident < args.pctid:
            continue
        if query_id not in metadata:
            continue
        row = {
            'qseqid': query_id,
            'pident': fields[2],
            'depth': metadata[query_id]['depth'],
            'lat_lon': metadata[query_id]['lat_lon']
        }
        results.append(row)

    delimiter = guess_delimiter(args.outfile, args.delimiter)
    with open(args.outfile, 'w', newline='') as out_f:
        writer = csv.DictWriter(out_f,
                              fieldnames=['qseqid', 'pident', 'depth', 'lat_lon'],
                              delimiter=delimiter)
        writer.writeheader()
        writer.writerows(results)

    print(f'Exported {len(results)} to "{args.outfile}".')


if __name__ == '__main__':
    main()
