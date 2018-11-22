#!/usr/bin/env python3

import sys
import glob
import asyncio
import cv2
import time
import numpy as np

def load_file(path):
    with open(path, 'rb') as fd:
        img_str = fd.read()
    nparr = np.fromstring(img_str, np.uint8)
    return cv2.imdecode(nparr, 1)

def main(argv):
    """ Main function call."""
    file_paths = glob.glob(argv[1] + "/*.png")
    return [load_file(path) for path in file_paths]

if __name__ == '__main__':
    t1 = time.time()
    response = main(sys.argv)
    print("Got %d files in %.3f seconds." % (len(response), time.time() - t1))

