def twoStrings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    if set.intersection(set1,set2):
        return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        print(result)