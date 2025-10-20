from typing import List

class Solution:

    def getCharacterCount(self, s: str) -> dict:
        characterCount = {}
        for c in s:
            characterCount[c] = characterCount.get(c,0) + 1
        
        return tuple(sorted(characterCount.items()))


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDictionary = {}

        for s in strs:
            count = self.getCharacterCount(s)
    
            if count not in anagramDictionary:
                anagramDictionary[count] = []
            anagramDictionary[count].append(s)

        return list(anagramDictionary.values())
    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["aa","aa","a","cab","abc"]))
