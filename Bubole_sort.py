# Bubble sort algorithm this is use to sort a list of numbers....

list =[12,13,47,1,0,15]
print("Unsorted list: ",list)
for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
print("Sorted list: ", list)
