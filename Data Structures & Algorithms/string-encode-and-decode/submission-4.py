class Solution:
    strs=["we","say",":","yes","!@#$%^&*()"]
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    "2#we3#say1#:3#yes10#!@#$%^&*()"
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j+1:j+1+length]

            result.append(word)

            i = j + 1 + length

        return result

            
