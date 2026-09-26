class Solution:
    def encode(self, strs: List[str]) -> str:
        global lengths
        lengths = []
        for i in strs:
            lengths.append(len(i))
        encoded_string = "".join(strs)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        for i in lengths:
            popped, s = s[:i], s[i:]
            decoded_strs.append(popped)
        return decoded_strs