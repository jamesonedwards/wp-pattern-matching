'''
Created on Dec 14, 2013

@author: jedwards
'''
import sys
import operator
import math
import decimal
# import logging

# TODO: Figure out logging (to file?) vs stdout for results.
# TODO: Write and then refactor into methods.
# TODO: Add try-catch? (Probably not necessary since program can just crash. 
# FIXME: Once the quadratic solution works, refactor to store patterns in has tavke with pattern length as key.
# TODO: Watch for blank patterns and/or paths.
# TODO: Match case exactly?
# TODO: Can paths have asterisk fields!?


class PatternMatcher(object):
    # Constants.
    PATTERN_SEP = ','
    PATH_SEP = '/'
    WILDCARD = '*'
    NO_MATCH = 'NO MATCH'
    # Class members.
    patterns = []
    paths = []
    
    def match(self, lines):
        ''' Start the program. '''
        # Get patterns.
        pattern_cnt = int(lines[0])
        self.patterns = [self._parse_pattern(line) for line in lines[1:pattern_cnt + 1]] 
        # Get paths.
        path_cnt = int(lines[pattern_cnt + 1])
        # Note: If we can assume the input file will not contain extra characters at the end, then we can take a split until the end instead.
        self.paths = [self._parse_path(line) for line in lines[pattern_cnt + 2:pattern_cnt + 2 + path_cnt]]
        # Loop through paths and find best match.
        for path in self.paths:
            print self._find_best_match(path)
    
    def _find_best_match(self, path):
        # Check each pattern against this path.
        best_score = decimal.Decimal(sys.maxint)
        best_pattern = self.NO_MATCH
        for pattern in self.patterns:
            # Pattern and path have to be the same length.
            if len(pattern) == len(path):
                tmp_score_tuple = self._get_score(pattern, path)
                '''
                To prevent ties between patterns with an equal number of wildcards, we create a decimal value consisting of:
                (wildcard count as integer component) . (weighted value based on position of wildcards as decimal component)
                This way, the wildcard count has greater weight.
                '''
                tmp_score = decimal.Decimal(str(tmp_score_tuple[0]) + '.' + str(int(tmp_score_tuple[1]))) 
                if tmp_score < best_score:
                    best_score = tmp_score
                    best_pattern = pattern 
        return best_pattern 

    def _get_score(self, pattern, path):
        '''
        Scoring - for each character:
            Exact match: + (0, 0) and recurse
            Wildcard match: + (1, 10^len(pattern - 1) and recurse
            No match: return sys.maxint
            
            UPDATE:
            *,*,y,z 2.1100
            *,x,*,z 2.1010
        '''
        if pattern == None or len(pattern) == 0:
            # Exit condition: Done with this pattern.
            return (0, 0);
        elif pattern[0] == path[0]:  # TODO: Watch casing?
            return tuple(map(operator.add, (0, 0), self._get_score(pattern[1:], path[1:])))
        elif pattern[0] == self.WILDCARD:
            return tuple(map(operator.add, (1, math.pow(10, len(pattern) - 1)), self._get_score(pattern[1:], path[1:])))
        else:
            # Exit condition: No match.
            return (sys.maxint, 0)

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
    # HACK: When debugging in Aptana/PyDev, there's no stdin so read from file.
    if ide:
        lines = [line.strip() for line in open('input_file.txt')]
    else:
        lines = [line.strip() for line in sys.stdin]
    patternMatcher.match(lines)
