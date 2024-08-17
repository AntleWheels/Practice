def input_field():
    how_many = int(input("How many numbers you want to enter :"))
    return logical_operation(how_many)
def neon_nummber(number):
    squared_value = number**2
    string_value = str(squared_value)
    count =0
    for i in string_value:
        count =count +int(i)
    if count ==number :
        return number
def logical_operation(how_many):
    global number_collection
    global neon_nummbers
    number_collection =[]
    neon_nummbers =[]
    for i in range(how_many):
        number = int(input("Enter the number :"))
        number_collection.append(number)
    for j in number_collection:
        if neon_nummber(j):
            neon_nummbers.append(j)
    return display_field(neon_nummbers)
def display_field(neon_nummbers):
    print("In the entered list of numbers the Neon numbers are :",neon_nummbers)
    str = input("Do you want to continue(yes/no) :").strip().lower()
    if str == "yes":
        return input_field()
    else :
        print ("Thank you")
input_field()