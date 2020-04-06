def minimumSwaps(arr):
    swaps = 0
    for i in range(0, n - 1):
        while arr[i] != i+1:
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            swaps += 1
    return swaps

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)