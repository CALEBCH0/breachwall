import ctypes
import os
import struct
import sys
# import commands
import gconf

# import win32con

import wget
from os import walk, getenv, system
from shutil import copyfile
from PIL import Image

import breachWall.breacher


def main():
    breachWall.breacher.runit()
    # breachWall.breacher.breach_wall()


if __name__ == '__main__':
    main()
