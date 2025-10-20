class Solution:
    def isAnagram(self, s: str, t:str) -> bool:

        if len(s) != len(t):
            return False

        character_count = {}
        for c in s:
            character_count[c] = character_count.get(c,0) + 1

        for c in t:
            character_count[c] = character_count.get(c,0) - 1
            if character_count[c] < 0:
                return False
            
        for count in character_count.values():
            if count != 0:
                return False
            
        return True
    

if __name__ == "__main__":

    solution = Solution()
    print(solution.isAnagram("test","test"))
    print(solution.isAnagram("test","testt"))
    print(solution.isAnagram("tets","test"))
    print(solution.isAnagram("aabbcc","ccbbaa"))
    print(solution.isAnagram("adsasd","asdasdasd"))

