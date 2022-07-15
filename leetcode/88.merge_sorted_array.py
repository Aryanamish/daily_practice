class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        for i in range(len(nums1)-1,-1,-1):
            if n<0:
                return
            if m>=0 and nums1[m]>nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -=1
            
                
if __name__ == '__main__':
    s = Solution()
    nums1=[1,2,3,7, 8,0,0,0]
    nums2 = [2,5,6]
    s.merge(nums1, 5, nums2, 3)
    print(nums1)
