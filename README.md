# Big O Notation Using Python Examples

Big O notation is a method for determining how efficient an algorithm is.\
This knowledge lets us design better algorithms.

## About The Big O Notation

Efficiency is classified by the relation of a large input (denoted by "n" in Big O notation) and the numbers of operations required by the algorithm.

### Big O Notation's Order Of Growth

```
---------------------------------------------------------------------------------
|  Constant  |  Logarithm  |  Linear  |       Polynomial       |  Exponentioal  |
---------------------------------------------------------------------------------
|    O(1)    |   O(log n)  |   O(n)   |  O(n^2),O(n^3),O(n^x)  |      O(2^n)    |
---------------------------------------------------------------------------------
```
Being constant the fastest of all Big O time complexities and Exponentional the slowest.

Other asymptotic (time-measuring) notations are:

```
Asymptotic Notation

---------------------------------------------------------------------------------
|  Big Omega (lower bound)  |  Big Theta (average bound)  |  Big O (max bound)  |
|        (best case)        |        (average case)       |     (worst case)    |
---------------------------------------------------------------------------------
|            ω(n)           |            θ(n)             |        O(n)         |
---------------------------------------------------------------------------------
```

But let's focuse only in Big O.

![Order Of Growth](https://github.com/noevazz/big_o_python/blob/master/img/bigO.png)

## Constant Time

Constant algorithms do not scale with the input size, they are constant no matter how big the input.\
An example of this is addition. 1+2 takes the same time as 1000+900

```python
def constant_addition(x, y):
    return x+y
```

Adding bigger numbers may take more physical time, bu what matters in O(1) is that it takes a constant number of operations.

## Logarithmic Time

First to all... what is a logarithm?: basically it is the inverse function to exponentation.\
Example: How many 2s do we multiply to get 8?\
Answer: 2 × 2 × 2 = 8, so we had to multiply 3 of the 2s to get 8\
So the logarithm is 3

![logarithm of 8 base 2](https://github.com/noevazz/big_o_python/blob/master/img/logarithm.png)

Now, let's discuss another short thing before jumping into O(log n):

### Binary Search

The binary search also called bisect, bisection and half-interval, is a search algorithm that finds\
the position of a target value within a sorted array.\
\
Binary search compares the target value to the middle element of the array. If they are not equal,\
the half in which the target cannot lie is eliminated and the search continues on the remaining half,\
again taking the middle element to compare to the target value, and repeating this until the target value\
is found. If the search ends with the remaining half being empty, the target is not in the array. 

```python
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
        if my_list[low] > search_this or my_list[high] < search_this:
            return f"{search_this} is not in the list"
    return f"{search_this} is at index {mid}, my_list[{mid}]={my_list[mid]}, number of search={counter}"

print(f"Searching in this array: {my_list}")
print(bisect(3, my_list))
print(bisect(5, my_list))
print(bisect(11, my_list))
print(bisect(25, my_list))
print(bisect(19, my_list))
print(bisect(16, my_list))

print("end")
```
The algorithm halves the input every single time it iterates. Therefore it is logarithmic.

## Linear Time

```python
def linear_addition(*numbers):
    result = 0
    for i in numbers:
        result += i 
    return result
    
print(linear_addition(1,3,4))
# result in terminal: 8
```

Linear time algorithms mean that every single element from the input is visited exactly once, O(n) times.

## Polynomial Time

If one loop through a list is O(n), 2 loops must be O(n2). For each loop, we go over the list once.\
For each item in that list, we go over the entire list once. Resulting in n2 operations

```python
a = [1, 2, 3, 4, 5]
for i in a:
    for x in a:
        print("* ", end="")
    print()
```

Bubblesort is a good example of an O(n2) algorithm.

```python
# bubble sort
a = [1, 2, 3, 4, 5]
for iterator in a:
    for index in range(len(a)):
        if index == len(a)-1:
            break
        if a[index] > a[index+1]:
            a[index], a[index+1] = a[index+1], a[index]
print(a)
```

## Exponential Time

Exponential time is 2n, where 2 depends on the permutations involved.\
Wait, what?, what is a permutation?:\
\
First let's learn what a combination is:

### Combinations

Having 4 teams in a football cup (A, B, C and D), what are the possible matches that define the last game:
1. A vs B
2. A vs C
3. A vs D
4. B vs C
5. B vs D
6. C vs D
\
The equation is:\
nCr = n! / ( (n-r)!*r! )\
4C2 = 4! / ( (4-2)!*2! )\
4C2 = 24 / 2!*2!\
4C2 = 24 / 4\
4c2 = 6

### Permutations
Having 4 teams in a football cup (A, B, C and D), how many possibilities we have for a champ and a subchamp:\
```
A champ & B sub-champ   B champ & A sub-champ   C champ & A sub-champ   D champ & A sub-champ
A champ & C sub-champ   B champ & C sub-champ   C champ & B sub-champ   D champ & B sub-champ
A champ & D sub-champ   B champ & D sub-champ   C champ & D sub-champ   D champ & C sub-champ
```

answer = 12\
\
The equation is:\
nPr = n! / (n-r)!\
4P2 = 4! / (4-2)!\
4P2 = 24 / 2!\
4P2 = 24 / 2\
4P2 = 12\
\
So, when talking about permutations the order matters.\
\
Let's say that you want to guess a password that is composed by 6 digits [0-9].\
You can perform a brute-force attack and guess each permutation:
012345\
012344\
012343\
012342\
012341\
etc..\
\
So the number of permutations is:\
10P6 = 10! / (10-6!)\
10P6 = 3628800 / 24\
10P6 = 151200\
\
151200 Permutations!!!!