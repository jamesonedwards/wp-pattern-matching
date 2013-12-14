'''
Created on Dec 14, 2013

@author: jedwards
'''
import sys
# import logging

# TODO: Figure out logging (to file?) vs stdout for results.
# TODO: Write and then refactor into methods.
# TODO: Add try-catch? (Probably not necessary since program can just crash. 
# FIXME: Once the quadratic solution works, refactor to store patterns in has tavke with pattern length as key.
# TODO: Watch for blank patterns and/or paths.
# TODO: Match case exactly?


class PatternMatcher(object):
    # Constants.
    PATTERN_SEP = ','
    PATH_SEP = '/'
    NO_MATCH = 'NO MATCH'
    # Class members.
    patterns = []
    paths = []
    
    def match(self, lines):
        ''' Start the program. '''
        # logging.info('Entered main')
        # Get patterns.
        patternCnt = int(lines[0])
        # print patternCnt
        self.patterns = [self._parse_pattern(line) for line in lines[1:patternCnt + 1]] 
        # print patterns
        # Get paths.
        pathCnt = int(lines[patternCnt + 1])
        # print pathCnt
        # Note: If we can assume the input file will not contain extra characters at the end, then we can take a split until the end instead.
        self.paths = [self._parse_path(line) for line in lines[patternCnt + 2:patternCnt + 2 + pathCnt]]
        # print paths
        
        # Loop through paths and find best match.
        for path in self.paths:
            print self._find_best_match(path)
    
    def _find_best_match(self, path):
        return path
        # Check each pattern against this path.
        # for pattern in self.patterns:
        #    if len(pattern) == len(path):
        #        return 'maybe?'
    
    def _parse_pattern(self, pattern):
        # Split string at separator.
        return pattern.split(self.PATTERN_SEP)
    
    def _parse_path(self, path):
        # String leading/trailing slashes and split string at separator.
        return path.strip('/').split(self.PATH_SEP)

if __name__ == '__main__':
    ide = True
    patternMatcher = PatternMatcher()
    # Get lines from stdin.
    # HACK: When debugging in Eclipse, there's no stdin so read from file.
    lines = None
    if ide:
        lines = [line.strip() for line in open('input_file.txt')]
    else:
        lines = [line.strip() for line in sys.stdin]
    patternMatcher.match(lines)
