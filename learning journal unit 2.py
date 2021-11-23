#Learning journal unit week 2
#FIRST PART

# here am defining the print volume function
# then i imported pi from math module

def print_volume(r):
    from math import pi
    return print((4 / 3) * pi * (r ** 3))
 
 
print_volume(1)
print_volume(2)
print_volume(3)


def sin_us(x):
    from math import sin, cos, tan
    print(sin(x), cos(x), tan(x), end='\n')
    return None
#Description
#My function allows the angle and calculates, also it prints the sine, cosine, and tangent of the entered angle for this function



#SECOND PART GOES HERE
#The function findMean first calculate the length of the array. Then the a temporary variable Sum is initialized to zero and sum of all the elements of array you are taken in the for loop that goes from 0 to length of the array. In the end, the sum is divided by the length of the array to get the mean. The mean is returned to the calling function.
def findMean(u):
    Sum=0
    for r in range(0,len(u)):
        Sum = Sum + u[r]
    Mean = Sum/len(u)
    return(Mean)


A = [5, 9, 12, 86]
m = findMean(A)
print("\nCall No. 1")
print("Input Array = ",A)
print("Mean = %.2f"%m)

A = [10, 15, 13, 56]
m = findMean(A)
print("\nCall No. 2")
print("Input Array = ",A)
print("Mean = %.2f"%m)

A = [2, 44, 11, 560]
m = findMean(A)
print("\nCall No. 3")
print("Input Array = ",A)
print("Mean = %.2f"%m)

#The out put for the above code will be 
# Call No. 1        
# Input Array =  [5, 9, 12, 86]
# Mean = 28.00

# Call No. 2
# Input Array =  [10, 15, 13, 56]
# Mean = 23.50

# Call No. 3
# Input Array =  [2, 44, 11, 560]
# Mean = 154.25
