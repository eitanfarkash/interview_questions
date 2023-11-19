mem = {-2: 0, -1: 0, 0: 1, 1: 1}


def ways(h):
    # if h in mem:
    #     return mem[h]
    # else:
    #     mem[h] = ways(h - 3) + ways(h - 2) + ways(h - 1)
    #     print(f"h = {h} and mem = {mem}")
    #     return mem[h]
    try:
        return mem[h]
    except KeyError:
        mem[h] = ways(h - 1) + ways(h - 2) + ways(h - 3)
        # print(mem)
        return mem[h]


print(ways(4))
