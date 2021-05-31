1. How many stars(*) will the following snippet send to the console?
```py
i = 0
while i < i + 2:
    i += 1
    print("*")
else:
    print("*")
```
    A: the snippet will enter an infinite loop, printing one star per line

2. What is the output of the following snippet?
```py
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")
```
    A: 21

3. Which of the following sentences are true about the code? (Select two answers)
```py
nums = [1, 2, 3]
vals = nums
```
  1.  nums and vals are different lists
  2.  nums has the same langth as vals
  3.  vals is longer than nums
  4.  nums and vals are different names of the same list
    T: 2 & 4

4. What is the output of the following piece of code if the user enters two lines containing 3 dan 6 respectively?
```py
y = input()
x = input()
print (x, y)
```
    A: 63

5. What is the output of the following piece of code?
```py
print("a", "b", "c", sep="sep")
```
    A: asepbsepc

6. What is the output of the following snippet?
```py
def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))
```
    A: 4

7. The following snippet:
```py
def function_1(a):
    return None

def function_2(a):
    return function_1(a) * function_1(a)

print(function_2(a))
```
    A: will cause a runtime error

8. The meaning of a positional argument is determined by:
    T: the argument's name specified along with its value

9. What is the output of the following snippet?
```py
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0, 3))
```
    A: 0

10. Which of the following variable names are illegal and will cause SyntaxError exception? (Select two answers):
    1. for
    2. in
    3. print
    4. In
    T: 2 & 4

11. The result of the following division: 1 // 2
    A: is equal to 0

12. What is the output of the following piece of code if the user enters two lines containing 2 and 4 respectively?
```py
x = float(input())
y = float(input())

print(y ** (1 / x))
```
    A: 2.0

13. Assuming that my_tuple is a correctly created tuple are immutable means that the following instruction:
```py
my_tuple[1] = my_tuple[1] + my_tuple[0]
```
    T: can be executed if and only if the tuple contains at least two elements

14. Take a look at the snippet and choose the true statement:
```py
nums = [1, 2, 3]
vals = nums
del vals[:]
```
    T: the snippet will couse a runtime error

15. What is the output of the following piece of code if the user enters two lines containing 3 and 2 respectively?
```py
x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)
```
    A: 2

16. How many elements does the lst list contain?
```py
lst = [i for i in range(-1, -2)]
print(lst)
```
    A: zero `[]`

17. What is the output of the following snippet?
```py
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
```
    A: 4

18. The following snippet:
```py
def func(a, b):
    return b ** a

print(func(b=2, 2))
```
    A: is erroneous

19. What is the output of the following snippet?
```py
dct = {'one':'two', 'three':'one', 'two':'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)
```
    A: one

20. What is the output of the following snippet?
```py
my_list = [x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))
```
    A: [0, 1, 4, 9]

21. What is the output of the following snippet?
```py
dd = {"1":"0", "0":"1"}
for x in dd.vals():
    print(x, end="")
```
    A: the code is erroneous (the dict object has no vals() method)

22. Which of the following lines correctly invoke the function defined below? (Select two answers):
  1. fun(b=1)
  2. fun()
  3. fun(0, 1, 2)
  4. fun(b=0, a=0)
    A: 1 & 4

23.  How many hashes(#) will the following snippet send to the console?
```py
lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
```
    A: three

24. An operator able to check whether two values are no equal is coded as:
    A: !=

25. What is the output of the following piece of code?
```py
x = 1 // 5 + 1 / 5
print(x)
```
    A: 0.2

26. What is the output of the following piece of code?
```py
x = 1
y = 2
x, y ,z = x, x ,y
z, y ,z = x, y ,z

print(x, y, z)
```
    A: 1 1 2

27. What value will be assigned to the x variable?
```py
z = 0
y = 10
x = y < z and z > y or y > z and z < y
print(x)
```
    A: True

28. What is the output of the following snippet?
```py
my_list = [1, 2]
for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
```
    A: [1, 1, 1, 2]

29. What is the output of the following snippet?
```py
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))
```
    A: 2

30. What will be the output of the following snippet?
```py
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
```
    A: 0 1
