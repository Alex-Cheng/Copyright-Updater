from __future__ import print_function

import sys  
import os
import fileinput
from datetime import date
from P4 import P4
from subprocess import call

p4 = P4()
p4.connect()
pwd = os.getcwd()

start_copyright = " * Copyright (C)"
correct = " * Copyright (C) {0} by Autodesk, Inc. All Rights Reserved.".format(date.today().year)


def copyright_status(filepath):
    """Return values:
    0: valid copyright
    1: invalid copyright statement
    2: no copyright statement
    3: everything else
    """
    with open(filepath) as f:
        for line in f:
            if line.startswith(start_copyright):
                return 0 if line.startswith(correct) else 1
            else:
                if line.startswith('using') or line.startswith('namespace'):
                # Meets starting of code section
                    return 2
                continue
    return 3 # Who knows what else will happen


def get_files(changelist):
    """Get files in a specified changelist, with absolute paths of each file."""
    return [pwd + os.path.normpath(f[1:])
            for f in p4.run_describe(str(changelist))[0]["depotFile"]
            if os.path.splitext(f)[1] == '.cs']


def update_copyright(filepath):
    "Updates copyright line. Returns True if succeeded, False otherwise."
    modified = False
    for line in fileinput.input(filepath, inplace=1):
        if line.startswith(start_copyright) and modified == False:
            print(correct)
            modified = True
        else:
            print(line, end='')
    return modified


def main(args):
    status = 0
    changelist = args[1]
    filepaths = get_files(changelist)
    print("Updating copyright statements for {0} file(s).".format(len(filepaths)))
    for f in filepaths:
        st = copyright_status(f)
        if st == 0:
            print("{0} - {1}".format(f, "No update required."))
        elif st == 1:
            result = update_copyright(f)
            if result == True:
                print("{0} - {1}".format(f, "Update success!"))
            else:
                print("{0} - {1}".format(f, "Update error!"), file=sys.stderr)
                status = 1
        elif st == 2:
            print("{0} - {1}".format(f, "Copyright missing, skipped!"), file=sys.stderr)
            status = 0  # Warn, but not treated as error
        else:
            raise NotImplementedError
    return status


if __name__ == '__main__':
    sys.exit(main(sys.argv))
        
