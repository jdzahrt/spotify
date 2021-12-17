dict = {
    "a": ["b", "c", "e"],
    "m": ["c", "e"],
}
inp = "c"

# closest_key(dictionary, input) -> 'm'
# c is at distance 1 from a and 0 from m. Hence closest key for c is m.


def closest_key(dct, i) -> str:
    d = {}
    for k, v in dct.items():
        # print(k, v)
        d[k] = v.index(i)
        j = v.index(i)
        print(j)
        print(d)
    if d.get("a") > d.get("m"):
        print("m is closest")
    else:
        print("a is closest")


closest_key(dict, inp)