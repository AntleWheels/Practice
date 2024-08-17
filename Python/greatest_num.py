def input_field():
    global range_value
    range_value = int(input("How many numbers you want to enter : "))
    return logical_operation(range_value)
def logical_operation(range_value):
    number =[]
    for i in range (1,range_value+1):
        elements = int(input("Enter the number : "))
        number.append(elements)
    global count
    count =number[1]
    for j in number :
        if j>count:
            count =j
    global position
    position = number.index(count)
    return count


object =input_field()
print(f"The greatest number amoung {range_value} numbers is :",count,f" which you have entered at {position+1} position while entering")
