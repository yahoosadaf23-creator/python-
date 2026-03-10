#x=2
#y=5
#z= x+y
#print(z)
"""
a=input ("what's a number a?")
b=input ("what's a number b?")
c = (a )+ (b)
print(c)

a = int(input ("_what's a number a?"))
b = int(input ("what's a number b?"))
c = a + b
print(c)

h = input("what's h?")
i= input("what's i ")
g= int(h) + int(i)
print(g)


t= float(input("what's t?"))
r= float(input("what's r?"))
s = t + r
print(s)

a = float(input("what's a?"))
b = float(input("what's b"))
c = round(a + b)
print(f"The sum is: {c:,}")


s= float(input("what's s?"))
d= float(input("what's d?"))
z= round(s/d,2)
print(f"{z:,}")


s= float(input("what's s?"))
d= float(input("what's d?"))
z = s/d
print(f"{z:,.2f}")


d= float(input("what's d?"))
r = float(input("what's r?"))
"""

def main():
    x = int(input("what's x?"))
    print("x squared is", square(x))

def square(n):
     return n**2

main()