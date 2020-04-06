def pairs(k, arr):
    count=0
    arr.sort()
    i=0
    j=i+1
    while ((i< len(arr)-1) and (j<len(arr))):
        if(arr[j]-arr[i] < k):
            j+=1
        elif ((arr[j]- arr[i]) == k):
                count+=1
                i+=1
        else:
            i+=1
    return count         

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
    print(result)