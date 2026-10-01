from class_customer import Customer
from class_vehicle import Vehicle
from class_appointment import Appointment
from class_service_advisor import ServiceAdvisor
from class_workshop import Workshop



workshop = Workshop()



print("\nIntegration Test")
print("----------------")



# Create customer

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



# Create vehicle

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



# Create appointment

appointment = Appointment(
    customer=customer,
    vehicle=vehicle,
    appointment_date="2026-08-03 9:00 AM",
    customer_concern="Vehicle vibrates while braking."
)



# Service advisor workflow

advisor = ServiceAdvisor(
    advisor_id=101,
    name="Carlos",
    last_name="Rivera"
)



print(
    advisor.check_in_vehicle(
        appointment
    )
)



# Create repair order

repair_line = advisor.add_repair_line(
    "Inspect brake system."
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



print("\nRepair Order Created")
print("-------------------")

print(
    repair_order.display_repair_order_summary()
)



# Verify vehicle history

print("\nVehicle History")
print("----------------")


for order in vehicle.get_repair_history():

    print(
        order.repair_order_number,
        order.get_status()
    )



# Complete repair

print("\nCompleting Repair")
print("-----------------")


print(
    repair_order.complete_repair_order()
)



print(
    repair_order.display_repair_order_summary()
)