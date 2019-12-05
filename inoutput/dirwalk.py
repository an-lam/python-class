#!/usr/bin/env python
"""Demonstrates the os.walk function, one of many
very useful things given to us in the os module.
"""
import time  
import os 
        
def print_path(this_dir, dir_names, file_names):
    print("In " + os.path.abspath(this_dir))
    for file_name in sorted(dir_names + file_names):
        whole_name = os.path.join(this_dir, file_name)
        if os.path.isdir(whole_name):
            print("   directory: " + file_name)
        else:
            print("   %s:\n        %s" % (
                file_name, time.ctime( 
                os.path.getmtime(whole_name))))

if __name__ == '__main__':
    for (this_dir, dir_names, file_names) in os.walk("."):
        print_path(this_dir, dir_names, file_names)
