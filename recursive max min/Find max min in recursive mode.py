x = 0
y = 0
s = []
a = [0]
b = [0]
c = [0]
d = [0]

while x is not "end":
    print("Alert : if you finished your entering your number write\" end \"")
    x = input("enter your numbers : ")
    if "end" in x:
        break
    y = int(x)
    s.append(y)

L = 0
H = len(s) - 1


def findMinMax(low_number, high_number):
    if (low_number == high_number - 1) or (low_number == high_number):
        min_number_if = min(s[low_number], s[high_number])
        max_number_if = max(s[low_number], s[high_number])
        a.pop()
        a.insert(0, max_number_if)
        return min_number_if
    else:
        mid_number = int((low_number + high_number) / 2)
        min_number1 = findMinMax(low_number, mid_number)
        global b
        b = a.copy()
        min_number2 = findMinMax(mid_number + 1, high_number)
        global c
        c = a.copy()
        min_number_else = min(min_number1, min_number2)
        max_number_else = max(b, c)
        global d
        j = d.pop()
        i = max_number_else.pop()
        m = max(j, i)
        d.append(m)
        return min_number_else


minimum = findMinMax(L, H)
maximum = d.pop()
print("minimum  = ", minimum)
print("maximum  = ", maximum)
