def rotLeft(a, d):
    
    for i in range(d):
        # print(i)
        f = a[0]
        a.remove(f)
        a.append(f)
    return a
                

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    # print(a)
    result = rotLeft(a, d)
    print(' '.join(map(str, result)))
