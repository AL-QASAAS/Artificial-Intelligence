#Activity 1

n = int(input("Enter a Number"))
if (n%2==0):
    print("The Number is Even")
else:
    print("The Number is Odd")

#Activity 2

sum = 0
n = int(input("Enter an integer number"))
while (n!=0):
    sum = sum+n
    n = int(input("Enter an integer value"))
print("Sum of the values is" , sum)

#Activity 3
n = int(input("Enter a Number"))
c = 0
for i in range (1,n+1):
    if (n%i==0):
        c+=1
if (c>2):
    print("Number is not prime")
else:
    print("Number  is prime")

#Activity 4
sum = 0

for i in range (0 , 5):
    n = int(input("Enter a number"))
    sum = sum+n
print("Sum is: " , sum)

# Activity 5
sum = 0
i = 1
while (i<=10):
    sum = sum + i
    i=i+1
print("Sum is: " , sum)

#Activity 6
name = input('What is your name? ')
print('Hello ' + name)
job = input('What is your job? ')
print('Your job is ' + job)
num = input('Give me a number? ')
print('You said: ' + str(num))

#Activity 7
import random

rand = random.randint(1,9)
guess = 0
c = 0
while guess != rand and guess != "exit":
    guess = input("Enter a guess between 1 to 9")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < rand:
        print("Too low")
    elif guess > rand:
        print("Too high")
    else:
        print("Right!")
        print("You took only", c, "tries!")


#Task 1

n = int(input("Enter a number"))
a=0
print("Numbers are: ",n)
result = ""
while n!=0:
    a = n%10
    result =result + str(a)
    n=int(n/10)

print('Numbers in reverse order: ',result)

# Task 2

n = int(input("Enter the Number of elements"))

odd = 0
even = 0
for i in range(0, n):
    n = int(input("Enter the number"))
    if n % 2 == 0:
        even = even + n
    else:
        odd = odd + n

print("Sum of odd numbers: ", odd)
print("Sum of even numbers: ", even)


# Task 3

def Fibonacci(n):
    if n < 0:
        print("Invalid input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print(Fibonacci(3))


#Task 4

marks = int(input('Enter the marks:'))

if marks<0 or marks>100:
    print("Invalid marks")
else:
    if marks<50:
        print("F Grade" ,marks)
    elif marks>50 and marks<60:
        print("E Grade",marks)
    elif marks>61 and marks<70:
        print("D Grade",marks)
    elif marks>71 and marks<80:
        print("C Grade",marks)
    elif marks>81 and marks<90:
        print("B Grade" , marks)
    else:
        print("A Grade")


# Task 5
def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number"));
print("Factorial of", num, "is",
      factorial(num))

