from vehicles import Vehicle, Car, Bike


def main():

    print("My Vehicles App")

    vehicle1 = Vehicle()
    print(vehicle1)

    car1 = Car()
    print(car1)

    bike1 = Bike()
    print(bike1)

    print(vehicle1.get_vehicle_type())
    print(car1.get_vehicle_type())
    print(bike1.get_vehicle_type())

    return


if __name__ == "__main__":
    main()