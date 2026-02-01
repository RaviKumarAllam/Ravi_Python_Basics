a = 10
b = 20
c = 40
print(a + b + c)


#remove the special meaning of \n --> r (raw string)

#multi print lly for + - * / // (Floor division) ** (power off) % (output will be reminder) _ (underscore for previous output)
a='ravi'
print(a*5)

num1 = 8
num2 = 2

print(num1+num2, num1-num2, num1*num2, num1/num2, num1//num2, num1**num2, num1%num2)

#indexing [a:b] a--> starting, b --> ending
name = 'RAVIALLAM'
print(name[0], name[-1], name[0:2], name[1:], name[:4], name[::-1])

#List indexing [a:b] a--> starting, b --> ending append, insert, pop, extend, min, max, sum and sort
List_Num = [1,3,4,5,6]
print(List_Num[0], List_Num[-1], List_Num[0:2], List_Num[1:], List_Num[:4], List_Num[::-1])
List_Num.append(7)
List_Num.insert(1,2), List_Num.pop(2)
List_Num.extend([8,9,10])
print(List_Num)
List_Num.sort()
print(sum(List_Num),min(List_Num),max(List_Num),max(List_Num),sorted(List_Num))


#Tuple indexing [a:b] a--> starting, b --> ending append, insert, pop, extend, min, max, sum and sort
Tuple_Num = (1,8,9,0,3,4,5,6,5,9,5,1)
print(Tuple_Num[0], Tuple_Num[-1], Tuple_Num[0:2], Tuple_Num[1:], Tuple_Num[:4], Tuple_Num[::-1])
print(Tuple_Num.count(5))

#Set indexing not support improper sequence add, discard, clear, copy, union etc...
Set_Num = {1,8,9,0,2,3,4,5,6,5,9,5,1}
Set_Num.add(7)
print(Set_Num)
Set_Num.union()
print(Set_Num)
