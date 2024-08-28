# EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]
def count(array):
    count_number=0
    for i in range(len(array)):
        if array[i]==5:
            count_number+=1
    return count_number
array=[2,3,5,0,11,5,2]
print(count(array))