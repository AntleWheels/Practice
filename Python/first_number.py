'''number = int(input("Enter the number :"))
string =str(number)
first_number =int(string[0])
print(first_number)'''

def input_field():
    number = int (input("Enter the number :"))
    return logical_operation(number)
def logical_operation(number):
    divisor=[]
    for i in range(2,number):
        if number%i==0:
            divisor.append(i)
            break
        else :
            print(f"It is a Prime number it will divisible by 1 and {number} itself ")
    return output_field(divisor,number)
def output_field(divisor,number):
    print(f"The first common divisor for the number {number} is :",divisor[0])

input_field()