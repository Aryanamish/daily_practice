def solve(s, index):

    if index == len(s):
        print("".join(s))
        return
    for j in range(index, len(s)):
        s[index], s[j] = s[j], s[index]
        solve(s, j + 1)
        s[index], s[j] = s[j], s[index]


solve(list('ABCDEF'), 0)