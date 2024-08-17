number = int (input("Enter the number :"))
squared_value = number**2
string_value = str(squared_value)
count =0
for i in string_value:
    count =count +int(i)
if count ==number :
    print(f"{number} is a Neon number")
else :
    print(f"{number} is not a Neon number")
   