def whatFlavors(cost, money):
    d = {}
    for x, y in enumerate(cost):
        if y in d:
            return (d[y], x + 1)
        else:
            d[money-y] = x + 1        
    


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        r = whatFlavors(cost, money)
        print(r[0],r[1])
