def verifyPreorder(preorder):
    low = float("-inf")
    path = []
    for p in preorder:
        if p < low:
            return False
        while path and p > path[-1]:
            low = path[-1]
            path.pop()
        path.append(p)
    return True

verifyPreorder([6,2,3,9])