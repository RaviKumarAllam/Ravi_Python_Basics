#Magical code-1
total = 0.1 + 0.2 +0.3
print(total)
if total == 0.3:
    print('Hi')
else:
    print('Hello')

#Magical code 2 These are non-empty strings so always true.
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

#Magical code-4  Conditional logic [if inside if].
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
print(list(range(1,10,3)))
s="python"
print(s[::2])

#Magical code-6 
x=3
if x%2==False:
    print('Odd')
elif x%2:
    print('Even')
else:
    print('End')

x=[1,2,3,2]
x.append([4,5])
print(len(x))
x.remove(2) #It will remove only first occurence 
print(x)

a = [1,2,3,4]
b = [1,1,1,1]
c = [x*y for x in a for y in b]
print(len(set(c)))
d = a
a = a + [5]
print(d)

#Magical code-7 operators validation
x={1,2,3}
y={3,4,5}
print(x&y)

#Magical code-8 set remove the duplicates
a={1,2,3,4,2}
print(a)

#Magical code-9
p = "7"
q = "2"
print(int(p+q) - int(q+p))

a="Python"
b=a
b += "Rocks"
print(a)

