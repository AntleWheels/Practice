def introduction():
    print("It is a Narrow Gauge Train Coach with 10 seats")
    return input_function()

def input_function():
    global UB, MB, LB, SL, SU, seats, passengers, count, number_of_passengers
    UB = [1, 4, 9]
    MB = [2, 5, 10]
    LB = [3, 6]
    SL = [7]
    SU = [8]
    seats = []
    passengers = []
    count = 0
    number_of_passengers = int(input("Enter the number of passengers: "))
    
    if number_of_passengers <= 10:
        return passenger_input()
    else:
        return decision()

def decision():
    print("Seats are not available, please enter only up to 10 passengers.")
    print("Beyond booking 10 seats will automatically be considered as RAC or Waiting List.")
    decision = str(input("Do you want to continue (yes/no): ").strip().lower())
    
    if decision == "yes":
        return passenger_input()    
    else:
        print("Thank you for visiting Antle Wings Platform")

def passenger_input():
    global count
    for i in range(number_of_passengers):
        name = str(input("Enter the name of the passenger: "))
        passengers.append(name)
        count += 1
        seats.append(count)
        if count > 10:
            return rac_and_waiting_list()

    return passenger_logic()  

def passenger_logic():
    for i, h in enumerate(passengers): # It is used to loop through passengers and retrieve the index. The index is then used to access the corresponding seat from the seats list,
        seat_number = seats[i] 
        if seat_number in UB:
            print(f"Passenger {h} is in Upper berth with Seat Number: {seat_number}")
        elif seat_number in MB:
            print(f"Passenger {h} is in Middle berth with Seat Number: {seat_number}")
        elif seat_number in LB:
            print(f"Passenger {h} is in Lower berth with Seat Number: {seat_number}")
        elif seat_number in SL:
            print(f"Passenger {h} is in Side Lower berth with Seat Number: {seat_number}")
        elif seat_number in SU:
            print(f"Passenger {h} is in Side Upper berth with Seat Number: {seat_number}")
        print("Happy Journey!")

def rac_and_waiting_list():
    if count >= 11 and count <= 15:
        print(f"Your position has moved to the RAC with Coach Number: {count - 10}")
    elif count >= 16 and count <= 35:
        print(f"Your position has changed to the Waiting List with WL number: {count - 15}")
    else:
        print("The train is almost full. Please try again on another date.")

introduction()
