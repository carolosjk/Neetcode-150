from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        if not strs:
            return ""
        
        for s in strs:
            encoded += str(len(s))
            encoded += "_"
        
        encoded += "#"
        
        for s in strs:
            encoded += s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        if s == "":
            return []
        
        sizes = s.split("_#")[0].split("_")

        s = s.split("_#")[1]

        for size in sizes:
            decoded.append(s[:int(size)])
            s = s[int(size):]

        return decoded
      


if __name__ == "__main__":
    solution = Solution()
    encoded = solution.encode(["neet","code","love","you"])
    print(encoded)
    decoded = solution.decode(encoded)
    print(decoded)


    
