def valid_string(s):
    found = {}
    max_times = 0

    removed = False
    for i in s:
        if found.get(i) is None:
            found[i] = 1
        else:
            found[i] += 1
        max_times = max(found[i], max_times)
    for times in found.values():
        if (times - 1 == max_times or times - 1 == 0) and removed is False:
            removed = True
            continue
        elif times == max_times:
            continue
        else:
            return "NO"
    return "YES"

print(valid_string("aabbccddeefghi"))