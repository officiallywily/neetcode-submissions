class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded: List[str] = []
        i = 0
        while i < len(s):
            frag_len_str = ""
            while s[i] != '#':
                frag_len_str += s[i]
                i += 1
            frag_len: int = int(frag_len_str)
            decoded.append(s[i + 1: i + frag_len + 1])
            i += frag_len + 1
        return decoded

