# Updating list of LeetCode I've solved.


### **Array**

- [Two Sum](https://leetcode.com/problems/two-sum/) - **Use hashmap to hash each value, but before hashing check, if the difference has already been hashed.**
- [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - **Find local min and search for local max, sliding window;**
- [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) - **Use** **sets operation then compare lengths**
- [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) - **make two passes, first in order, second in reverse, to compute products. (you will need the prefix & suffix to compute these values)**
- [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) - **Pattern: prev subarray cant be negative, dynamic programming: compute max sum for each prefix**
- [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) - **Dynamic programming problem, keeping track of max and min product.**
- [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) - **Use binary search to determine you’re in the LHS or RHS of the sorted sub array.**
- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - **Use binary search determine if you’re in the LHS or RHS and handle them**
- [3 Sum](https://leetcode.com/problems/3sum/) - **One loop and perform 2 sum on each iteration**
- [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) - **Shrinking Window:** **use pointers favouring the biggest height**

---

### **Binary**

- [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) - **add bit by bit, be mindful of carry, after adding, if carry is still 1, then add it as well.**
- [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) - **Use bitwise & 1. Incrementing the count value of 1.**
- [Counting Bits](https://leetcode.com/problems/counting-bits/) - **Write binary values of 0-16 to find pattern; res[i] = res[i - offset], where offset is the biggest power of 2 <= I;**
- [Missing Number](https://leetcode.com/problems/missing-number/) - **Compute expected sum - real sum;**
- [Reverse Bits](https://leetcode.com/problems/reverse-bits/) - **reverse each of 32 bits;**
---

### **Dynamic Programming**

- [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)  - **Bottom-up approach. Compute for the last 2 which always have just […1,1] ways. Then work backwards by adding the dp[i+1] + dp[i+2]**
- [Coin Change](https://leetcode.com/problems/coin-change/) - **Bottom-up approach(tabulation). Compute coins for amount 1→ n, then compare (amount-coin). Can also do it with a Top-down approach(memoization).**
- [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) - **solve from RHS, as nums[-1] only has 1 subsequence use this to solve for the rest taking the max subsequence from DP[]**
- [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) - **Bottom-up approach. Use 2d matrix e.g abc0 x abc0, and fill each index with values to allow matrix[0][0] hold the value. (if match move diagonally else move sideways right & down)**
- [Word Break Problem](https://leetcode.com/problems/word-break/) - **desc**
- [Combination Sum](https://leetcode.com/problems/combination-sum-iv/) - **desc**
- [House Robber](https://leetcode.com/problems/house-robber/) - **DP problem, The last 2 houses have a sum of their actual value as they don't have adjacent houses that meet the requirement.**
- [House Robber II](https://leetcode.com/problems/house-robber-ii/) - **desc**
- [Decode Ways](https://leetcode.com/problems/decode-ways/) - **desc**
- [Unique Paths](https://leetcode.com/problems/unique-paths/) - **desc**
- [Jump Game](https://leetcode.com/problems/jump-game/) - **desc**

---

### **Graph**

- [Clone Graph](https://leetcode.com/problems/clone-graph/)
- [Course Schedule](https://leetcode.com/problems/course-schedule/)
- [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- [Alien Dictionary (Leetcode Premium)](https://leetcode.com/problems/alien-dictionary/)
- [Graph Valid Tree (Leetcode Premium)](https://leetcode.com/problems/graph-valid-tree/)
- [Number of Connected Components in an Undirected Graph (Leetcode Premium)](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

---

### **Interval**

- [Insert Interval](https://leetcode.com/problems/insert-interval/)
- [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- [Meeting Rooms (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms/)
- [Meeting Rooms II (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms-ii/)

---

### **Linked List**

- [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [Detect Cycle in a Linked List](https://leetcode.com/problems/linked-list-cycle/)
- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) - **Traverse both lists and create a new list while comparing value each node**
- [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [Reorder List](https://leetcode.com/problems/reorder-list/)

---

### **Matrix**

- [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
- [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [Rotate Image](https://leetcode.com/problems/rotate-image/)
- [Word Search](https://leetcode.com/problems/word-search/)

---

### **String**

- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [Encode and Decode Strings (Leetcode Premium)](https://leetcode.com/problems/encode-and-decode-strings/)

---

### **Tree**

- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [Same Tree](https://leetcode.com/problems/same-tree/)
- [Invert/Flip Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [Add and Search Word](https://leetcode.com/problems/add-and-search-word-data-structure-design/)
- [Word Search II](https://leetcode.com/problems/word-search-ii/)

---

### **Heap**

- [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)



### **Extras**