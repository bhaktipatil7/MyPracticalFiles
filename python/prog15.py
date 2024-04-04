import numpy 

# initializing matrices 
x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]]) 

print ("The element wise addition of matrix is : ") 
print (numpy.add(x,y)) 

print ("The element wise subtraction of matrix is : ") 
print (numpy.subtract(x,y)) 

print ("The element wise division of matrix is : ") 
print (numpy.divide(x,y)) 

print ("The element wise multiplication of matrix is : ") 
print (numpy.multiply(x,y)) 

print ("The dot product of matrices is : ") 
print (numpy.dot(x,y)) 