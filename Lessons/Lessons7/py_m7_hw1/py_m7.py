rows = []
L=[]
SH = []
DL = []
C =[]
with open("m7-map-1.txt") as fp:
    for row in fp:
        if 'ID' in row:
            rows.append(row)
    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        S = (int(s[1])) *  (int(s[0]))
        L.append(S)
    print(sum(L)/len(rows))
    N = print(max(L))


    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        S = (int(s[1])) / (int(s[0]))
        C.append(S)
    print('vut = ',max(C))
    print('vut.min = ', min(C))

    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        S = (int(s[1])) / (int(s[0]))
        if S == 6.9:
            print('vut = ',l[0])
            break

    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        S = (int(s[1])) * (int(s[0]))
        if S == 6831:
            print('S.max = ',l[0])
            break

    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        sh = (int(s[1]))
        SH.append(sh)
        dl = (int(s[0]))
        DL.append(dl)
    print('Sh = ', max(SH))
    print('Dl = ', max(DL))

    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        sh = (int(s[1]))
        if sh == 69:
            print('sh = ',l[0])
            break

    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        dl = (int(s[0]))
        if dl == 99:
            print('dl = ',l[0])
            break

rows = []
L=[]
with open("m7-map-2.txt") as fp:
    for row in fp:
        if 'ID' in row:
            rows.append(row)
    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        S = (int(s[1])) *  (int(s[0]))
        L.append(S)

    print(sum(L)/len(rows))
    N = print(max(L))

    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        S = (int(s[1])) * (int(s[0]))
        if S == 6831:
            print('S.max = ',l[0])
            break

    for row in rows:
        l = row[2:].split('::')
        s = l[2].split('x')
        sh = (int(s[1]))
        SH.append(sh)
        dl = (int(s[0]))
        DL.append(dl)
    print('Sh = ',max(SH))
    print('Dl = ',max(DL))