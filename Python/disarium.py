def input_field():
    number = int(input("Enter the number :"))
    return logical_operation(number)
def logical_operation(number):
    count =0
    seperate_numbers =[]
    for i in str(number):
        count =count+1
        integer_convert =int(i)
        seperate_numbers.append(integer_convert**count)
    return output_field(seperate_numbers,number)
def output_field(seperate_numbers,number):
    count =0
    for number_in_array in seperate_numbers:
        count =count+number_in_array
    if number ==count:
        print(f"{number} is a Disarium number")
    else :
        print(f"{number} is not a Disarium number")

input_field()