#!/usr/bin/python3

import collections
import argparse
  
def process(jsin):
    f = open(jsin,encoding='utf-8')
    # Find base64 data, ...


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser(description="Investigate ASAR")
    parser.add_argument(
        "--in",
        dest="jsin",
        type=str,
        help="JS to investigate",
        required=True,
    )

    args = parser.parse_args()
    process(args.jsin)
