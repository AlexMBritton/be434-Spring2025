#!/usr/bin/env python3
"""
Author : Alex
Date   : 2025-02-14
Purpose: divide two numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='divide two numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='INT',
                        help='two integers to divide',
                        nargs=2,
                        type=int)

    args = parser.parse_args()
    if args.numbers[1] == 0:
        parser.error(f'Cannot divide by zero, dum-dum!')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = args.numbers
    num1 = numbers[0]
    quotient = num1 // numbers[1]

    print(f'my answer is: {quotient}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
