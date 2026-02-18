# https://leetcode.com/problems/find-common-characters/description/

from typing import List
import collections

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        master_counts = collections.Counter(words[0])

        for i in range(1, len(words)):

            master_counts &= collections.Counter(words[i])
        
        return list(master_counts.elements())


    
'''
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''