'''
Given an array "arr" of positive integers with length N, your goal is to achieve the maximum possible score by removing elements from either the beginning or the end of the array. The score for removing an element is calculated as:

Score = element * length(arr) + minimum(arr)

Here, "arr" is considered before the current operation, and you can choose to remove elements from the start or end of the array.
"element" represents the value of the removed element. 

Example 1:

Input:
N = 2
arr = {1, 2}
Output: 7
Explanation: A possilbe way to perform the operations
-> remove first element, 
score = 1*length({1,2}) + min({1,2}) = 3
updated arr = {2}

-> remove last element 
score = 2*length({2}) + min({2}) = 4

-> total score = 3 + 4 = 7 

Example 2:

Input:
N = 3
arr = {2,3,4}
Output: 26
Explanation: A possilbe way to perform the operations
-> remove 4 from last, 
score = 4*length({2,3,4})+min({2,3,4}) = 14
updated arr = {2,3}

-> remove 2 from start, 
score = 2*length({2,3})+min({2,3}) = 6
updated arr = {3}

-> remove last element 3, 
score = 3*length({3})+min({3}) = 6

-> total score = 14 + 6 + 6 = 26   

Your Task: 
You don't need to read input or print anything. Complete the function MaxScore(), which takes integer N and an array of integers arr as input parameters and returns the maximum score you can get after performing all operations.
'''
from queue import PriorityQueue


class Solution:
    def MaxScore(self, N, arr):
        pq = PriorityQueue()

        for i in range(N):
            pq.put((arr[i], i))

        def find_arr_min(i, j):
            while pq.qsize() > 0:
                elm, index = pq.queue[0]
                if i <= index <= j:
                    return elm
                pq.get()

        def find_score(arr, i, j, score):
            if i == j:
                return arr[i] + arr[i] + score
            if i > j:
                return score
            left_score = (arr[i] * (j-i+1)) + find_arr_min(i, j)

            right_score = (arr[j] * (j-i+1)) + find_arr_min(i, j)

            return max(find_score(arr, i+1, j, left_score), find_score(arr, i, j-1, right_score)) + score

        return find_score(arr, 0, N-1, 0)


s = Solution()
print(s.MaxScore(8, [2, 3, 4, 1, 5, 7, 5, 6]))
