# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
def sum_odd(sum):
    sum=0
    for i in range(len(array)):
        if array[i]%2==1:
            sum+=array[i]
    return sum
array=[1,2,3,4,5,6]
print(sum_odd(array))