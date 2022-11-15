'''
Given a string s that represents a DNA sequence, 
return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
'''

# Time: O(n) and Space: O(1)
# Runtime: 74 ms, faster than 91.73%
# Memory Usage: 26.1 MB, less than 74.53%
def findRepeatedDnaSequences(s):
    '''
    store all substrings of len 10 in a hashset
    &
    if already in hashset then add to res, which stops duplicates
    
    '''
    n = len(s)
    finder = set()
    res = set()
    
    for i in range(n-9):
        value = str(s[i:i+10])
        if value in finder: 
            res.add(value)
        else:
            finder.add(value)

    return list(res)
        
INPUT_LIST= "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(INPUT_LIST)) #output ["AAAAACCCCC","CCCCCAAAAA"]
