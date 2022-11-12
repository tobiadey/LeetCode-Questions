'''
Bottom-up approach. 
Use 2d matrix e.g abc0 x abc0,  [a,b,c,0][a,b,c,0][0,0,0,0]
Fill each index with values to allow matrix[0][0] hold the value. 
(if match move diagonally else move sideways right & down)

"abcde"  "ace"
3
'''


# Time: O(n*m) and Space: O(n*m) n,m are lengths of the strings
# Runtime: 498 ms
# Memory Usage: 22.6 MB MB
def longestCommonSubsequence(text1,text2):
    '''
    bottom up dp solution 
    '''
    n1 = len(text1)
    n2 = len(text2)
    dp = [[0 for x in range(n2+1)] for y in range(n1+1)] 
    
        
    for i in range(n1-1,-1,-1): #5 abcde
        for j in range(n2-1,-1,-1): #3 ace
            # print(i,j)
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
                # print(text1[i],text2[j])
                # print(i,j)
                # print(dp)
            else:
                dp[i][j] = max(dp[i][j+1],dp[i+1][j])
                
        
        
        
    
    # print(dp)

    
    return dp[0][0]

TEXT_1 = "abcde"
TEXT_2 = "ace"

print(longestCommonSubsequence(TEXT_1,TEXT_2)) #output 3