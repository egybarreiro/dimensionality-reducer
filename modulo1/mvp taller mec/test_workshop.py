from class_customer import Customer
from class_vehicle import Vehicle
from class_workshop import Workshop


workshop = Workshop()


customer_1 = Customer(
    customer_id=1,
    name="Juan Rodriguez",
    phone="787-555-1111",
    email="juan@email.com"
)


customer_2 = Customer(
    customer_id=2,
    name="Maria Lopez",
    phone="787-555-2222",
    email="maria@email.com"
)


vehicle_1 = Vehicle(
    make="Honda",
    model="Accord",
    year=2020,
    color="Black",
    mileage=45000,
    vin="1HGCM82633A004352",
    license_plate="ABC123"
)


vehicle_2 = Vehicle(
    make="Toyota",
    model="Corolla",
    year=2022,
    color="White",
    mileage=30000,
    vin="2HGCM82633A004999",
    license_plate="XYZ789"
)


workshop.register_customer(customer_1)
workshop.register_customer(customer_2)


workshop.register_vehicle(vehicle_1)
workshop.register_vehicle(vehicle_2)


print(workshop.find_customer(1).name)

print(workshop.find_vehicle(
    "2HGCM82633A004999"
).model)


print(
    workshop.find_vehicle_by_license_plate(
        "ABC123"
    ).make
)


print("\nTesting Duplicate Vehicle Prevention:")
print("-----------------------------------")


try:

    duplicate_vehicle = Vehicle(
        make="Honda",
        model="Civic",
        year=2023,
        color="Blue",
        mileage=10000,
        vin="1HGCM82633A004352",
        license_plate="NEW123"
    )


    workshop.register_vehicle(
        duplicate_vehicle
    )


except ValueError as error:

    print(error)