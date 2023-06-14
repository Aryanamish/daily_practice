from collections import deque


class Solution:
    # 1 1 1
    # 1 1 1
    # 1 1 1
    #Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        KnightPos[0] -= 1
        KnightPos[1] -= 1
        TargetPos[1] -= 1
        TargetPos[0] -= 1
        if KnightPos[0] == TargetPos[0] and KnightPos[1] == TargetPos[1]:
            return 0
        visited = [[False for _ in range(N)] for _ in range(N)]
        steps = ((1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1),
                 (-2, -1))
        q = deque()
        q.append((KnightPos[0], KnightPos[1], 0))

        while len(q) != 0:
            temp = q.popleft()
            for step in steps:
                x = temp[0] + step[0]
                y = temp[1] + step[1]
                if (x == TargetPos[0] and y == TargetPos[1]):
                    return temp[2] + 1
                if 0 <= x < N and 0 <= y < N and visited[x][y] is False:
                    q.append((x, y, temp[2] + 1))
                    visited[x][y] = True
        return -1


#{
# Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        KnightPos = list(map(int, input().split()))
        TargetPos = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
        print(ans)

# } Driver Code Ends