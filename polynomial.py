a = [1, 2, 3, 4, 5]
for i in a:
    for x in a:
        print("* ", end="")
    print()

# bubble sort
a = [1, 2, 3, 4, 5]
for iterator in a:
    for index in range(len(a)):
        if index == len(a)-1:
            break
        if a[index] > a[index+1]:
            a[index], a[index+1] = a[index+1], a[index]
print(a)
