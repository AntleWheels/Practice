height = int(input("Enter the number :"))
for i in range (height+1,0,-1):
    for j in range (0,i-1):
        print("*",end="")
    print()