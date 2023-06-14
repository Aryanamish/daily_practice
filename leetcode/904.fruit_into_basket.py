class Solution:
    def totalFruit(self, fruits):
        i = 0
        j = 1
        seen = {}
        seen[fruits[0]] = 1
        ans = 1
        while j < len(fruits):
            if fruits[j] not in seen and len(seen) == 2:
                remove = fruits[i]
                while True:
                    seen[fruits[i]] -= 1
                    i += 1
                    if seen[remove] == 0 or len(seen) < 2:
                        seen.pop(remove)
                        break
                    if seen[fruits[i-1]] == 0:
                        seen.pop(fruits[i-1])
                        break
            
            seen[fruits[j]] = seen.get(fruits[j], 0) + 1
            j += 1
            ans = max(ans, sum(list(seen.values())))
        return ans

if __name__ == '__main__':
    s = Solution()
    fruits = [1,0,1,4,1,4,1,2,3]
    print(s.totalFruit(fruits))
            