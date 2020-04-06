def triplets(a, b, c):
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort()
    b.sort()
    c.sort()
    result = 0
    i=0
    k=0
    for j in range(len(b)):
        while i < len(a):
            if a[i] <= b[j]:
                i += 1
            else:
                break

        while k < len(c):
            if c[k] <= b[j]:
                k += 1
            else:
                break

        result += i * k

    return result
    

if __name__ == '__main__':

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)
    print(ans)
