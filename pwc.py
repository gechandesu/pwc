#!/usr/bin/env python3

# This program is free software. It comes without any warranty, to
#   the extent permitted by applicable law. You can redistribute it
#   and/or modify it under the terms of the Do What The Fuck You Want
#   To Public License, Version 2, as published by Sam Hocevar. See
#   http://www.wtfpl.net/ for more details.

import sys
import getopt
import subprocess

import random
import string

def generate_pass(special_chars: bool, lenght: int, print_pass: bool) -> str:
    abc = string.ascii_letters + string.digits
    if special_chars:
        abc = abc + string.punctuation
    pw = ''
    for char in range(lenght):
        pw = pw + random.choice(abc)

    if print_pass:
        print(pw)
    else:
        # Run xclip. Copy generated password to X clipboard!
        command = 'xclip -selection clipboard'.split()
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        process.stdin.write(pw.encode())  # Put password to STDIN.

def usage():
    print('Usage: pwc [-h|--help] [-s|--special] [-p|--print] [<lenght>]')

def print_help():
    print('Generate password and copy it to clipboard (xclip).')
    print()
    usage()
    print()
    print('    -s, --special    use punctuation characters in password.')
    print('    -p, --print      print password to STDOUT instead of copy to clipboard.')
    print('    -h, --help       print this help message and exit.')

def main():
    # Set default values.
    special_chars = False
    print_pass = False
    lenght = 12

    # Parse agrs.
    try:
        opts, args = getopt.getopt(
            sys.argv[1:], 
            "hsp", 
            ["help", "special", "print"]
        )
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
        special_chars=False
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        if opt in ("-s", "--special"):
            special_chars=True
        if opt in ("-p", "--print"):
            print_pass=True
    if len(args) >= 2:
        print('Too many arguments.')
        usage()
        sys.exit(2)
    for arg in args:
        try:
            lenght = int(arg)
        except ValueError:
            print('Argument must be an integer.')
            usage()
            sys.exit(1)

    # Run password generator.
    generate_pass(special_chars, lenght, print_pass)

if __name__ == "__main__":
    main()
