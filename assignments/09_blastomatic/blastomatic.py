#!/usr/bin/env python3
import argparse
import os
import sys

def main():
    print("DEBUG: Raw sys.argv =", sys.argv)

    parser = argparse.ArgumentParser(description='Debug parser')
    parser.add_argument('-a', '--annotations', required=True)
    parser.add_argument('-b', '--blasthits', required=True)
    args = parser.parse_args()

    print("DEBUG: args.blasthits =", args.blasthits)
    print("DEBUG: args.annotations =", args.annotations)
    print("DEBUG: File exists (blasthits)?", os.path.isfile(args.blasthits))
    print("DEBUG: File exists (annotations)?", os.path.isfile(args.annotations))

if __name__ == '__main__':
    main()
