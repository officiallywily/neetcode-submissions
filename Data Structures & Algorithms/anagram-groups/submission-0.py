class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[str, List[str]] = {}
        for string in strs:
            sorted_string: str = "".join(sorted(string))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = []
            anagrams[sorted_string].append(string)
        
        return_list: List[List[str]] = []
        for anagram_chunk in anagrams.values():
            return_list.append(anagram_chunk)
        
        return return_list