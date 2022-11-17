'''
Question: Given a string s containing only digits, return the number of ways to decode it.
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Solution: Literally just use dfs + memoisation

Video: https://www.youtube.com/watch?v=YcJTyrG3bZs
'''

# Time: O(n) and Space: O(n)
# Runtime: 66 ms, faster than 35.06% 
# Memory Usage: 14.2 MB, less than 21.30%

def numDecodings(s):
    # dfs
    dp = {len(s):1}
    
    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0
        
        res = dfs(i+1) # non greedy
        print("first",res)
        if (i+1<len(s)) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
            res += dfs(i+2) # greedy
            print("second",res)
        
        dp[i] =res
        return res
    
    return dfs(0)

S= 11106
print(numDecodings(S)) #output 2
