import unittest
from datetime import datetime, timedelta
from bikeRental import BikeRental, Customer

class BikeRentalTest(unittest.TestCase):

    def test_Bike_Rental_displays_correct_stocks(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(),0)
        self.assertEqual(shop2.displaystock(),0)
    
    def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(-1), None)
    
    def test_rentBikeOnHourlyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.renBikeOnHourlyBasis(0), None)
        