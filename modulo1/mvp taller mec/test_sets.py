# Test file for verifying set-based duplicate prevention.
# Tests duplicate emails, VINs, and license plates.


from class_customer import Customer
from class_vehicle import Vehicle
from class_workshop import Workshop



# -------------------------------
# Create workshop system
# -------------------------------

workshop = Workshop()



# -------------------------------
# Test duplicate customer email
# -------------------------------


print("\n")
print("Testing Duplicate Customer Email:")
print("--------------------------------")


customer_1 = Customer(
    customer_id=1,
    name="Juan Rodriguez",
    phone="787-555-1111",
    email="juan@email.com",
    customer_type="Individual"
)


customer_2 = Customer(
    customer_id=2,
    name="Maria Lopez",
    phone="787-555-2222",
    email="juan@email.com",
    customer_type="Individual"
)



workshop.register_customer(
    customer_1
)


try:

    workshop.register_customer(
        customer_2
    )


except ValueError as error:

    print(error)



# -------------------------------
# Test duplicate VIN
# -------------------------------


print("\n")
print("Testing Duplicate VIN:")
print("----------------------")


vehicle_1 = Vehicle(
    make="Honda",
    model="Accord",
    year=2020,
    color="Black",
    mileage=45000,
    vin="VIN123",
    license_plate="ABC123",
    usage_type="Personal"
)


vehicle_2 = Vehicle(
    make="Toyota",
    model="Corolla",
    year=2022,
    color="White",
    mileage=30000,
    vin="VIN123",
    license_plate="XYZ789",
    usage_type="Personal"
)



workshop.register_vehicle(
    vehicle_1
)



try:

    workshop.register_vehicle(
        vehicle_2
    )


except ValueError as error:

    print(error)



# -------------------------------
# Test duplicate license plate
# -------------------------------


print("\n")
print("Testing Duplicate License Plate:")
print("--------------------------------")


vehicle_3 = Vehicle(
    make="Ford",
    model="F150",
    year=2021,
    color="Blue",
    mileage=50000,
    vin="VIN999",
    license_plate="ABC123",
    usage_type="Commercial"
)



try:

    workshop.register_vehicle(
        vehicle_3
    )


except ValueError as error:

    print(error)