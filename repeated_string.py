def repeatedString(s, n):
    flag=s.count('a')
    if flag==0:
        x=0
    elif flag==1 and len(s)==1:
        x=n
    else:
        q=int(n/len(s))
        r=n%len(s)
        count=flag*q
        st1=s[:r]
        x=count+st1.count('a')
    return x

if __name__ == '__main__':
    
    s = input("enter your string")

    n = int(input('enter your number'))

    result = repeatedString(s, n)
    print(result)