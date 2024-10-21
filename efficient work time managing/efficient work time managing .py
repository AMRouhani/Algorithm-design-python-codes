arr_input = int(input("please enter your numbers of your works : "))
work = []
val = 0


def array_maker(m, n):
    A = []
    for kk in range(m):
        v = []
        for k in range(n):
            if k == 0:
                x = input("Please enter your work name : ")
                v.append(x)
            elif k == 1:
                y = int(input("Please enter your work time : "))
                v.append(y)
            else:
                z = int(input("Please enter your work value : "))
                v.append(z)
        A.append(v)
    return A


arr = array_maker(arr_input, 3)
print(" your array entered : ", arr, "\n")

for j in range(arr_input - 1, 0, -1):
    for i in range(j):
        if arr[i][1] > arr[i + 1][1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if arr[i][1] == arr[i + 1][1]:
            if arr[i][2] > arr[i + 1][2]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(" your array sorted by work time : ", arr, "\n")

lengh_of_arr = len(arr)
last_time = arr[lengh_of_arr - 1][1]
mag = []
choosen_work_profit = []
bb_prime = 0

for t in range(1, last_time + 1):
    bb = bb_prime
    while t <= arr[bb][1] < t + 1:
        mag.append(arr[bb][2])
        bb += 1
        if bb == lengh_of_arr:
            break
    bb_prime = bb
    mag.extend(choosen_work_profit)
    choosen_work_profit.clear()
    mag.sort()
    iioo = 0
    while iioo < t:
        choosen_work_profit.append(mag.pop())
        iioo += 1
    mag.clear()

for hm in range(lengh_of_arr):
    if arr[hm][2] in choosen_work_profit:
        work.append(arr[hm][0])

val = sum(choosen_work_profit)

print(" our works that we should choose : ", work, "\n")
print(" our choosen works profit : ", choosen_work_profit, "\n")
print(" whole profit is : ", val)
