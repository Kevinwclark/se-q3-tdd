#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Kevin Clark"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-l', '--lower', help='lowercase', action='store_true')
    parser.add_argument('-u', '--upper', help='uppercase', action='store_true')
    parser.add_argument('-t', '--title', help='titlecase', action='store_true')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage(args)
        sys.exit(1)

    text = ns.text
    if ns.title:
        print(text.title())
    elif ns.lower:
        print(text.lower())
    elif ns.upper:
        print(text.upper())
    else:
        print(text)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
