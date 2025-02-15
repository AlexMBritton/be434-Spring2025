#!/usr/bin/env python3
"""
Author : Alex
Date   : 2025-02-14
Purpose: divide two numbers
"""

import argparse
import sys

def get_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Divide two numbers')
    parser.add_argument('num1', type=int, help='First integer')
    parser.add_argument('num2', type=int, help='Second integer (cannot be zero)')
    return parser.parse_args()

def main():
    """Main function."""
    args = get_args()

    if args.num2 == 0:
        print("usage: divide.py [-h] INT INT", file=sys.stderr)
        print("divide.py: error: Cannot divide by zero, dum-dum!", file=sys.stderr)
        sys.exit(1)

    result = args.num1 // args.num2
    print(f"{args.num1} / {args.num2} = {result}")

if __name__ == '__main__':
    main()
