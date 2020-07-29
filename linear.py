def linear_addition(*numbers):
    result = 0
    for i in numbers:
        result += i 
    return result
    
print(linear_addition(1,3,4))
# result in terminal: 8

# note that sum(iterable) does the same