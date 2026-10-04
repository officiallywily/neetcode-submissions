class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for string in strs:
            ret += str(len(string)) + "#" + string

        # placeholder
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            frag_len_str = ""
            while s[i] != "#":
                frag_len_str += s[i]
                i += 1
            frag_len = int(frag_len_str)
            ret.append(s[i + 1: i + frag_len + 1])
            i += frag_len + 1
            
        return ret