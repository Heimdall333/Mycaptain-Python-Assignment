#Q1 Write a Python program which accepts the radius of a circle from the user and computes area.
r = float(input("Input the radius of the circle = "))
a = 3.14159 * r * r
print("The area of the circle with radius is = ", a)


#Q2 Write a Python program to accept a filename from the user and print the extension of that.
fn= input("Enter Filename: ")
f = fn.split(".")
print ("Extension of the file is : " + f[-1])
