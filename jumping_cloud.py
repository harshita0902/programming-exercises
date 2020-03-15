def jumpingOnClouds(n,c):
    steps= n-1-sum(c)
    i = 0
    while i < n-2:
        if c[i]==0:
            if c[i+1]==0:
                if c[i+2]==0:
                    steps -= 1
                    i += 2
                    continue
        i += 1
    return steps

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n,c)
    print(result)