# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    min_val = arr[0]
    for i in arr:
        if min_val>i:
            min_val=i
    return min_val
    
def maximum(arr):
    max_val = arr[0]
    for i in arr:
        if max_val<i:
            max_val=i
    return max_val

#arr1 = [4,6,2,1,9,63,-134,566]  
#print(maximum(arr1), minimum(arr1))       # max = 566, min = -134
#arr2 = [-52, 56, 30, 29, -54, 0, -110] 
#print(maximum(arr2), minimum(arr2))     # min = -110, max = 56
#arr3 =  [42, 54, 65, 87, 0]           
#print(maximum(arr3), minimum(arr3))   # min = 0, max = 87
#arr4 =  [5]  
#print(maximum(arr4), minimum(arr4))  

