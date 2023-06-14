from queue import PriorityQueue

class Solution:
    def print(self, heap, p=True):
        ans = []
        if p: print("Min head: ", end="")
        h = PriorityQueue()
        while heap.qsize() > 0:
            ans.append(heap.queue[0])
            if p:print(heap.queue[0], end=" ")
            h.put(heap.get())
        while h.qsize() > 0:
            heap.put(h.get())
        if p:print()
        return ans

    def minimumDeviation(self, nums):
        min_heap = PriorityQueue()
        min_heap2 = PriorityQueue()
        max_val = float('-inf')
        for num in nums:
            orignal = num
            while num % 2 == 0:
                num = num // 2
            min_heap.put([num, max(orignal, num * 2)])
            max_val = max(max_val, num)
        
        
        # print(f"max_val={max_val}")
        deviation = max_val - min_heap.queue[0][0]
        while min_heap.qsize() == len(nums):
            pair = min_heap.get()
            deviation = min(deviation, max_val - pair[0])
            if pair[0] < pair[1]:
                pair[0] *= 2
                max_val = max(max_val, pair[0])
                min_heap.put(pair)


        return deviation


if __name__ == '__main__':
    s = Solution()
    print(s.minimumDeviation([399,908,648,357,693,502,331,649,596,698]))