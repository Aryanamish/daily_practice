class Solution:
    def best_team(self, members):
        teams = []
        for m1 in range(len(members)):
            for m2 in range(m1+1, len(members)):
                final = bin(members[m2] | members[m1])[2:]
                fianl = final.replace('0', '')
                teams.append(final.replace('0', ''))

        teams.sort()
        teams.reverse()
        best_score = len(teams[0])
        no_of_teams = 0
        best_team = teams[0]
        for t in teams:
            if t == best_team:
                no_of_teams += 1
            else:
                break
        return best_score, no_of_teams
    
input = [
    "10101", # 21
    "11100", #28
    "11010", #26
    "00101", #5
]
inputs = []
for i in input:
    inputs.append(int(i, 2))
s = Solution()
ans = s.best_team(inputs)
print(ans[0])
print(ans[1])