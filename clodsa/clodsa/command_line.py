from __future__ import absolute_import
from . import augment
from . import generate_sample
import argparse
import sys

def main():
    arg1 = sys.argv[1]
    augment.main(arg1)

def main_sample():
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    generate_sample.main(arg1,arg2)
