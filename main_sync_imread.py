#!/usr/bin/env python3

import sys
import glob
import asyncio
import cv2
import time
import numpy as np

def main(argv):
    """ Main function call."""
    file_paths = glob.glob(argv[1] + "/*.png")
    return [cv2.imread(path) for path in file_paths]

if __name__ == '__main__':
    t1 = time.time()
    response = main(sys.argv)
    print("Got %d files in %.3f seconds." % (len(response), time.time() - t1))

