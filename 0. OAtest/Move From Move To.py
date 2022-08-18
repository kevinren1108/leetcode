def move_from_move_to(loc:list, mFrom:list, mTo:list)->list:
    curr = set(loc)
    for i in range(len(mFrom)):
        if mFrom[i] in curr:
            curr.remove(mFrom[i])
            curr.add(mTo[i])
    curr = sorted(curr)
    print(curr)
    return curr


move_from_move_to([1,7,6,8], [1,7,2], [2,9,5])