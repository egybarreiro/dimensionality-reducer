from class_customer import Customer
from class_vehicle import Vehicle
from class_appointment import Appointment
from class_service_advisor import ServiceAdvisor
from class_workshop import Workshop
from class_json_manager import JsonManager



# Creates workshop system.

workshop = Workshop()



# Creates customer.

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



# Creates vehicle.

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



customer.register_vehicle(
    vehicle
)


workshop.register_vehicle(
    vehicle
)



# Creates appointment.

appointment = Appointment(

    customer=customer,

    vehicle=vehicle,

    appointment_date="2026-08-03 9:00 AM",

    customer_concern="Vehicle vibrates while braking."

)



# Creates service advisor.

advisor = ServiceAdvisor(

    advisor_id=101,

    name="Carlos",

    last_name="Rivera"

)



# Checks in vehicle.

advisor.check_in_vehicle(
    appointment
)



# Creates repair order.

repair_line = advisor.add_repair_line(

    "Customer states vehicle vibrates while braking."

)



repair_order = advisor.create_repair_order(

    appointment,

    [
        repair_line
    ]

)



workshop.register_repair_order(
    repair_order
)



# Displays workshop information before saving.

print(
    "WORKSHOP DATA BEFORE SAVING"
)

print(
    "--------------------------"
)


print(
    f"Customers: {len(workshop.customers)}"
)


print(
    f"Vehicles: {len(workshop.vehicles)}"
)


print(
    f"Repair Orders: {len(workshop.repair_orders)}"
)



# Saves information into JSON file.

json_manager = JsonManager()


print()


print(
    json_manager.save_workshop(
        workshop
    )
)