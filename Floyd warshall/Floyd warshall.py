from numpy import zeros

s = int(input(" Enter your whole number of States : "))
w = zeros((s, s))


def floyd(f):
    for k in range(f):
        for n in range(f):
            for m in range(f):
                w[n][m] = min(w[n][m], w[n][k] + w[k][m])


print("If your state doesn't have any edge enter \" 9999 \" else enter your edge weight")
for i in range(s):
    for j in range(s):
        if i != j:
            w[i][j] = int(input("now is state " + str(i+1) + " " + str(j+1) + " Enter edge weight : "))
        else:
            w[i][j] = 0

print("Your first array you entered : ", "\n", "\n", w, "\n", "\n")
floyd(s)
print("Your array after floyd algorithm : ", "\n", "\n", w)
