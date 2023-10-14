### Print
print("Hello World")

### Data Types
n1 = 123            # int
n2 = 100.23         # decimal
name = 'John'      # string
list1 = ['apple', 'orange', 'kiwi'] # list
dict1 = {'name': 'John Doe', 'age': 21, 'country': 'SG'} # dictionary
v1 = True           # boolean
v2 = False          # boolean
print(n1)
print(n2)
print(name)
print(list1)
print(dict1)
print(v1)
print(v2)

# Reassignment of Variable
variable = 222
print(n1)
variable = 'Brave new World'
print(n1)

## If-else Condition
example = 'Sagar'
if example == 'sagar':
    print("Success!")
else:
    print("Failed")

## If-elif-else Condition
num = 300
if num > 200:
    print("More than 200")
elif num > 100:
    print("More than 100")
else:
    print("Less than equal 100")

## While Loop
num = 0
while num < 100:
    num = num + 20
    print("Value of num: " + str(num))
