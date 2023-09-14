def calculate_inactive_time(attack, d):
    total_inactive_time = 0
    last_attack_time = 0

    for time in attack:
        inactive_time = max(0, time - last_attack_time - d)
        total_inactive_time += inactive_time
        last_attack_time = time

    inactive_time = max(0, attack[-1] + 1 - last_attack_time - d)
    total_inactive_time += inactive_time

    return total_inactive_time


print(calculate_inactive_time([1, 3], 3))
