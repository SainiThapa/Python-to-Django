# Write a class Bus which has methods to book a ticket, get status (No of Seats)
# and get fare information of buses under Bus Sewa yatayat
class Bus:
    service="Bus Sewa yatayat"
    def __init__(self,name,seats,fare):
        self.name=name
        self.seat=seats
        self.fare=fare
    def getStatus(self):
        print(f"\nBus Name : {self.name}")
        print(f"Available seats : {self.seat}")
    
    def getFareinfo(self):
        print(f"Fare amount : Rs.{self.fare}")
    def bookTicket(self):
        if self.seat>0:
            print(f"\nYour ticket is booked !!\nYour seat number is {self.seat}")
            self.seat=self.seat-1
        else:
            print("The bus has no seats available, kindly look for another bus")
    
    def cancelTicket(self,seatno):
        print(f"\nYour ticket has been cancelled and you're getting 50% refund (Rs.{self.fare*0.5})")
        self.seat+=1

Driver1=Bus('SALEENA',1,1500)
Driver1.getStatus()
Driver1.getFareinfo()
Driver1.bookTicket()
print(f"\nThank you for visiting us!!\n\t{Driver1.service}")

Driver1.getStatus()
Driver1.bookTicket()

Driver1.cancelTicket(Driver1.seat)
Driver1.getStatus()