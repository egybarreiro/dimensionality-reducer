"""
Purpose: This module contains a simple MVP to manage a portion of a business operationof a 
mechanic workshop. It demonstrates the use of object-oriented programming principles, 
including encapsulation, inheritance, and polymorphism. The MVP allows for the management of customers, 
vehicles, appointments, repair orders, and service advisors.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-30 Modified: 2026-08-03
"""
 
# Main program file.
# Demonstrates the automotive repair shop MVP workflow.


from customer import Customer
from vehicle import Vehicle
from appointment import Appointment
from vehicle_scanner import VehicleScanner
from service_advisor import ServiceAdvisor
from workshop import Workshop
from json_manager import JsonManager



# -------------------------------
# 0. Create workshop system
# -------------------------------

workshop = Workshop()

json_manager = JsonManager()



# -------------------------------
# 1. Create customers
# -------------------------------

customer_1 = Customer(
    customer_id=1,
    name="Juan Rodriguez",
    phone="787-555-1234",
    email="juan.rodriguez@email.com",
    customer_type="Individual"
)



customer_2 = Customer(
    customer_id=2,
    name="Rodriguez Transport LLC",
    phone="787-555-5678",
    email="contact@rodrigueztransport.com",
    customer_type="Commercial"
)



# Register customers

workshop.register_customer(customer_1)

workshop.register_customer(customer_2)



# -------------------------------
# 2. Scan vehicle VIN information
# -------------------------------

scanner = VehicleScanner()



vin_1 = scanner.scan_barcode(
    "1HGCM82633A004352"
)



vin_2 = scanner.scan_barcode(
    "1FTFW1E50MFA12345"
)



# -------------------------------
# 3. Create vehicles
# -------------------------------

vehicle_1 = Vehicle(
    make="Honda",
    model="Accord",
    year=2020,
    color="Black",
    mileage=45000,
    vin=vin_1,
    license_plate="ABC123",
    usage_type="Personal"
)



vehicle_2 = Vehicle(
    make="Ford",
    model="F150",
    year=2021,
    color="White",
    mileage=60000,
    vin=vin_2,
    license_plate="XYZ789",
    usage_type="Commercial"
)



# Associate vehicles with customers

customer_1.register_vehicle(
    vehicle_1
)



customer_2.register_vehicle(
    vehicle_2
)



# Register vehicles in workshop

workshop.register_vehicle(
    vehicle_1
)



workshop.register_vehicle(
    vehicle_2
)



# -------------------------------
# 4. Display registered information
# -------------------------------

print(customer_1)

print("\n")

print(vehicle_1)



print("\n")

print(customer_2)



print("\n")

print(vehicle_2)



# -------------------------------
# 5. Create appointment
# -------------------------------

appointment = Appointment(
    customer=customer_1,
    vehicle=vehicle_1,
    appointment_date="2026-08-03 9:00 AM",
    customer_concern="Vehicle vibrates while braking."
)



# -------------------------------
# 6. Service advisor check-in
# -------------------------------

advisor = ServiceAdvisor(
    advisor_id=101,
    name="Carlos",
    last_name="Rivera"
)



print("\n")

print(
    advisor.check_in_vehicle(
        appointment
    )
)



# -------------------------------
# 7. Create repair order
# -------------------------------

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



# -------------------------------
# 8. Display repair order
# -------------------------------

print("\n")

print(
    repair_order.display_repair_order_summary()
)



# -------------------------------
# 9. Display vehicles by usage type
# -------------------------------

print("\n")

print(
    "Juan Personal Vehicles:"
)



print(
    "----------------------"
)



for vehicle in customer_1.get_vehicles_by_usage(
    "Personal"
):

    print(
        f"{vehicle.make} {vehicle.model}"
    )



print("\n")

print(
    "Commercial Customer Vehicles:"
)



print(
    "---------------------------"
)



for vehicle in customer_2.get_vehicles_by_usage(
    "Commercial"
):

    print(
        f"{vehicle.make} {vehicle.model}"
    )



# -------------------------------
# 10. Demonstrate workshop searches
# -------------------------------

print("\n")

print(
    "Workshop Search Examples:"
)



print(
    "------------------------"
)



found_customer = workshop.find_customer(
    1
)



print(
    f"Customer Found: {found_customer.name}"
)



found_vehicle = workshop.find_vehicle_by_license_plate(
    "ABC123"
)



print(
    f"Vehicle Found: {found_vehicle.make} {found_vehicle.model}"
)



found_order = workshop.find_repair_order(
    repair_order.repair_order_number
)



print(
    f"Repair Order Found: {found_order.repair_order_number}"
)



# -------------------------------
# 11. Workshop summary
# -------------------------------

print("\n")

print(
    "Workshop Summary:"
)



print(
    "-----------------"
)



print(
    f"Customers registered: {len(workshop.customers)}"
)



print(
    f"Vehicles registered: {len(workshop.vehicles)}"
)



print(
    f"Repair Orders registered: {len(workshop.repair_orders)}"
)



# -------------------------------
# 12. Save workshop data
# -------------------------------

print("\n")

print(
    json_manager.save_workshop(
        workshop
    )
)