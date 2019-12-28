ar = [3, 2, 1, 3]

def birthdayCakeCandles(ar):
    m = max(ar)
    r = []
    print(m)
    for i in ar:
        if i == m:
            r.append(i)
    print(r.count(m))

birthdayCakeCandles(ar)