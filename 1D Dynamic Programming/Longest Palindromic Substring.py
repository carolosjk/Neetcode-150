
class Solution:

    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        max_str = s[0]

        for i in range(l):
            a = i
            b = l-1
            cur_str = s[a]
            while b > a:
                print(i,a,b,cur_str)
                if s[b] == s[a]:
                    a += 1
                    b -= 1
                    cur_str += s[a]
                else:
                    a = i
                    b += len(cur_str)-2 
                    cur_str = s[a]

            
            if b == a: # even length
                cur_str = cur_str[:-1] + cur_str[::-1]
                if len(cur_str) > len(max_str):
                    max_str = cur_str
            if b < a:
                cur_str = cur_str[:-1]
                cur_str += cur_str[::-1]
                if len(cur_str) > len(max_str):
                    max_str = cur_str
        
        return max_str


            



# abcbcaba

if __name__ == "__main__":
    solution = Solution()
    # print(solution.longestPalindrome("a"))
    # print(solution.longestPalindrome("aba"))
    print(solution.longestPalindrome("aacabdkacaa"))
    # print(solution.longestPalindrome("abaaabbbcab"))
    
