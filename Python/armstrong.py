print(" Either want to check the armstrong number for the single or the range of numbers( Single / Series ) ?")
input_form=str(input()).strip().lower()#strip function is used to remove the white spaces from the string and lower function is used to convert the string into lower case
if input_form == "single":
    number = int(input("Enter the number :"))
    String_number  = str(number)
    length = len(String_number)
    total =0
    for i in String_number:
        total =total + int(i)**length

    if total ==number :
        print(f"{number} is a Armstrong number")
    else :
        print(f"{number} is not a Armstrong number")
elif input_form == "series":
    start = int (input("enter the starting number :"))
    end = int(input("enter the ending number :"))
    armstrong =[]
    for i in range (start ,end+1):
        String_number = str(i)
        length = len(String_number)
        total = 0
        for j in String_number:
            total=total +int(j)**length
        if total ==i:
            armstrong.append(i)
        else :
            pass

    print(armstrong)
else:
    print("Invalid Input")      
