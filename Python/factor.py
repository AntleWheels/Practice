'''def input_field():
    number =int(input("Enter the starting number :"))
    return logical_operation(number)
def logical_operation(number):
    count =0
    factors =[]
    for i in range(1,number+1):
        sum = number%i
        if sum ==0:
           factors.append(i)
           count =count+1
    return output_field(factors,count,number)

def output_field(factors,count,number):
    print(f"The factors for the {number} are :",factors,f"This number has {count} factors")


input_field()'''
#for a range of numbers
'''start_number = int(input("Enter the starting number :"))
end_number = int(input("Enter the ending number :"))
factors=[]
for i in range(start_number,end_number+1):
    for j in range(1,i+1):
        if i%j==0:
            factors.append(j)
    print(factors)'''