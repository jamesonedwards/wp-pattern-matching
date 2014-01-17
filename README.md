wp-pattern-matching
===================
A pattern matching exercise.

Computational complexity:
Taking advantage of the fact that we know the length of potentially matched patterns for a given path,
I stored the patterns in a dictionary with length(pattern) as the key. Thus the worst case complexity
(where every pattern is the same length) is O(N*M), where N is the number of patterns and M is the
number of paths. In the best case (where every pattern is a different length), the complexity is O(M).
Assuming an average distribution of pattern lengths, this should be faster than quadratic time.

I made the following assumptions when writing this program:
- Based on the statement "For a pattern to match a path, each field in the pattern must exactly match
  the corresponding field in the path.", I assume that matching is case-sensitive.
- Because it wasn't explicitly stated otherwise, I will assume that paths CAN have asterisks. If a
  path has an asterisk, I will give weight to a direct match (with pattern asterisk) over it being a
  wildcard match. 

Input tests performed:
- multiple leading/trailing slashes in path [PASS]
- blank paths [PASS]
- blank patterns [PASS]
- patterns with whitespace elements [PASS]
- paths with whitespace elements [PASS]
- case-sensitivity [PASS]
- paths containing asterisks [PASS]
- paths containing multiple asterisks [PASS]
- patterns containing multiple asterisks [PASS]
- zero patterns [PASS]
- zero paths [PASS]
