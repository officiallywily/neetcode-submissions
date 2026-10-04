class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results: Dict[ Tuple, List[str] ] = {}
        for string in strs:
            count = [0] * 26
            for letter in string:
                count[ord(letter) - ord('a')] +=  1
            
            results.setdefault(tuple(count), []).append(string)
        
        return list(results.values())