n=input("Enter a number")
if int(n)%2==0:
    print("the given number is an even number") 
else:
     print("The given number is an odd number")

sum=0
s=input("Enter an integer value...")
n=int(s)
while n!=0:
    sum=sum+n
    s=input("Enter an integer value...")
    n=int(s)
print("Sum of given value is ",sum)


isPrime = True
i=2
n=int(input("Enter a number"))
while i<n:
    remainder=n%i
    if remainder==0:
        isPrime=False
        break
    else:
        i=i+1
        if isPrime:
            print("Number is Prime")
        else:
            print("Number is not Prime")


summ = 0
i=0
while i<=4:
    s=input("Enter a number")
    n=int(s)
    summ=summ+n
    i=i+1
    
    print("sum is ",summ)



summation = 0
i=1
while i<=10:
    summation=summation+i
    i=i+1
    
    print("sum is ",summation)


name = input('What is your name? ')
print('Hello' + name)

job = input('What is your job? ')
print('Your job is ' +job)

num = input('Give me a number? ')
print('You said:' +str(num))



import random
# Awroken

MINIMUM=1
MAXIMUM=9
NUMBER=random.randint(MINIMUM,MAXIMUM)
GUESS=None
ANOTHER=None
TRY=0
RUNNING=True

print ("Alright...")

while RUNNING:
    GUESS=input("What is your lucky number?")
    if int(GUESS)<NUMBER:
        print("Wrong,too low.")
    elif int(GUESS)>NUMBER:
        print("Wrong,too high.")
    elif GUESS.lower()=="exit":
        print ("Better luck next time.")
    elif int(GUESS)==NUMBER:
        print("Yes,that's the one,%s."%str(NUMBER))
    if TRY<2:
        print("Impressive,only%s tries."%str(TRY))
    elif TRY>2and TRY<10:
        print("Pretty good,%s tries." %str(TRY))
    else:
            print("Bad,%s tries."%str(TRY))
            RUNNING=False
    TRY +=1
