'''
3Sum - Given an integer array nums,
return all the triplets such that
i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Hashmap- Loop through array and perform 2 sum on all possible values.
Apeending results(sorted) to a set to avoid duplicates.

Try next using pointers over hashmap:
sort input,
for each first element,
find next two where -a = b+c,
if a=prevA, skip a, if b=prevB
skip b to elim duplicates;
to find b,c use two pointers,
left/right on remaining list;
'''


import itertools

# Time: O(n*n) and Space: O(n)
# Runtime: 8240 ms
# Memory Usage: 18.3 MB
def three_sum(nums):
    '''
    three_sum(): List -> [List[int]]
    '''

    answer = set()
    # loop over whole list
    for i, val1 in enumerate(nums):

        # calculate differece needed to add up to 0
        target = 0 - val1

        # perform 2 sum with target of "_target above"
        storage = {}

        for j, val2 in itertools.islice(enumerate(nums), i+1, None):
            if i==j:
                continue

            # check if they sum up to target
            bal = target - val2

            if bal in storage and storage[bal]!= j:

                answer.add(tuple(sorted([val1, val2, bal])))
            else:
                storage[val2] = j

    return answer

INPUT_LIST = [-1,0,1,2,-1,-4]
print(three_sum(INPUT_LIST))
