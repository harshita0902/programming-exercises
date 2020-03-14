def sockMerchant(n, ar):
    d={}
    sum=0
    for i in ar:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]==1:
            continue
        else:
            a=d[i]/2  
        sum=int(sum+a)
    return sum

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)