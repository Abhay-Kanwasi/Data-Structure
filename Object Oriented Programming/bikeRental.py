import datetime

class Bikerental:

    def __init__(self,stock = 0):
        """ 
        Our constructor class that instantiates bike rental shop.
        """
        self.stock = stock
    
    def displaystock(self):
        """ 
        Display the currently avilable bikes for rent in the shop
        """
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock
    
    def rentBikeOnHour(self,n):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n<=0:
            print("Number of bikes should be positive.")
            return None

        elif n>self.stock:
            print("Sorry ! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that enjoy our service.")

            self.stock -= n
            return now
        
    def rentBikeOnDailyBasis(self,n):
        """ 
        Rents a bike on daily basis to a customer.
        """
        if n<=0:
            print("Number of bikes should be positive!")
            return None
        
        elif n>self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $20 for each hour per bike.")
            print("We hope that enjoy our service.")

            self.stock -= n
            return now
        
    def rentBikeOnWeeklyBasis(self,n):
        """ 
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that enjoy our service.")

            self.stock -= n
            return now

    def returnBike(self,request):
        """ 
        1. Accept a rented bike from a customer.
        2. Replensishes the inventory
        3. Return a bill
        """
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # hourly bill calculation

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds/3600) * 5 * numOfBikes
            
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
            
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days/7) * 60 * numOfBikes
            
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
            
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None

class Customer:

    def __init__(self):
        """ 
        Our constructor method which instantiates various 
        """
