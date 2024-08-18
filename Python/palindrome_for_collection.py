def input_field():
    global input_number_count
    input_number_count = int(input("How many numbers you want to enter :"))
    return logical_operation(input_number_count)
def palindrome(j):
    number =str(j)
    revesed_number =number[-1::-1]
    if number ==revesed_number:
        return j
def logical_operation(input_number_count):
    numbers =[]
    count=0
    for i in range (input_number_count):
        global palindrome_numbers
        palindrome_numbers =[]
        input_number =int(input("Enter the number :"))
        numbers.append(input_number)

    for j in numbers:
        if palindrome(j):
            palindrome_numbers.append(j)
        else:
            count =count + j
            if count ==0:
                palindrome_numbers.append(j)
    return output_field()

def output_field():
    print("The palindrome numbers are :",palindrome_numbers)
    str = input("Do you want to continue(yes/no) :").strip().lower()
    if str == "yes":
        return input_field()
    else :
        print ("Thank you")

input_field()