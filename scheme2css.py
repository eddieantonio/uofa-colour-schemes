#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Converts colo(u)r schemes to CSS files.
"""

import sys
from pathlib import Path

UOFAGREEN = '#007C41'.lower()
UOFAGOLD = '#FFDB05'.lower()

program_name = str(Path(sys.argv[0]).stem)


def usage_error(message=None):
    if message:
        print(f"{program_name}:", message, file=sys.stderr)
    print(f"Usage:\n\t{program_name} infile.tsv > scheme", file=sys.stderr)
    sys.exit(1)


def error(message):
    print(f"{program_name}:", message, file=sys.stderr)
    sys.exit(2)


if program_name not in ('scheme2css', 'scheme2scss'):
    usage_error("I should be named either 'scheme2css' or 'scheme2scss'")

colors = {}

if len(sys.argv) != 2:
    usage_error("you must provide exactly one .tsv file")

# Read in all the colours.
with open(sys.argv[1]) as scheme_file:
    for line in scheme_file:
        name, color = line.strip().split()
        colors[name] = color.lower()

# Let's make sure the green and gold are in there.
if not {UOFAGREEN, UOFAGOLD}.issubset(colors.values()):
    error("Colour schemes MUST have UofA's green and gold.")

print('@charset "UTF-8";')
print(':root {')
for name, color in colors.items():
    print(f'  --{name.lower()}: {color};')
print('}')
