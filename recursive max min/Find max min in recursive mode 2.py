x = 0
y = 0
s = []

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
        max_number_if = max(s[low_number], s[high_number])
        return max_number_if
    else:
        mid_number = int((low_number + high_number) / 2)
        max_number1 = findMinMax(low_number, mid_number)
        max_number2 = findMinMax(mid_number + 1, high_number)
        max_number_else = max(max_number1, max_number2)
        return max_number_else


maximum = findMinMax(L, H)
print("maximum  = ", maximum)
