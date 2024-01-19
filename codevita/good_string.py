from queue import PriorityQueue

good_string = "6*K4AQf]gpi"
name = "Nainika"


def solve(good_string, name):
    good_string_map = set()
    for i in good_string:
        good_string_map.add(ord(i))
    ans = 0
    prev_good = good_string[0]
    for n in name:
        dist, prev_good = find_dist(good_string_map, n, prev_good)
        ans += dist
    return ans


def find_dist(good_string_map, char, prev_good):
    q = PriorityQueue()
    asci = ord(char)
    if asci in good_string_map:
        return 0, prev_good
    for ch in good_string_map:
        diff = abs(asci - ch)
        q.put((diff, chr(ch)))
    if q.qsize() >= 2:
        first = q.get()
        second = q.get()
        if first[0] == second[0]:
            if abs(ord(prev_good) - ord(first[1])) < abs(ord(prev_good) - ord(second[1])):
                return abs(ord(prev_good) - ord(first[1])), first[1]
            else:
                return abs(ord(prev_good) - ord(second[1])), second[1]
        return first
    else:
        return q.get()


print(solve(good_string, name), end="")
