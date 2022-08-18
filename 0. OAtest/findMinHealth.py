def minimumHealth(damage, armor):
    sm = sum(damage)
    against = min(max(damage), armor)

    return sm - against + 1

res = minimumHealth([2,7,4,3], 4)
print(res)
            