#emp details

def emp(name):
    return name

def sal(exp):
    if exp>=5:
        return 300000
    elif exp>=3:
        return 100000
    else:
        return 50000

print("Emp Name:",emp("Prachi"))
print("Salary:",sal(10))
