# total = int(input("Enter the total marks obtained by the individual :"))
# if total >=90 and total <=100:
#     print("Grade : O")
# elif total >=80 and total <90:
#     print("Grade : A")
# elif total >=70 and total <80:
#     print("Grade : B")
# elif total >=60 and total <70:
#     print("Grade : C")
# elif total >=50 and total <60:
#     print("Grade : D")
# elif  total>100 :
#     print("Enter the number which is less than the number 100")
# else :
#     print("Grade : F")
    

marks =[]
subjects =[]
number_of_subjects = int(input("Enter the Number of Subjects :"))
for i in range (number_of_subjects):
    # if str(i)[::-1]==2:
        subjects.append(str(input("Enter the ",i,"nd Subject :")))
    # else:
    #     print("pass")
print (subjects)