'''
TINAMAD NA GAWIN OKAY NA UNG LOGIC

ROUTE: Sapang Palay - PITX

Name                 Distance
Sapang Palay
Rancho
ASSUMPTION
STO ROSARIO
STO NINO
LAWANG PARI
BBE
CITRUS
RD 2
QUARRY
RD 1
TOWERVILLE
PALMERA
TUNGKO
STI
MALARIA
FATIMA
FAIRVIEW

'''
from os import system
from random import randint
from sys import exit
from unittest import case


ROUTE = {
    "Sapang Palay": 0,
    "Rancho": 1,
    "Assumption": 1.2,
    "Sto. Rosario": 1.3,
    "Sto. Niño": 2.4,
    "Lawang Pari": 2.8,
    "Citrus": 3.2,
    "Road 2": 4.3,
    "Quarry": 4.7,
    "Road 1": 5,
    "Towerville": 5.9,
    "Palmera": 8.7,
    "Tungko": 12,
    "SM Tungko": 12.2,
    "STI": 13,
    "Malaria": 14.3,
    "Fatima": 19,   
    "Robinsons Novaliches": 20.8,
    "SM Fairview": 20.7,
    "Commonwealth Market": 26.6,
    "Litex": 26,
    "Batasan": 23.6,
    "Sandigan": 28,
    "Philcoa": 32.8,
    "Quezon Memorial Circle": 34,
    "Quezon Avenue": 34.2,
    "Welcome Rotonda": 40,
    "España": 41.2,
    "Quiapo": 42.7,
    "Lawton": 44.5,
    "Manila City Hall": 44.7,
    "United Nations": 45.3,
    "Pedro Gil": 45.6,
    "Quirino": 46.4,
    "Gil Puyat (Buendia)": 50,
    "Libertad": 50.7,
    "EDSA-Taft": 51,
    "Baclaran": 52.1,
    "MOA": 51.3,
    "PITX": 55
}

class Ticket:
    def __init__(self, price, distance):
        self.price = price
        self.distance = distance
        self.type_num = 0
        self.pass_type = ""
        self.boarding = ""
        self.destination = ""

    @staticmethod
    def calcdistance(boarding, destination):
        return abs(destination - boarding)
    
    @staticmethod
    def fare(ticket_distance, type_pass):
        return ticket_distance * 10
    
    def ticket(self, boarding, destination, pass_type):
        system('cls')
        self.id = randint(0, 999999)

        if self.type_num == 1:
            final_price = self.price * .8
        else:
            final_price = self.price

        print("***KLAREXPRESS***")
        print(f"Type: {pass_type}")
        print(f"From: {boarding}")
        print(f"To: {destination}")
        if self.type_num == 1:
            discount = self.price * .2
            print(f"Discount: 20% off: {self.price} x 20% = {discount:.2f}")
        print(f"Fare: {final_price}")
        print(f"Ticket ID: {self.id}")
        cont()

    def passenger_type(self):
        system("cls")
        print("***KLAREXPRESS***")
        print("PASSENGER TYPE")
        z=int(input("1.Regular\n2.Student\n3.Senior\n4.PWD\n5.Exit\nEnter Here: "))

        match z:
            case 1:
                self.type_num = 0
                self.pass_type = "Regular"
            case 2:
                self.type_num = 1
                self.pass_type = "Student"
            case 3: 
                self.type_num = 1
                self.pass_type = "Senior"
            case 4:
                self.type_num = 1
                self.pass_type = "PWD"
            case 5:
                print('EXITING...')
                exit(0)
            case _:
                print("INVALID")
                cont()


    def Boarding(self):
        system('cls')
        print("***KLAREXPRESS***")
        print("BOARDING")

        for i, j in enumerate(ROUTE):
            print(f"{i+1}. {j}")
        x=int(input("Enter the Number: "))

        self.boarding = list(ROUTE.keys())[x-1]
        return ROUTE[self.boarding]
   
    def Destination(self):
        system('cls')
        print("***KLAREXPRESS***")
        print("DESTINATION")
        for i, j in enumerate(ROUTE):
            print(f"{i+1}. {j}")
        x=int(input("Enter the Number: "))

        self.destination = list(ROUTE.keys())[x-1]
        return ROUTE[self.destination]
  
def cont():
    n=int(input("'0' RETURN || '1' EXIT: "))
    match n:
            case 0:
                main()
            case 1:
                print('EXITING...')
                exit(0)

def main():
    T = Ticket(0, 0)
   
    T.passenger_type()
    board = T.Boarding()
    desti = T.Destination()

    if board == desti:
        print("\n You're already in your destination")
        cont()

    T.distance=T.calcdistance(board, desti)
    T.price= T.fare(T.distance, T.type_num)
    T.ticket(T.boarding, T.destination, T.pass_type)

if __name__ == "__main__":
    main()
