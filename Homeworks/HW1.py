#Swapping second half the list with first half of the list and printing swapped version to screen

#Question 1

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
