def input_field():
    number = int(input("Enter the number :"))
    return logical_operation(number)
def logical_operation(number):
    count =0
    for i  in str(number):
        count =count +1
    return output_field(count)
def output_field(count):
    print("The number of digits in the number are :",count)


input_field()
"""number  = int(input("Enter the number :"))
print("The number of digits in the numbers are :",len(str(number)))"""