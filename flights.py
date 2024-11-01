# flights module

import json

import datetime

import time

class Flights():
    
    def __init__(self, filename):
        self.filename = filename

        self.datalist = []

        try:
             with open(self.filename, 'r') as input:
                self.datalist = json.load(input)
             print("Data has been loaded")
        except FileNotFoundError:
             print ("Filename was not found, has now been created")
    
    def add_flight(self, /, origin, destination, flight, departure, next_day, arrival):
        
        self.origin = origin
        self.destination = destination
        self.flight = flight
        self.departure = departure
        self.next_day = next_day
        self.arrival = arrival
        
        if (len(self.departure) != 4 or len(self.arrival) != 4):
            print ("Wrong input, please put in HHMM, nothing has occurred\n")
            return False
        else:

               departure_hour = int(self.departure[0:2])
               departure_minutes = int(self.departure[3:])

               arrival_hour = int(self.arrival[0:2])
               arrival_minutes = int(self.arrival[3:])
               
               self.updated_departure = datetime.time(departure_hour, departure_minutes)
               self.updated_arrival = datetime.time(arrival_hour, arrival_minutes)

               self.updated_departure = self.updated_departure.strftime("%#I:%M%p").lower()
               self.updated_arrival = self.updated_arrival.strftime("%#I:%M%p").lower()
               
               if self.next_day == 'Y':
                   self.updated_arrival = ('+' + str(self.updated_arrival))
                   arrive = datetime.timedelta(days  = 1, hours = arrival_hour, minutes = arrival_minutes)
                   departing = datetime.timedelta(hours = departure_hour, minutes = departure_minutes)
                   duration = str(arrive - departing)

                   duration = duration[:-3]

                   hours2,minutes2 = duration.split(':')

                   duration = (hours2 + ':' + minutes2)

               elif (self.next_day == 'N') :
                   arrive = datetime.timedelta(hours = arrival_hour, minutes = arrival_minutes)
                   departing = datetime.timedelta(hours = departure_hour, minutes = departure_minutes)
                   duration = str(arrive - departing)

                   duration = duration[:-3]

                   hours2,minutes2 = duration.split(':')

                   duration = (hours2 + ':' + minutes2)
            
                   

               self.temp_list = [self.origin, self.destination, self.flight, self.updated_departure, self.updated_arrival, duration]

               self.datalist.append(self.temp_list)


               with open(self.filename, 'w') as input:
                json.dump(self.datalist, input)

                return True
    
    def get_flights(self):
        new_list = []

        with open(self.filename, 'r') as input:
            new_list = json.load(input)

        for i in range(len(new_list)):
            print(f'{new_list[i][0]:<7}{new_list[i][1]:<12}{new_list[i][2]:<7}{new_list[i][3]:<11}{new_list[i][4]:<8}{new_list[i][5]:<8}')
        
        
