'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Dp bottom up problem- last value of True, 
Update each dp[i] by checking if s[i]:offsetcan form a word available in the word dict.
'''


# Time: O(n^2 * m)  and Space: O(n)
# Runtime: 58 ms, faster than 77.12% 
# Memory Usage: 13.9 MB, less than 95.16%
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False]*(n+1)
    dp[-1]= True
    
    for i in range(n-1,-1,-1):
        for word in wordDict:
            word_len = len(word)
            if s[i:i+word_len] == word and dp[i+word_len]: 
                dp[i]=True
                
    return dp[0]

s = "applepenapple"
INPUT_LIST= ["apple","pen"]
print(wordBreak(s,INPUT_LIST)) #output True

        

        