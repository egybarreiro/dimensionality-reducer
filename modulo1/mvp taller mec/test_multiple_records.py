from class_customer import Customer
from class_vehicle import Vehicle
from class_workshop import Workshop
from class_appointment import Appointment
from class_service_advisor import ServiceAdvisor



# Create workshop system

workshop = Workshop()



# Create customers

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



# Create vehicles

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



# Associate vehicles with customers

customer_1.register_vehicle(
    vehicle_1
)


customer_2.register_vehicle(
    vehicle_2
)



# Register data in workshop

workshop.register_customer(
    customer_1
)


workshop.register_customer(
    customer_2
)


workshop.register_vehicle(
    vehicle_1
)


workshop.register_vehicle(
    vehicle_2
)



# Create service advisor

advisor = ServiceAdvisor(
    advisor_id=101,
    name="Carlos",
    last_name="Rivera"
)



# Create appointments

appointment_1 = Appointment(
    customer=customer_1,
    vehicle=vehicle_1,
    appointment_date="2026-08-05",
    customer_concern="Brake vibration"
)


appointment_2 = Appointment(
    customer=customer_2,
    vehicle=vehicle_2,
    appointment_date="2026-08-06",
    customer_concern="Engine noise"
)



# Check-in vehicles

print(
    advisor.check_in_vehicle(
        appointment_1
    )
)


print(
    advisor.check_in_vehicle(
        appointment_2
    )
)



# Display customer vehicles

print("\nCustomer Vehicles:")
print("------------------")


for vehicle in workshop.find_customer_vehicles(1):

    print(
        vehicle.make,
        vehicle.model
    )


for vehicle in workshop.find_customer_vehicles(2):

    print(
        vehicle.make,
        vehicle.model
    )



# Verify separation of data

print("\nVerification:")
print("------------")


print(
    workshop.find_customer(1).name,
    "owns",
    workshop.find_customer_vehicles(1)[0].model
)


print(
    workshop.find_customer(2).name,
    "owns",
    workshop.find_customer_vehicles(2)[0].model
)