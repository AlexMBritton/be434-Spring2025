
#!/usr/bin/env python3
"""Parse blast file"""

import argparse
import csv
import os
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """Command-line arguments"""
    blasthits: TextIO
    annotations: TextIO
    outfile: str
    delimiter: str
    pctid: float


def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                       '--blasthits',
                       help='BLAST -outfmt 6',
                       metavar='FILE',
                       type=argparse.FileType('rt'),
                       required=True)

    parser.add_argument('-a',
                       '--annotations',
                       help='Annotations file',
                       metavar='FILE',
                       type=argparse.FileType('rt'),
                       required=True)

    parser.add_argument('-o',
                       '--outfile',
                       help='Output file',
                       metavar='FILE',
                       type=str,
                       default='out.csv')

    parser.add_argument('-d',
                       '--delimiter',
                       help='Output field delimiter',
                       metavar='DELIM',
                       type=str,
                       default='')

    parser.add_argument('-p',
                       '--pctid',
                       help='Minimum percent identity',
                       metavar='PCTID',
                       type=float,
                       default=0.0)

    args = parser.parse_args()

    return Args(args.blasthits, args.annotations, args.outfile,
               args.delimiter, args.pctid)


def guess_delimiter(filename: str) -> str:
    """Guess the delimiter based on the file extension"""
    ext = os.path.splitext(filename)[1].lower()
    return '\t' if ext in ['.tab', '.txt', '.tsv'] else ','


def main() -> None:
    """Make a jazz noise here"""
    args = get_args()

    # Load the annotations into a lookup dict
    annotations = {}
    reader = csv.DictReader(args.annotations)
    for row in reader:
        annotations[row['qseqid']] = {
            'depth': row['depth'],
            'lat_lon': row['lat_lon']
        }

    # Determine output delimiter
    delimiter = args.delimiter or guess_delimiter(args.outfile)

    # Process BLAST hits and write output
    hits = []
    for line in args.blasthits:
        fields = line.rstrip().split('\t')
        qseqid = fields[0]
        pctid = float(fields[2])
        
        if pctid >= args.pctid and qseqid in annotations:
            hits.append({
                'qseqid': qseqid,
                'pident': fields[2],
                'depth': annotations[qseqid]['depth'],
                'lat_lon': annotations[qseqid]['lat_lon']
            })

    # Write output
    with open(args.outfile, 'wt') as out:
        writer = csv.DictWriter(out,
                              fieldnames=['qseqid', 'pident', 'depth', 'lat_lon'],
                              delimiter=delimiter)
        writer.writeheader()
        writer.writerows(hits)

    print(f'Exported {len(hits)} to "{args.outfile}".')


if __name__ == '__main__':
    main()
