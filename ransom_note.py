def checkMagazine(magazine, note):
    l1 = len(note)
    l2 = len(magazine)
    magazine.sort()
    note.sort()
    i = 0
    j = 0
    count = 0
    while i<l1 and j<l2:
        if note[i] == magazine[j]:
            count += 1
            i += 1
        j+= 1
    if count == l1:
        return 'Yes'
    else:
        return 'No'
        

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))