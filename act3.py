#  factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)  


num = int(input("Enter a number: "))
if num < 0:
    print("Not exist for negative num")
else:
    print("Factorial:",fact(num))