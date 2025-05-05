n="$"
for i in range(1,8,2):
    print((n*i).center(10))


# rows=15
# for i in range(1,rows+1):
#     for j in range(rows-i): #Calculates how many spaces to print before the stars.
#          print(" ",end="")
#     for k in range(2*i-1): # this is will print the stars
#         print("$",end="")
#     print()    
    
string="tenet\n"
string2= string * 10
print(string2)      
def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True 
def prime_generator(n):
    num=2
    while n:
        if isprime(num):
            yield num
            n-=1
        num+=1
x=int(input("Enter no. of prime numbers required"))
it=prime_generator(x)
for e in it :
    print(e,end=" ")     