list1 = [2, 13, 14, 1]
list2 = [12, 8, 17, 9]

if len(list1) > len(list2):
    list1, list2 = list2, list1  # Ensure list1 is smaller

m, n = len(list1), len(list2)
print("len of lists , m and n", m,n)
imin, imax, half_len = 0, m, (m + n + 1) // 2

while imin <= imax:
    i = (imin + imax) // 2
    j = half_len - i

    print("DEBUG i,j",i,j)
    if i < m and list2[j-1] > list1[i]:
        print("i  is too small, must increase it, list2[j-1], list1[i]", list2[j-1],list1[i])
        imin = i + 1
        print("imin=",imin)
    elif i > 0 and list1[i-1] > list2[j]:
        print("i is too big, must decrease it, list1[i-1], list2[j]",list1[i-1], list2[j])
        imax = i - 1
    else:
        print( "i is perfect",i)
        if i == 0: max_of_left = list2[j-1]
        elif j == 0: max_of_left = list1[i-1]
        else: max_of_left = max(list1[i-1], list2[j-1])

        if (m + n) % 2 == 1:
            print("Median is =", max_of_left)
            break

        if i == m: min_of_right = list2[j]
        elif j == n: min_of_right = list1[i]
        else: min_of_right = min(list1[i], list2[j])

        print("Median is =", (max_of_left + min_of_right) / 2)
        break






