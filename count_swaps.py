def countSwaps(a):
    temp=0
    count=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                count+=1
    return count               


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    x = countSwaps(a)
    print('Array is sorted in', x, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])
