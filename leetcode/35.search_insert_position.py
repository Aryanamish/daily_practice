class Solution:
    def searchInsert(self, nums, target: int) -> int:
        return self.find_target(nums, (0, len(nums)), target)
    
    # range = (start, end)
    def find_target(self, array, range, target):
        if len(array) == 1:
            return 1 if target > array[0] else 0
        if len(array) == 2 and target > array[0] and target < array[1]:
             return range[0] + 1

        middle = len(array)//2
        left_range = (range[0], range[0]+middle)
        left = array[:middle]
        right_range = (range[0]+middle , range[1])
        right = array[middle:]

        if target >= right[0]:
            if target > right[-1]:
                return right_range[1]
            elif target == right[-1]:
                return right_range[1] - 1
            elif target == right[0]:
                return right_range[0]

            new_range = right_range
            new_array = right
        elif target <= left[-1]:
            if target <= left[0]:
                return left_range[0]
            elif target == left[-1]:
                return left_range[1] - 1
            new_range = left_range
            new_array = left
        elif target < right[0] and target > left[-1]:
            return left_range[1]
        return self.find_target(new_array, new_range, target)

    def searchInsert2(self, nums, target):
        l, h = 0, len(nums)
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            while l<h:
                mid = (l+h)//2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    h = mid

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5], 2))
    print(s.searchInsert([1,3,4,6], 5))