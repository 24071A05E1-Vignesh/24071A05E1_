#GCD and LCM of two numbers.
def gcd(n1,n2):
    if n2==0:
        return n1
    else:
        return gcd(n2,n1%n2)
def lcm(n1,n2):
    return (n1*n2)/gcd(n1,n2)
n1=int(input("Enter 1st number "))
n2=int(input("Enter 2nd number "))
print("The GCD is",gcd(n1,n2))
print("The LCM is",lcm(n1,n2))