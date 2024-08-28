# EX7.Create function to count negative number in array [-1,11,2,0,-1,4]
def count(array):
    count_number=0
    for i in range(len(array)):
        if array[i]<0:
            count_number+=1
    return count_number
array=[-1,11,2,0,-1,4]  
print(count(array))