# https://leetcode.com/problems/find-common-characters/description/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        set1 = set(words[0]) 
        set2 = set(words[1]) 
        set3 = set(words[2]) 

        intersection = set1 & set2 & set3
        intersection_list = list(intersection)

        result = []

        for candidate_char in intersection_list:
            count_in_word1 = words[0].count(candidate_char) 
            count_in_word2 = words[1].count(candidate_char) 
            count_in_word3 = words[2].count(candidate_char)

            minimum_frequency = min(count_in_word1, count_in_word2, count_in_word3)

            for i in range(minimum_frequency):  
                result.append(candidate_char)
                
        return result
    
'''
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''