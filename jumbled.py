import os
import sys
import time
import string
import argparse
import itertools
def createWordList(chrs):
    output = 'output/wordlist.txt'
    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))
    print ('[+] Creating wordlist at `%s`...' % output)
    print ('[i] Starting time: %s' % time.strftime('%H:%M:%S'))
    output = open(output, 'w')
    for xs in itertools.permutations(chrs):
        chars = ''.join(xs)
        output.write("%s\n" % chars)
        sys.stdout.write('\r[+] saving character `%s`' % chars)
        sys.stdout.flush()
    output.close()
    print ('\n[i] End time: %s' % time.strftime('%H:%M:%S'))
    print("started -- init.py ")
    os.system("sort  output/wordlist.txt > output/sortlist.txt")
    os.system("init.py")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Python Wordlist Generator for permutations only')
    parser.add_argument(
        '-chr', '--chars',
        default=None, help='characters to iterate')
    args = parser.parse_args()
    if args.chars is None:
        args.chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
    createWordList(args.chars)
