# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]
def min(array):
    min_number=array[0]
    for i in range(len(array)):
        if min_number>array[i]:
            min_number=array[i]
    return min_number
array=[2,3,5,0,11,5,2]
print(min(array))