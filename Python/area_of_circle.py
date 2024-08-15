#define the pie value =3.124
#create the input function 
#then  send to the operating function 

def input_elements():
    pie = 3.124
    radius = int(input("Enter the value of radius :")) 
    return operation(pie ,radius)
def operation(pie,radius):
    area = pie *(radius*radius)
    print("The Area of Circle is :",area)

input_elements()