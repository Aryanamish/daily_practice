class Solution:
    
    def __init__(self):
        self.fact = {}
        self.calc_fact = {}
    
    def factorial(self, n):
        if self.fact.get(n, None) is not None:
            return self.fact.get(n)
        ans = 1
        for i in range(2, n+1):
            ans *= i
        self.fact[n] = ans
        return ans
            
        
    def climbStairs(self, n: int) -> int:
        loop = n//2 + 1
        total_steps = 1
        for i in range(1, loop):
            fact_string = f'{n-i}!/{i}!x{n-i-i}!'
            if self.calc_fact.get(fact_string) is not None:
                total_steps += self.calc_fact.get(fact_string)
                continue
                
            output = self.factorial(n - i)/(self.factorial(i)* self.factorial(n-i-i))
            self.calc_fact[fact_string] = output
            total_steps += output
        return int(total_steps)
    
s = Solution()
print(s.climbStairs(6))