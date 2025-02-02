#!/usr/bin/env python3
"""
Author: Alex Britton
Email: alexanderbritton@arizona.edu
Purpose: Print greeting
"""

import argparse

def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Greetings and howdy')

    parser.add_argument('-g', '--greeting',
                        metavar='str',
                        default='Howdy',
                        help='The greeting (default: Howdy)')

    parser.add_argument('-n', '--name',
                        metavar='str',
                        default='Stranger',
                        help='Whom to greet (default: Stranger)')

    parser.add_argument('-e', '--excited',
                        action='store_true',
                        help='Include an exclamation point (default: False)')

    return parser.parse_args()

def main():
    """Main function"""
    args = get_args()
    punctuation = '!' if args.excited else '.'
    print(f"{args.greeting}, {args.name}{punctuation}")

if __name__ == '__main__':
    main()
