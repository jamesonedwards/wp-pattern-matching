'''
Created on Dec 14, 2013

@author: jedwards

NOTES:
I made the following assumptions when writing this program:
- Based no the statement "For a pattern to match a path, each field in the pattern must exactly match the corresponding field in the path.", I assume that matching is case-sensitive. 
- Because it wasn't explicitly stated otherwise, I will assume that paths CAN have asterisks. If a path has an asterisk, I will give weight to a direct match (with pattern asterisk) over it being a wildcard match. 

'''

import sys
import operator
import math
import decimal

'''
TODO: Create a bunch of test files with known outputs:
- multiple leading/trailing slashes in path
- blank paths
- patterns with whitespace elements
- paths with whitespace elements
- blank paths
- case-sensitivity
- paths containing asterisks
- paths containing multiple asterisks
- patterns containing multiple asterisks
'''
# TODO: Clean up and comment.

class PatternMatcher(object):
    # Constants.
    PATTERN_SEP = ','
    PATH_SEP = '/'
    WILDCARD = '*'
    NO_MATCH = 'NO MATCH'
    # Class members.
    patterns = {}
    paths = []
    
    def match(self, lines):
        '''
        The entry point for the pattern matching algorithm.
        '''
        # Store patterns in a dictionary with len(pattern) as key.
        pattern_cnt = int(lines[0])
        for line in lines[1:pattern_cnt + 1]:
            tmp_pattern = self._parse_pattern(line)
            tmp_pattern_lenth = len(tmp_pattern) 
            if tmp_pattern_lenth in self.patterns:
                self.patterns[tmp_pattern_lenth].extend([tmp_pattern])
            else:
                self.patterns[tmp_pattern_lenth] = [tmp_pattern]
        # Store paths in a flat list.
        path_cnt = int(lines[pattern_cnt + 1])
        # Note: If we can assume the input file will not contain extra characters at the end, then we can take a split until the end instead.
        self.paths = [self._parse_path(line) for line in lines[pattern_cnt + 2:pattern_cnt + 2 + path_cnt]]
        # Loop through paths and find best match.
        for path in self.paths:
            # Reformat the pattern and print.
            match = self._find_best_match(path)
            if match == None:
                print self.NO_MATCH
            else:
                print self.PATTERN_SEP.join(match)

    def _find_best_match(self, path):
        '''
        Check each pattern against this path.
        '''
        best_score = decimal.Decimal(sys.maxint)
        best_pattern = None
        # Optimization: Since the pattern and path have to be the same length for there to be a match, we only look patterns of that length.
        for pattern in self.patterns[len(path)]:
            tmp_score_tuple = self._get_score(pattern, path)
            # If the score is (0, 0), we have a perfect match. No need to continue the search.
            if tmp_score_tuple[0] == 0 and tmp_score_tuple[1] == 0:
                return pattern
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
        Get the score for this pattern/path combination.
        Scoring works like this:
            For each character:
                Exact match: + (0, 0) and recurse
                Wildcard match: + (1, 10^len(pattern - 1) and recurse
                No match: return (sys.maxint, 0)
        '''
        if pattern == None or len(pattern) == 0:
            # Exit condition: Done with this pattern.
            return (0, 0);
        elif pattern[0] == path[0]:
            return tuple(map(operator.add, (0, 0), self._get_score(pattern[1:], path[1:])))
        elif pattern[0] == self.WILDCARD:
            return tuple(map(operator.add, (1, math.pow(10, len(pattern) - 1)), self._get_score(pattern[1:], path[1:])))
        else:
            # Exit condition: No match.
            return (sys.maxint, 0)

    def _parse_pattern(self, pattern):
        '''
        Split string at separator.
        '''
        return pattern.split(self.PATTERN_SEP)
    
    def _parse_path(self, path):
        '''
        Strip leading/trailing slashes and split string at separator.
        '''
        return path.strip('/').split(self.PATH_SEP)

if __name__ == '__main__':
    '''
    The main entry point for the prorgam.
    '''
    # FIXME: Make sure this is False before submitting!
    # ide = False
    ide = True
    patternMatcher = PatternMatcher()
    if ide:
        # HACK: When debugging in Aptana/PyDev, there's no stdin so read from file.
        lines = [line.strip() for line in open('input_file.txt')]
    else:
        # Get lines from stdin.
        lines = [line.strip() for line in sys.stdin]
    patternMatcher.match(lines)
