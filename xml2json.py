#!/usr/bin/python
import os
import xmltodict
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    "-f", "--file",
    dest="filename",
    help="Xml file to convert",
    metavar="XMLFILE",
    required=True
)

parser.add_argument(
    "-o", "--output",
    dest="output",
    help="Json filename to export",
    metavar="JSONFILE",
    nargs='?',
    const="output.json",
    default="output.json",
    required=False,
)

args = parser.parse_args()

if not os.path.exists(args.filename):
    print(f"File {args.filename} not found")
    exit(1)

with open(args.filename, "r") as f:
    data = f.read()

    try:
        json_data = xmltodict.parse(data)
    except Exception as e:
        print(f"Error parsing xml file: {e}")
        exit(1)

    if args.output:
        # Export to file
        with open(args.output, "w") as f:
            f.write(str(json_data))
    else:
        # Print to console
        print(json_data)
