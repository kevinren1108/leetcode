def add(curr, k):
    curr = set(curr)
    for i in range(len(curr), k):
        for j in range(1, 1000):
            if j in curr:
                continue
            else:
                curr.add(j)
                break

    return list(curr)

res = add([2,3,7], 5)
print(res)