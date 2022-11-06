# Activity 1
#           Accept two lists from user and display their join.
# Solution:
myList1=[]
print("Enter objects of first list...")
for i in range(5):
    val=input("enter a value:")
    n=int(val)
    myList1.append(n)

myList2=[]
print("Enter objects of second list...")
for i in range(5):
    val=input("Enter a avlue")
    n=int(val)
    myList2.append(n)

list3=myList1+myList2
print(list3)

#Activity 2:
#A palindrome is a string which is same read forward or backwards.
#For example: "dad" is the same in forward or reverse direction. Another example is "aibohphobia"
#which literally means, an irritable fear of palindromes.
#Write a function in python that receives a string and returns True if that string is a palindrome and
#False otherwise. Remember that difference between upper and lower case characters are ignored
#during this determination.

#Solution

def isPaindrome(word):
    temp=word[::-1]
    if temp.capitalize()==word.capitalize():
        return True
    else:
        return False

print(isPaindrome("deed"))


#Activity 3:
#Imagine two matrices given in the form of 2D lists as under; a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
#b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
#Write a python code that finds another matrix/2D list that is a product of and b, i.e., C=a*b
#Solution:
a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
c=[]
for indrow in range (3):
    c.append([])
    for indcol in range (3):
        c[indrow].append(0)
        for indaux in range (3):
            c[indrow][indcol] +=a[indrow][indaux] * b[indcol][indaux]

print(c)

#Activity 4:
#A closed polygon with N sides can be represented as a list of tuples of N connected coordinates, i.e.,
#[ (x1,y1), (x2,y2), (x3,y3), . . . , (xN,yN) ]. A sample polygon with 6 sides (N=6) is shown below.
#Write a python function that takes a list of N tuples as input and returns the perimeter of the
#polygon. Remember that your code should work for any value of N.
#Hint: A perimeter is the sum of all sides of a polygon.
#Solution:

def perimeter(listing):
    leng=len(listing)
    perimeter=0;
    for i in range(0,leng-1):
        dist=(((listing[i][0]-listing[i+1][0])**2)+
              ((listing[i][1]-listing[i+1][1])**2))**0.5
        perimeter=perimeter+dist
    perimeter=perimeter + (((listing[0][0]-listing[leng-1][0])**2)
                           +((listing[0][1]-listing[leng-1][1])**2))**0.5
    return perimeter

L = [1,3],(2,7),(3,9),(-1,8)
print(perimeter(L))


#Activity 5:
#Imagine two sets A and B containing numbers. Without using built-in set functionalities, write your
#own function that receives two such sets and returns another set C which is a symmetric difference
#of the two input sets. (A symmetric difference between A and B will return a set C which contains
#only those items that appear in one of A or B. Any items that appear in both sets are not included in
#C). Now compare the output of your function with the following built-in functions/operators.
#✓ A.symmetric_difference(B)
#✓ B.symmetric_difference(A)
#✓ A ^ B
#✓ B ^ A

#Solution:

#functiopn defined
def symmDiff(a,b):
    e=set()  #empty set
    for i in a: #for loop used to access in a
        if i not in b:
            e.add(i)
    for i in b: #for loop used to access in b
        if i not in a:
            e.add(i)
    return e
set1={0,1,2,4,5}
set2={4,5,7,8,9}
print(symmDiff(set1,set2))
#verification using inbuilt function
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print(set1^set2)
print(set2^set1)

 #Activity 6:
#Create a Python program that contains a dictionary of names and phone numbers. Use a tuple of
#separate first and last name values for the key field. Initialize the dictionary with at least three
#names and numbers. Ask the user to search for a phone number by entering a first and last name.
#Display the matching number if found, or a message if not found.
#Solution:

sample={("sohaib","ali"):"0246585468445",("alib","li"):"02465854645",
        ("sib","ai"):"0246585468445",}
firstName=input("enter first name")
lastname=input("enter last name")

searchTuple= (firstName,  lastname)
if searchTuple in sample:
    print(sample[searchTuple])
else:
    print("name not found")

    


