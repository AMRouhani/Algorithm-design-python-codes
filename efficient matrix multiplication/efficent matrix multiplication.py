from numpy import zeros

s = int(input(" Enter your whole number of Arrays : ")) + 1
w = zeros((s, s))
x = -1
y = -1
d = []
v = []
P = zeros((s, s))


def Dynamic_algo(n):
    global P
    for i in range(1, n):
        w[i][i] = 0
    for diagonal in range(1, n - 1):
        for p in range(1, n - diagonal):
            j = p + diagonal
            for k in range(p, j):
                if k == p:
                    v.clear()
                v.append(w[p][k] + w[k + 1][j] + d[p - 1] * d[k] * d[j])
            V_min_val = min(v)
            V_min_index = v.index(V_min_val) + p
            w[p][j] = V_min_val
            P[p][j] = V_min_index


def order(ii, jj):
    if ii == jj:
        print("A" + str(ii), end=" ")
    else:
        kk = int(P[ii][jj])
        print("(", end=" ")
        order(ii, kk)
        order(kk + 1, jj)
        print(")", end=" ")


for t in range(1, s):
    x = int(input("please enter your matrix row : "))
    if x <= 0:
        while x <= 0:
            print("Notice your row number should be positive number, enter again")
            x = int(input("please enter your matrix row : "))
    else:
        d.append(x)
    if y != -1:
        if y != x:
            while y != x:
                print(" Notice your new matrix is not match by last matrix")
                print("Enter your matrix again")
                d.pop()
                x = int(input("please enter your matrix row : "))
                d.append(x)

    y = int(input("please enter your matrix column : "))
    if y <= 0:
        while y <= 0:
            print("Notice your column number should be positive number, enter again")
            y = int(input("please enter your matrix column : "))
    if t == s - 1:
        d.append(y)

Dynamic_algo(s)
print("Ok , now choose which matrixes will be multiple")
iii = int(input("enter your first matrix index : "))
while iii not in range(1, s):
    print(" your index should be higher than 0 and lower than" + str(s))
    iii = int(input("enter your first matrix index : "))
jjj = int(input("enter your last matrix index : "))

while jjj not in range(iii, s):
    print(" your index should be biger than " + str(iii) + " and lower than " + str(s))
    jjj = int(input("enter your last matrix index : "))
print("P is : ", "\n", P, "\n")
print("The multiple of matrices is : ", "\n")
order(iii, jjj)
