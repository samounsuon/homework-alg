# EX1.Create function to sum numbers in array [1,2,3,4,5,6]
def sum(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    return sum
array=[1,2,3,4,5,6]
print(sum(array))