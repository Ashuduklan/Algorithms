# Ascending order

li = [56, 23, 2, 3, 5, 14]
print("unsorted list", li)
for i in range(len(li)):
    min_value = min(li[i:])
    min_ind = li.index(min_value)
    li[i], li[min_ind] = li[min_ind], li[i]
    # temp = li[i]
    # li[i] = li[min_ind]
    # li[min_ind]= temp
print("sorted list", li)