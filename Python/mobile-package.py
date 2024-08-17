from datetime import date,timedelta
def decision():
    print("Wheater do you want to check the package validity or start a new package?(check/create)")
    user =str(input().strip().lower())
    if user =="check":
        return check_package_validity()
    elif user == "create":
        return input_field()
def input_field():
    global package
    global validity
    print("Select the package between the value (199/230/250/395) :")
    package = int(input("Enter the package amount :"))
    if package == 199:
        print(f"You have selected the package of {package} here you will get the benifits like 1GB/day ,Unlimmited Calls and 100 SMS per day")
        validity = 30
    elif package == 230:
        print(f"You have selected the package of {package} here you will get the benifits like 1.5GB/day ,Unlimmited Calls and 100 SMS per day")
        validity =30
    elif package == 250:
        print(f"You have selected the package of {package} here you will get the benifits like 2GB/day ,Unlimmited Calls and 100 SMS per day")
        validity =40
    elif package == 395:
        print(f"You have selected the package of {package} here you will get the benifits like 6GB/day ,Unlimmited Calls and 100 SMS per day")
        validity =84
    else:
        print(f"We dosnt provide the package amount {package} , please select the package between the value (199/230/250/395)")
    further = str(input("Do you want to continue ?(yes/no)"))
    if further.lower() in ["no","n"]:
        print("Thank you")
    elif further.lower() in ["yes","y"]:
        return pack_activation()
def pack_activation():
    global valid_from
    global valid_till
    global today
    today =date.today()
    valid_from = date.today()
    valid_till = valid_from + timedelta(days=validity)
    print(f"Your validity will start from {valid_from} and the plan will be valid for {valid_till} days")
    return decision()
def check_package_validity():
    global check
    check = date.today()
    if check > valid_till:#We dosnt provide any database when the validity is stored in the database we can able rto save the present date and also can able to check the validity 
        print (f"You have selected a package {package} which have validity for {validity} days")
        print (f"And you have consumed the validity for {check-valid_till} days")
        return decision()
    else :
        print("Your validity has expired ,Please recharge immediatly")
        return decision()
decision()