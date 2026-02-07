#Magical code-1
total = 0.1 + 0.2
print(total)
if total == 0.3:
    print('Hi')
else:
    print('Hello')

#Magical code-2 These are non-empty strings so always true
name = "Ravi"
if name == "Kumar" or "Allam":
    print('Correct Name')
else:
    print('Wrong Name')

x="False"
if x:
    print('Coding')
else:
    print('Non Coding')

#Magical code-3 strings are immutable. If we are not storing it will unchange
food = "Pizza"
b= food.replace("z","s")
print(food,b)

#Magical code-4  Conditional logic [if inside if]
x=10
if x>5:
    x=x*2
    if >30:
        x=x-5
print(x)

#Magical code-5 slicing and appening
nums1=[10, 20, 30,40]
nums1.append(nums1[-1]+5)
print(nums1)
total=sum(nums1[1:3])
print(total)

