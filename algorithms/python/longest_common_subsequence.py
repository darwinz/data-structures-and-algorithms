def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    L = [[None] * (m + 1) for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]


x = input("First string : ")
y = input("Second string: ")
print("The length of LCS is : ", lcs(x, y))
