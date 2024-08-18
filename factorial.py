
def fact_func(n):

    if n==1 or n==0:
        return 1
    
    else:
        result = n*fact_func(n-1)
    return result
n = int(input("Enter: "))
print(fact_func(n))