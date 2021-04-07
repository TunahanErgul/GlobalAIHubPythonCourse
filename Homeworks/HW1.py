
#Question 1
#Swapping second half the list with first half of the list and printing swapped version to screen


#swap second half with second half 
#list can be changed by user to test different cases

mylist = [7,2,5,0,0,9,8]
x = int(len(mylist)//2)
j=x

if int(len(mylist))%2 == 0:
    while j != int(len(mylist)):
        for i in range(x):
            temp=mylist[i]
            mylist[i]=mylist[j]
            mylist[j]=temp
            j=j+1
else:
    print("length of list must be even")
   
if int(len(mylist))%2 == 0:  
    print(mylist)

    
    
#Question 2
#Finding even numbers according to user's input

#Ask the user to input a single digit integer
#to a variable "n"
#then, print out all of the even numbers from 0 to n
#including n

n = int(input("Please enter a single digit integer \n"))

if n < 10 and n > 0:
    print("Even Numbers from 0 to {} are listed at below \n ".format(n))
    evennumbers = []
    for i in range(0,n+1):
        if i % 2 == 0:
            evennumbers.append(i)
    print(evennumbers)

else:
    print("You have not entered a single digit integer ")
