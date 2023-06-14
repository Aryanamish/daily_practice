class Solution:

    def ship_worthy(self, w, ship, days):
        curr_w = 0
        day_count = 0
        for i in range(0, len(w)):
            if w[i] > ship:
                return False
            curr_w += w[i]
            if curr_w <= ship:
                continue
            curr_w = w[i]
            day_count += 1
            if day_count > days:
                return False
        if curr_w != 0:
            day_count += 1
        
        return day_count <= days

    def shipWithinDays(self, weights, days):
        prefix_sum = [weights[0]]
        for i in range(1, len(weights)):
            prefix_sum.append(prefix_sum[-1] + weights[i])
        low = 0
        high = len(prefix_sum) - 1
        print(prefix_sum)
        while low <= high:
            mid = int(low + (high - low) / 2)
            if self.ship_worthy(weights, prefix_sum[mid], days):
                high = mid - 1
            else:
                low = mid + 1
        
        new_high = prefix_sum[low]
        new_low = 0 if low == 0 else prefix_sum[low - 1]
        
        print(f"{self.ship_worthy(weights, new_high, days)} for ship: {new_high}")

        while new_low <= new_high:
            mid = int(new_low + (new_high - new_low) / 2)
            if self.ship_worthy(weights, mid, days):
                new_high = mid - 1
            else:
                new_low = mid + 1
        return new_low

if __name__ == '__main__':
    s = Solution()
    print(s.shipWithinDays([1,2,3,1,1], 4))