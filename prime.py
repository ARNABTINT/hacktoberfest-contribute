n = int(input("Enter Number:"))
f = 0
for i in range(2,n):
    if(n%i==0):
        f = 1
        break
          if(f==0):
            print("The number is Prime ")
            
    else:
         print("The number is Not Prime ")
