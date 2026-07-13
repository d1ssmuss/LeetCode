def sequentialDigits(low, high):
    # r = list({len(str(low)), len(str(high))})
    r = [i for i in range(len(str(low)), len(str(high)) + 1)]
    # print(r)
    n = '123456789'
    arr = []
    for j in r:
        for i in range(len(n)):
            v = int(n[i:i + j])
            if low <= v <= high and len(str(v)) == j:
                arr.append(v)
                # print(v)
    return arr




print(sequentialDigits(100, 300))
print(sequentialDigits(1000, 13000))
print(sequentialDigits(10, 1_000_000_000))
