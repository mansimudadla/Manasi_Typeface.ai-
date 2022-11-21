def Base3(number):
    result = ""
    while number!=0:
        result = str(number%3)+result
        number=number//3
    return result
number=int(input())
print(Base3(number))
    
