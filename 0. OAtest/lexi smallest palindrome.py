def lexi(origenal):
    res = ""
    ori = set(origenal)
    order = []
    for each in ori:
        order += [each]
    order = sorted(order)
    order = "".join(order)
    res = order + order[::-1]
    return res 


res = lexi("baab")
print(res)