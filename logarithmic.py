# note this program is not able to check numbers that are not present in the list

my_list = list(range(3, 28, 2)) # so my_list = 3, 5, 7, 9...27

def bisect(search_this, my_list):
    low = 0
    high = len(my_list)-1
    mid = high//2
    counter = 0
    
    while my_list[mid] != search_this:
        counter += 1
        if my_list[mid] < search_this:
            low = mid+1
        elif my_list[mid] > search_this:
            high = mid-1
        mid = (low+high)//2
    return f"{search_this} is at index {mid}, my_list[{mid}]={my_list[mid]}, numer of search={counter}"

print(f"Searching in this array: {my_list}")
print(bisect(3, my_list))
print(bisect(5, my_list))
print(bisect(11, my_list))
print(bisect(25, my_list))
print(bisect(19, my_list))
print("end")