from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        targetLength = len(s1)
        charCount = {}
        for c in s1:
            charCount[c] = charCount.get(c,0) + 1

        l = 0
        for r in range(len(s2)):
            if s2[r] in charCount:
                charCount[s2[r]] -= 1
                targetLength -= 1
                while charCount[s2[r]] < 0:
                    charCount[s2[l]] += 1
                    targetLength += 1
                    l += 1
                if targetLength == 0:
                    return True
            else:
                while l<=r:
                    if s2[l] in charCount:
                        charCount[s2[l]] += 1
                        targetLength += 1
                    l += 1
        
        return False


# count = {"a":1, "b":1, "c":1} targetLength = 3 l=0 r=0 substring = "l" charRead = "l"
# count = {"a":1, "b":1, "c":1} targetLength = 3 l=1 r=1 substring = "e" charRead = "e"
# count = {"a":1, "b":1, "c":0} targetLength = 2 l=2 r=2 substring = "c" charRead = "c"
# count = {"a":0, "b":1, "c":0} targetLength = 1 l=2 r=3 substring = "ca" charRead = "a"
# count = {"a":-1, "b":1, "c":0} targetLength = 0 l=2 r=4 substring = "caa" charRead = "a"


# count = {"a":1, "b":1, "c":1} targetLength = 3
# count = {"a":1, "b":1, "c":1} targetLength = 3 -> l
# count = {"a":1, "b":1, "c":1} targetLength = 3 -> le
# count = {"a":1, "b":1, "c":0} targetLength = 2 -> lec
# count = {"a":0, "b":1, "c":0} targetLength = 1 -> leca
# count = {"a":0, "b":0, "c":0} targetLength = 0 -> lecab -> True - test1


# count = {"a":-1, "b":1, "c":0} targetLength = 1 -> lecaa - test 2
# count = {"a":-1, "b":1, "c":0} targetLength = 1 -> ecaa
# count = {"a":-1, "b":1, "c":0} targetLength = 1 -> caa
# count = {"a":-1, "b":1, "c":1} targetLength = 2 -> aa
# count = {"a":0, "b":1, "c":1} targetLength = 2 -> a
# count = {"a":0, "b":0, "c":1} targetLength = 1 -> ab
# count = {"a":0, "b":0, "c":1} targetLength = 1 -> abe
# count = {"a":0, "b":0, "c":1} targetLength = 1 -> abee


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion("abc", "lecabee"))
    print(solution.checkInclusion("abc", "lecaabee"))
