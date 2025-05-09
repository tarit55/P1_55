import math

def math_prob(a,b,c):
    if a==0:
        if b==0:
            return "No solution: both a and b are zero"
        return "Linear solution: x="+str(-c/b)

    d=b**2-4*a*c

    if d>0:
        root1=(-b+math.sqrt(d))/(2*a)
        root2=(-b-math.sqrt(d))/(2*a)
        return "Two distinct real roots: x1 ="+str(root1)+" x2 ="+str(root2)
    elif d==0:
        root=-b/(2*a)
        return "One real root: x ="+str(root)
    else:
        real=-b/(2*a)
        imaginary=math.sqrt(-d)/(2*a)
        return "Two complex roots: x1 ="+str(real)+"+"+str(imaginary)+"i x2 ="+str(real)+"-"+str(imaginary)+"i"

a=float(input("Enter value of a="))
b=float(input("Enter value of b="))
c=float(input("Enter value of c="))

result=math_prob(a,b,c)
print(result)
