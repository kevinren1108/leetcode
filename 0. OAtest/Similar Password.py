def similar(new, old):
    newP = 0
    oldP = 0
    cnt = 0

    while oldP < len(old) and newP < len(new):
        if new[newP] == old[oldP]:
            newP += 1
            oldP += 1
            cnt += 1
        elif ord(new[newP]) + 1 == ord(old[oldP]) :
            newP += 1
            oldP += 1
            cnt += 1
        elif new[newP] == "z" and old[oldP] == "a":
            newP += 1
            oldP += 1
            cnt += 1

        else:
            newP += 1

    return cnt == len(old)

res = similar("baacbab", "abdbc")
print(res)
res = similar("accgb", "ach")
print(res)
res = similar("baacba", "abb")
print(res)
res = similar("zzzaa", "aaabb")
print(res)