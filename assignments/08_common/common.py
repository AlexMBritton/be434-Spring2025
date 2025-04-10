#!/usr/bin/env python3
import argparse

def get_words(filehandle):
    words = set()
    for line in filehandle:
        for word in line.strip().split():
            words.add(word)
    return words

def main():
    parser = argparse.ArgumentParser(description='Find common words')
    parser.add_argument('file1', type=argparse.FileType('r'), help='Input file 1')
    parser.add_argument('file2', type=argparse.FileType('r'), help='Input file 2')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), help='Optional output file (default: stdout)')
    args = parser.parse_args()

    words1 = get_words(args.file1)
    words2 = get_words(args.file2)
    common = sorted(words1 & words2)

    output = args.output if args.output else None
    for word in common:
        if output:
            output.write(f"{word}\n")
        else:
            print(word)

if __name__ == '__main__':
    main()
