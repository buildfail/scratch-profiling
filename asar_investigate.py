#!/usr/bin/python3
import os
import io
import re
import mmap
import base64
import collections
import argparse
  
def process(jsin,base64out):
    # Find base64 data, ...
    
    #f = open(jsin,'rb')    
    #reader = io.BufferedReader(f)
    #wrapper = io.TextIOWrapper(reader)
    #wrapper.read()

    f = open(jsin,'rb')
    dat = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    counter = 1
    pattern = re.compile(br'(base64,([a-zA-Z0-9\+\/]+=*))',re.MULTILINE)

    for m in pattern.finditer(dat):

        start = m.start()
        end = m.end()
        base64dat = m.group(2)
        #print(dat[start:start+30])

        try:
            tmp = open(os.path.join(base64out,"%d.out" % counter),'wb')
            tmp.write(base64.b64decode(base64dat))
            tmp.close()
        except Exception:
            nop = 0

        counter += 1

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
    parser.add_argument(
        "--out",
        dest="base64out",
        type=str,
        help="Directory to output base64 decoded data",
        required=True,
    )
    args = parser.parse_args()
    process(args.jsin,args.base64out)
