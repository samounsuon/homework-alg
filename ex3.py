# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]
def max(array):
    max_num=array[0]
    for i in range(len(array)):
        if max_num==0:
            max_num=array[0]
        elif max_num<array[i]:
            max_num=array[i]
    return max_num
array=[2,3,5,0,11,5,2]
print(max(array))