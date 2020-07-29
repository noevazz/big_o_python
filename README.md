# Big O Notation Using Python Examples

Big O notation is a method for determining how fast an algorithm is.\
This knowledge lets us design better algorithms.\

## Measuring The Time For An Algorithm In Python

- WIP

## About The Big O Notation

Big O takes the upper bound execution of an algorithm, e.g. an infinite list.\
Instead of saying the input is, for example 10 billion, or infinite, we say the input is "n" size,\
it doesn't really matter since we are considering the worst escenario.

### Big O Notation's Order Of Growth

```
---------------------------------------------------------------------------------
|  Constant  |  Logarithm  |  Linear  |       Polynomial       |  Exponentioal  |
---------------------------------------------------------------------------------
|    O(1)    |   O(log n)  |   O(n)   |  O(n^2),O(n^3),O(n^x)  |      O(2^n)    |
---------------------------------------------------------------------------------
```
Being constant the fastest of all Big O time complexities and Exponentional the slowest.\

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

What matters in O(1) is that it takes a constant number of steps.

## Logarithmic Time

First to all... what is a logarithm: basically it is the inverse function to exponentation.\
Example: How many 2s do we multiply to get 8?\
Answer: 2 × 2 × 2 = 8, so we had to multiply 3 of the 2s to get 8\
So the logarithm is 3\
![logarithm of 8 base 2](https://github.com/noevazz/big_o_python/blob/master/img/logarithm.png)


## Linear

```python
def linear_addition(*numbers):
    result = 0
    for i in numbers:
        result += i 
    return result
    
print(linear_addition(1,3,4))
# result in terminal: 8
```