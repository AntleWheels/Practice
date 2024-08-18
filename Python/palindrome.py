number = int(input ("Enter the number :"))
string_value = str(number)
reversed=""
for i in string_value[-1::-1]:
    reversed =reversed +i
integer=int(reversed)
if number ==integer:
    print(f"{number} is a palindrome number")
else:
    print(f"{number} is not a palindrome number")