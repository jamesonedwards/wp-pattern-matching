'''
Created on Dec 14, 2013

@author: jedwards
'''
import sys
import logging

# Constants.
PATTERN_SEP = ','
PATH_SEP = '/'
NO_MATCH = 'NO MATCH'

# Global variables.
patterns = []
paths = []


# TODO: Figure out logging (to file?) vs stdout for results.
# TODO: Write and then refactor into methods.
# TODO: Add try-catch? (Probably not necessary since program can just crash. 
# FIXME: Once the quadratic solution works, refactor to store patterns in has tavke with pattern length as key. 

def main():
    ''' Start the program. '''
    # logging.info('Entered main')
    # Get lines from stdin.
    lines = [line.strip() for line in sys.stdin]
    # Get patterns.
    patternCnt = int(lines[0])
    print patternCnt
    patterns = [parse_pattern(line) for line in lines[1:patternCnt + 1]] 
    print patterns
    # Get paths.
    pathCnt = int(lines[patternCnt + 1])
    print pathCnt
    # Note: If we can assume the input file will not contain extra characters at the end, then we can take a split until the end instead.
    paths = [parse_path(line) for line in lines[patternCnt + 2:patternCnt + 2 + pathCnt]]
    print paths
    
    # Loop through paths and find best match.
    for path in paths:
        print find_best_match(path)
    
    return

def find_best_match(path):
    return NO_MATCH

def parse_pattern(pattern):
    # Split string at separator.
    return pattern.split(PATTERN_SEP)

def parse_path(path):
    # String leading/trailing slashes and split string at separator.
    return path.strip('/').split(PATH_SEP)

if __name__ == '__main__':
    main()
