#Simple python code for bubble Sort: Method 1
lst = [6,7,8,3,7,8,4,1,0,6,3,6,17,8,9,4,3,2,1,3,6,7,2]
for times in range(len(lst)):
    for e in range(0,(len(lst)-1)):
        if lst[e] > lst[e +1]:
            temp = lst[e]
            lst[e] = lst[e+1]
            lst[e+1] = temp 
               
print("Method 1: ",lst)


#Bubble Sort using function(): Method 2
def bubble_sort(arr_lst):
    for i in range(0, (len(arr_lst)-1)):
        for j in range(len(arr_lst)-1):
            if(arr_lst[j] > arr_lst[j+1]):
                arr_lst[j], arr_lst[j+1] = arr_lst[j+1],arr_lst[j]
    return arr_lst

bucketlist = [529,7,8,3,7,8,4,10,0,6,3,6,7,8,9,4,3,1,1,3,6,7,2]
print("Method 2: ",bubble_sort(bucketlist))

                





