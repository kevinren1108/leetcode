from cmath import inf
from collections import Counter

def s_to_t(s:str, t:str)->int:
    sC = Counter(s)
    tC = Counter(t)

    mx = float(inf)

    for k,v in tC.items():
        mx = min(mx, sC[k])
    print(mx)
    return mx


s_to_t("monooomm", "mon")