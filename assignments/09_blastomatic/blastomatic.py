
#!/usr/bin/env python3
import argparse
import csv
import sys
import os

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

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Merge BLAST hits with metadata')
    parser.add_argument('-a', '--annotations', required=True, help='Annotations file')
    parser.add_argument('-b', '--blasthits', required=True, help='BLAST -outfmt 6')
    parser.add_argument('-o', '--outfile', type=str, default="out.csv", help='Output file (default: out.csv)')
    parser.add_argument('-d', '--delimiter', type=str, help='Output field delimiter')
    parser.add_argument('-p', '--pctid', type=float, default=0.0, help='Minimum percent identity')
    args = parser.parse_args()

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
        writer = csv.DictWriter(out_f, fieldnames=['qseqid', 'pident', 'depth', 'lat_lon'], delimiter=delimiter)
        writer.writeheader()
        writer.writerows(results)

    print(f'Exported {len(results)} to "{args.outfile}".')

if __name__ == '__main__':
    main()
