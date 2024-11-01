#main file for the project

from flights import Flights

file = ""

y = 123
while(y == 123):
    print('\n      *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU \n'
          '1. Add flight \n'
          '2. Print flight schedule \n'
          '3. Set flight schedule filename \n'
          '4. Exit the program\n'
          'Enter menu choice: ')

    action = int(input())

    if (action == 1):
          if (file == ""):
            print("No file inserted")
        
          else:
                origin1 =  input("Enter origin: ")
                destination1 = input("Enter destination: ")
                flight1 = input("Enter flight number: ")
                departure1 = input("Enter depature time (HHMM): ")
                arrival1 = input("Enter arrival time (HHMM): ")
                YesNo1 = input("Is arrival next day (Y/N): ")

                x.add_flight(origin1, destination1, flight1, departure1, YesNo1, arrival1)
    elif (action == 2):
        print ("================== FLIGHT SCHEDULE ==================\n")
        print ("Origin Destination Number Departure  Arrival Duration\n")
        print ("====== =========== ====== =========  ======= ========\n")

        x.get_flights()


    elif (action == 3):
        file = input("What would you like to name the filename? : ")

        x = Flights(filename = file)
        
    elif (action == 4):
        break
