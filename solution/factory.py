from parking_lot import VehicleType, Car, Bike, Bus


class VehicleFactory:

    def create_vehicle(vehicle_type, **kwargs):
        if (vehicle_type == VehicleType.CAR):
            return Car(kwargs['license_plate'], kwargs['company_name'])
        if (vehicle_type == VehicleType.BUS):
            return Bus(kwargs['license_plate'], kwargs['company_name'])
        if (vehicle_type == VehicleType.BIKE):
            return Bike(kwargs['owner_name'], kwargs['company_name'])
        return None


if __name__ == "__main__":
    my_bus = VehicleFactory.create_vehicle(
        VehicleType.BUS, 
        license_plate = "RL-CTCI",
        company_name = "Amazon",
    )
