# Python Practical 07 - To write a python program to find the square root of a number (Newton’s Method).

def sqr_root(num):
    sqr = num / 2
    threshold = 0.0001

    while abs(sqr * sqr - num) > threshold:
        sqr = (sqr + num / sqr) / 2

    return sqr

num = 16

ans = sqr_root(num)

print(f"The Square root of {num} is : {ans}")

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")