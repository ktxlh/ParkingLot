import unittest
from parking_lot import Vehicle, VehicleType, ParkingLot, Car, Bike, Bus


class TestParkingLot(unittest.TestCase):

    def test_abc(self):
        try:
            Vehicle("Google", VehicleType.CAR)
        except TypeError as e:
            print("test_abc:", e)

    def test_park(self):
        parking_lot = ParkingLot(6, 30)
        res2 = parking_lot.park_vehicle(Car(10, "Amazon"))
        res3 = parking_lot.park_vehicle(Bike("Ann", "Amazon"))
        res4 = parking_lot.park_vehicle(Bus(30, "Microsoft"))

        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)

        while parking_lot.park_vehicle(Bike("Brian", "Verizon")):
            continue
            
        res5 = parking_lot.park_vehicle(Bike("Cherry", "Verizon"))
        self.assertFalse(res5)

    def test_leave_operation(self):
        parking_lot = ParkingLot(6, 30)
        self.assertTrue(parking_lot.park_vehicle(Car(20, "Google")))
        self.assertFalse(parking_lot.leave_operation(Bus(20, "Google")))
        self.assertTrue(parking_lot.leave_operation(Car(20, "Google")))
        self.assertFalse(parking_lot.leave_operation(Car(20, "Google")))

    def test_companyParked(self):
        parking_lot = ParkingLot(6, 30)
        self.assertTrue(parking_lot.park_vehicle(Car(20, "Google")))
        self.assertEqual(parking_lot.company_parked("Google"), [Car(20, "Google")])
        print(parking_lot.company_parked("Google"))

    def test_all(self):
        parking_lot = ParkingLot(3, 10)
        # Assume at least 1 parking spot for car.
        # First park a car, it should return True.
        self.assertTrue(parking_lot.park_vehicle(Car(10, "Google")))
        # Get the list of cars, it should give one car we parked.
        self.assertEqual(parking_lot.company_parked("Google"), [Car(10, "Google")])
        # Remove that car successfully.
        self.assertTrue(parking_lot.leave_operation(Car(10, "Google")))
        # Now the list of cars should be empty.
        self.assertEqual(parking_lot.company_parked("Google"), [])


if __name__ == '__main__':
    unittest.main()
