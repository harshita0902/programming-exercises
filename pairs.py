def pairs(k, arr):
    count=0
    #arr.sort()
    for i in range(len(arr)-1):
        j=i+1
        while (j< len(arr)) and (arr[j]-arr[i] <= k):
            if ((arr[j]- arr[i]) == k):
                count+=1
        j+=1
    return count          

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
    print(result)