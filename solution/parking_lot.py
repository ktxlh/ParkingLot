import random
from enum import Enum
from abc import ABC, ABCMeta, abstractmethod


class VehicleType(Enum):
    """Vehicle type class for all types of vehicles that can be parked."""
    
    CAR = 1
    BIKE = 2
    BUS = 3


class Vehicle(ABC, metaclass=ABCMeta):
    """A vehicle for license plate, company name and their type."""

    def __init__(self, company_name, type_of_vehicle):  # self for the first argument to instance methods.
        self.company_name = company_name
        self.type_of_vehicle = type_of_vehicle

    def get_type(self):
        return self.type_of_vehicle

    @abstractmethod
    def __eq__(self, other):
        """Checks if two vehicle objects are the same.
        
        Overwrites __eq__ methods. Otherwise, they will be checked at hashcode 
        level not at content level.
        """

        if other is None:
            return False
        if self.type_of_vehicle != other.type_of_vehicle:
            return False
        if self.company_name != other.company_name:
            return False
        return True


class Car(Vehicle):
    """A car. 
    
    Inherited from Vehicle class for license plate, company name and their type.
    """

    def __init__(self, license_plate, company_name):
        Vehicle.__init__(self, company_name, VehicleType.CAR)
        self.license_plate = license_plate

    def __eq__(self, other):
        if Vehicle.__eq__(self, other) == False:
            return False
        if self.license_plate != other.license_plate:
            return False
        return True


class Bike(Vehicle):
    """A bike. 
    
    Inherited from Vehicle class for license plate, company name and their type.
    """

    def __init__(self, owner_name, company_name):
        Vehicle.__init__(self, company_name, VehicleType.BIKE)
        self.owner_name = owner_name

    def __eq__(self, other):
        if Vehicle.__eq__(self, other) == False:
            return False
        if self.owner_name != other.owner_name:
            return False
        return True


class Bus(Vehicle):
    """A bus. 

    Inherited from Vehicle class for license plate, company name and their type.
    """

    def __init__(self, license_plate, company_name):
        Vehicle.__init__(self, company_name, VehicleType.BUS)
        self.license_plate = license_plate

    def __eq__(self, other):
        if Vehicle.__eq__(self, other) == False:
            return False
        if self.license_plate != other.license_plate:
            return False
        return True

class Slot:

    def __init__(self, lane, spot_number, type_of_vehicle):
        self.lane = lane
        self.spot_number = spot_number
        self.type_of_vehicle = type_of_vehicle
        self._vehicle = None  # "suggested" private

    def is_available(self):
        return self._vehicle == None

    def park(self, vehicle):
        if not self.is_available():
            return False
        if vehicle.type_of_vehicle == self.type_of_vehicle:
            self._vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        vehicle = self.get_vehicle()
        self._vehicle = None
        return vehicle

    def get_vehicle(self):
        return self._vehicle


class Level:
    """A level in a parking lot.
    
    Level class - Each level is an independent entity with a floor number, its 
    lanes and the slots within it. The number of lanes are designed based on 
    the number of slots. 10 slots make one lane.
    """

    def __init__(self, floor_number, num_of_slots):
        self.spots_per_lane = 10
        self.floor_number = floor_number
        self.lanes = num_of_slots // self.spots_per_lane
        self.spots = []

        # Check available spots in a lane
        for lane in range(self.lanes):
            for i in range(self.spots_per_lane):
                # Randomly assign a type to each slot.
                self.spots.append(
                    Slot(lane, i, random.choice(list(VehicleType))))

    def park(self, vehicle):
        """Parks a vehicle if some spot is available."""

        for slot in self.spots:
            if slot.park(vehicle):
                return True
        return False

    def remove(self, vehicle):
        """Removes a vehicle from the spot it is parked."""

        for spot in self.spots:
            if spot.get_vehicle() == vehicle:
                spot.remove_vehicle()
                return True
        return False

    def company_parked(self, company_name):
        """Shows the company name for the vehicles parked at the level."""

        all_vehicles = []
        for spot in self.spots:
            vehicle = spot.get_vehicle()
            if (vehicle is not None) and (vehicle.company_name == company_name):
                all_vehicles.append(vehicle)
        return all_vehicles


class ParkingLot:
    """A parking lot of one or more levels.
    
    A parking lot is made up of 'n' number of levels/floors and 'm' number of 
    slots per floor.
    """

    def __init__(self, num_of_floor, num_of_slot):
        self.levels = []
        for i in range(num_of_floor):
            self.levels.append(Level(i, num_of_slot))

    def park_vehicle(self, vehicle):
        """Inserts a vehicle and takes care of what company the vehicle is."""

        for level in self.levels:
            if level.park(vehicle):
                return True
        return False

    def leave_operation(self, vehicle):
        """Removes a vehicle 'C' in a level 'm'."""

        for level in self.levels:
            if level.remove(vehicle):
                return True
        return False

    def company_parked(self, company_name):
        """Show the list of vehicles parked for a particular company."""

        all_vehicles = []
        for level in self.levels:
            all_vehicles.extend(level.company_parked(company_name))
        return all_vehicles
