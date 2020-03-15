def countingValleys(n, s):
    sea=count=0
    for i in range(n):
        if(s[i]=='U'):
            sea+=1
            if(sea==0):
                count+=1
        else:
            sea-=1
    return count       


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)
