# Tests error handling and validation rules
# of the automotive repair shop MVP.
#
# Demonstrates:
# - Input validation
# - Duplicate data prevention
# - Business rule protection
# - Encapsulation behavior


from class_customer import Customer
from class_vehicle import Vehicle
from class_workshop import Workshop
from class_appointment import Appointment
from class_service_advisor import ServiceAdvisor



print("\nError Handling Test")
print("-------------------")



# -------------------------------------------------
# Test 1: Customer without required email
# -------------------------------------------------

print("\nTest 1: Customer without email")

try:

    invalid_customer = Customer(
        customer_id=1,
        name="Invalid Customer",
        phone="787-555-0000",
        email="",
        customer_type="Individual"
    )


except ValueError as error:

    print(
        "Expected error:",
        error
    )



# -------------------------------------------------
# Test 2: Vehicle without VIN
# -------------------------------------------------

print("\nTest 2: Vehicle without VIN")

try:

    invalid_vehicle = Vehicle(
        make="Toyota",
        model="Corolla",
        year=2022,
        color="White",
        mileage=10000,
        vin="",
        license_plate="AAA111",
        usage_type="Personal"
    )


except ValueError as error:

    print(
        "Expected error:",
        error
    )



# -------------------------------------------------
# Test 3: Duplicate customer registration
# -------------------------------------------------

print("\nTest 3: Duplicate customer registration")


workshop = Workshop()


customer = Customer(
    customer_id=1,
    name="Juan Rodriguez",
    phone="787-555-1234",
    email="juan@email.com",
    customer_type="Individual"
)



workshop.register_customer(
    customer
)



try:

    duplicate_customer = Customer(
        customer_id=1,
        name="Juan Rodriguez",
        phone="787-555-1234",
        email="juan2@email.com",
        customer_type="Individual"
    )


    workshop.register_customer(
        duplicate_customer
    )


except ValueError as error:

    print(
        "Expected error:",
        error
    )



# -------------------------------------------------
# Test 4: Duplicate vehicle registration
# -------------------------------------------------

print("\nTest 4: Duplicate vehicle registration")



vehicle = Vehicle(

    make="Honda",
    model="Accord",
    year=2020,
    color="Black",
    mileage=45000,
    vin="1HGCM82633A004352",
    license_plate="ABC123",
    usage_type="Personal"

)



workshop.register_vehicle(
    vehicle
)



try:

    duplicate_vehicle = Vehicle(

        make="Honda",
        model="Accord",
        year=2020,
        color="Black",
        mileage=45000,
        vin="1HGCM82633A004352",
        license_plate="XYZ789",
        usage_type="Personal"

    )


    workshop.register_vehicle(
        duplicate_vehicle
    )


except ValueError as error:

    print(
        "Expected error:",
        error
    )



# -------------------------------------------------
# Test 5: Creating repair order without check-in
# -------------------------------------------------

print("\nTest 5: Repair order without vehicle check-in")



appointment = Appointment(

    customer=customer,

    vehicle=vehicle,

    appointment_date="2026-08-03 9:00 AM",

    customer_concern="Brake vibration"

)



advisor = ServiceAdvisor(

    advisor_id=101,

    name="Carlos",

    last_name="Rivera"

)



repair_line = advisor.add_repair_line(
    "Inspect brake system."
)



try:

    advisor.create_repair_order(

        appointment,

        [
            repair_line
        ]

    )


except ValueError as error:

    print(
        "Expected error:",
        error
    )



# -------------------------------------------------
# Test 6: Completing repair order twice
# -------------------------------------------------

print("\nTest 6: Completing repair order twice")


advisor.check_in_vehicle(
    appointment
)


repair_order = advisor.create_repair_order(

    appointment,

    [
        repair_line
    ]

)



print(
    repair_order.complete_repair_order()
)



try:

    repair_order.complete_repair_order()



except ValueError as error:

    print(
        "Expected error:",
        error
    )



print("\nError tests completed successfully.")