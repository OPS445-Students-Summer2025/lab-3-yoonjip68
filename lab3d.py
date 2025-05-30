#!/usr/bin/env python3
'''Lab 3 script to check free disk space on root directory'''
# Author ID: ypark68

import subprocess

def free_space():
    # Launch the command and capture the output
    result = subprocess.check_output("df -h | grep '/$' | awk '{print $4}'", shell=True)
    return result.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())

