def maximumToys(prices, k):
    prices.sort()
    count = 0
    i=0
    while k > 0 :
        k -= prices[i]
        count += 1
        i+=1
    
    return count - 1

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)