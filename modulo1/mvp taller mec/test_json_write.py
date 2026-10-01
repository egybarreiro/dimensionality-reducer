from class_customer import Customer
from class_vehicle import Vehicle
from class_workshop import Workshop
from class_json_manager import JsonManager



print("\nJSON Write Test")
print("----------------")



# Create workshop

workshop = Workshop()



# Create customer

customer = Customer(
    customer_id=1,
    name="Carlos Perez",
    phone="787-555-1111",
    email="carlos@email.com",
    customer_type="Individual"
)



workshop.register_customer(
    customer
)



# Create vehicle

vehicle = Vehicle(
    make="Toyota",
    model="Corolla",
    year=2022,
    color="Gray",
    mileage=30000,
    vin="JTDBR32E720123456",
    license_plate="AAA111",
    usage_type="Personal"
)



customer.register_vehicle(
    vehicle
)


workshop.register_vehicle(
    vehicle
)



# Create JSON manager

json_manager = JsonManager()



# Save data

result = json_manager.save_workshop(
    workshop
)



print(result)



print("\nFile Write Completed")
print("--------------------")

print(
    "Customer saved:",
    customer.name
)

print(
    "Vehicle saved:",
    vehicle.make,
    vehicle.model
)