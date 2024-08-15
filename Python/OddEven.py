# In the given number, Seperate the odd and even number then Find the difference 
number_count =int(input("How many number :"))
number_collections =[]
odd_numbers=[]
even_numbers=[]
odd_sum =0
even_sum =0
for i in range (number_count):
    number =int (input("Enter the Element :"))
    number_collections.append(number)
    if number%2==0:
        even_numbers.append(number)
        even_sum =even_sum+number 
    else:
        odd_numbers.append(number)
        odd_sum =odd_sum+number
Odd_length =len(odd_numbers)
Even_length =len(even_numbers)
print(number_collections)
difference = Odd_length - Even_length
if difference<0:
    even_difference=  Even_length - Odd_length
    print("The number of even numbers are larger than the odd numbers by",even_difference,"and then the difference between the Sum of Odd and the even numbers is ",even_sum-odd_sum)
    print("The total sum of the even numbers is :",even_sum)
    print(odd_numbers)
    user_wish = str(input("Do you wish to get the sum of odd numbers in the list of numbers ?"))
    if user_wish=="yes" or "y" or "Yes"or "YES":
        print(odd_sum)
    else :
        print()
elif Odd_length == Even_length:
    print("The number of odd and even numbers are same")
    print("Length of both odd and even elements",Even_length)
    print("Sum of Even Numbers :",even_sum)
    print("The even numbers are :",even_numbers)
    print("The sum of Odd numbers are :",odd_sum)
    print("The odd numbers are :",odd_numbers)
else:
    print("The number of odd numbers are larger than then even numbers by ",difference,"and the difference between the sum of the odd and even numbers is ",odd_sum-even_sum)
    print("The sum of odd numbers in the given list of numbers is :",odd_sum)
    print(even_numbers)
    user_wish = str(input("Do you want to see the sum of the even numbers ?"))
    if user_wish =="YES" or "yes" or "y" or "Yes" or "Y":
        print(even_sum)
    else :
        print()
