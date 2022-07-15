class Solution:
    highest_sqrt = 46340
    
    
   
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        high = min(self.highest_sqrt, x//2)
        low = 1
        ans = 0

        while low <= high:
            if low + 1 == high:
                return low if high*high > x else high
            mid = (high + low) //2
            
            sq = mid * mid

            if  sq <= x < (mid + 1) * (mid + 1):
                ans = mid
                break

            if sq < x:
                low = mid
                ans = mid
            elif sq > x:
                high = mid
        
        
        return ans
    

if __name__ == '__main__':
    s = Solution()
    for i in range(2,40):
        print(i)
        try:
            if int(i**(1/2)) == s.mySqrt(i):
                pass
            else:
                print(i, s.mySqrt(i))
        except Exception as e:
            print(e)
            break