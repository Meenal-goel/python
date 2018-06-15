#1.calculate the average of numbers in given list

list_one = [1,2,3,4,5,6]
sum = 0
for x in list_one :
    sum = sum + x
    avg = (sum/len(list_one))

print("average of numbers in list is:",avg)
print("\n")

#2.exchange the values of two numbers without using temporary variable

#only integer /float type values are supported in this approach
a = int(input("enter first value:"))
b = int(input("enter second value:"))
print("initial values : a = %s b = %s "%(a,b))
a = a - b
b = a + b
a = b - a
print("exchanged values : a = %s b = %s "%(a,b))
print("\n")
#another way of implementing same program (accepts string type value as well)
a1 = (input("enter first value:"))
b1 = (input("enter second value:"))
print("initial values : a = %s b = %s "%(a1,b1))
(a1, b1) = (b1, a1)
print("exchanged values : a = %s b = %s "%(a1,b1))
print("\n")

#3. read a number n and compute n+nn+nnn

n = int(input("enter a number"))
s = (n+(n*n)+(n*n*n))
print("n+nn+nnn=",s)
print("\n")

#4. prog to reverse a given number

n1 = int(input("enter a number:"))
rev = 0
while (n1 > 0):
    digit = n1 % 10
    rev = (rev * 10 ) + digit
    n1 = n1 // 10
print("REVERSED NUMBER :", rev)
print("\n")

#5. check for positive and negative number

num1 = int(input("enter a number : "))

if ( num1 > 0  ):
    print(" %d is a POSITIVE number"%(num1))

elif( num1 < 0 ):
    print(" %d is a NEGATIVE number"%(num1))

else :
    print("number is ZERO")
print("\n")

#6. take marks in five subjects and display grades accordingly


marks_dict = {}

data = int(input("enter the number of subjects"))
for sub in range(data):
    marks_list = input().split() 
    marks_dict[marks_list[0]] = int(marks_list[1])
print(marks_dict)



for k,v in marks_dict.items():
    if(100>=v>80):
        print("GRADE A")

    elif(80>=v>60):
        print("GRADE B")

    elif(60>=v>40):
        print("GRADE C")

    else:
        print("FAIL")
print("\n")

#7. print all numbers in a range divisible by a given number

divisor = int(input("enter a divisor"))

for any_num in range (1,20):
    if(any_num % divisor == 0):
        print (any_num)
print("\n")

#8.read two numbers and print their quotient and remainder

numb1 = int(input("enter first number"))
numb2 = int(input("enter second number"))

q1 = numb1/2
r1 = numb1%2

q2 = numb2/5
r2 = numb2%5

print("quotient = %d and remainder = %d for first number"%(q1,r1))
print("quotient = %d and remainder = %d for second number"%(q2,r2))
print("\n")

#9.program that accepts three digits and print all possible combinations from the digits

digit_list = []
val1 = int(input("enter first digit"))
val2 = int(input("enter second digit"))
val3 = int(input("enter third digit"))
digit_list.append(val1)
digit_list.append(val2)
digit_list.append(val3)

print("possible combinations are:")

for i in range(0,3):
    
    for j in range(0,3):
        
        for k in range(0,3):
            
            if(i != j and j != k and k != i):
                
                print(digit_list[i],digit_list[j],digit_list[k])
print("\n")

#10.program to print odd numbers within a given range

print("odd numbers from 1 to 20 are:")
for all_num in range(1,20):
    if(all_num % 2 != 0):
        print(all_num)
print("\n")

#11.program to find sum of digits of a number

numbx = int(input("enter a number:"))
sumx = 0
while( numbx >0):
    digits = numbx % 10
    numbx = numbx // 10
    sumx = sumx + digits

print("sum of digits is :",sumx)
print("\n")

#12.find smallest divisor of an integer

div_list = []
intx = int(input("enter the integer:"))
for element in range(2,intx):
    if(intx % element == 0):
        div_list.append(element)

div_list.sort()
print("smallest divisor of %d is %d"%(intx,div_list[0]))
print("\n")

#13.count number of digits in a number

numx = int(input("enter the number"))
cn = 0
dig_list = []
while(numx > 0):
    dig = numx % 10
    numx = numx // 10
    dig_list.append(dig)
print("Number of digits in a number :",len(dig_list))
print("\n")

#14. check if number is pallindrome

pal = int(input("enter the number"))
temp = pal
pal_rev = 0
while(pal > 0):
    pal_digit = pal % 10
    pal_rev = (pal_rev * 10) + pal_digit
    pal = pal // 10
if(temp == pal_rev):
    print("numbner is PALLINDROME")

else :
    print("number is NOT PALLINDROME")
print("\n")

#15. print all integers that are not divisible by 2 and 3 and lie between 1 and 50

print("all integers that are not divisible by 2 and 3 and lie between 1 and 50 are:")
for integers in range (1,50):
    if( integers % 2 != 0 and integers % 3 != 0):
        print(integers)
print("\n")

#16. read a number n and print series 1+2+....+n
m = int(input("enter a number"))
mx = 0

for ele in range(1,m+1):
        
    mx = mx + ele
    print(ele,end =' ')
    if(ele < m):
        print("+ ",end='')
   
print('=',mx)
print("\n")

#17. program to read a number n and print natural numbers summation pattern

natural = int(input("enter a number"))

for nat in range(1, natural+1):
    a_list = []
    for anat in range(1, nat+1):
        
        print (anat,end = '')
        if(anat < nat):
            print("+", end = '')
        a_list.append(anat)
    print('=',sum(a_list))
print("\n")

#18.program to print an identity matrix

mat = int(input("enter matrix size:"))
for row in range(0,mat):
    for col in range(0,mat):
        if(row == col):
          print("1",end= ' ')

        else :
          print("0",end = ' ')

    print()
print("\n")

#19.program to print an inverted star pattern

star = int(input("enter the matrix size:"))
print("\n")
while ( star > 0):
    print(("*")*star)
    star = star - 1
print("\n")

#20. program to check for prime numbers

prime = int(input("enter a number"))

if(prime ==1):
    print("prime number")
    
elif(prime ==( prime/2 + 1)):
    print("prime number")

else:
    print("not a prime number")
          
    

    
     
        
    
    




        


  
    

    




