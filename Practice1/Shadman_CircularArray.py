def checkInterval(a, n, ind, interval):
    CirArray2 = [None] * 2 * n
    i = 0

    while i < n:
        CirArray2[i] = CirArray2[n + i] = a[i]
        i = i + 1

    i = ind

    while i < n + ind:
        if CirArray2[0] % interval == 0:
            print(CirArray2[i], end=" ")
            i = i + 1
        if CirArray2[i] % interval != 0 and CirArray2[i] != 0:
            print((CirArray2[i] + 1), end=" ");
            i = i + 1
        else:
            print(CirArray2[i], end=" ")
            i = i + 1


CirArray = [0, 0, 2, 5, 3, 3, 5, 6, 7, 1, 0, 0]
n = len(CirArray);
checkInterval(CirArray, n, 2, 2);
