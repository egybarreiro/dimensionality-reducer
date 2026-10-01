from class_json_manager import JsonManager



# Creates JSON manager.

json_manager = JsonManager()



# Loads workshop information from JSON file.

workshop_data = json_manager.load_workshop()



# Displays loaded information.

print(
    "JSON Data Loaded Successfully"
)

print(
    "----------------------------"
)



print(
    "\nCustomers:"
)

for customer in workshop_data["customers"]:

    print(
        f"ID: {customer['customer_id']} | "
        f"Name: {customer['name']} | "
        f"Type: {customer['customer_type']}"
    )



print(
    "\nVehicles:"
)

for vehicle in workshop_data["vehicles"]:

    print(
        f"{vehicle['make']} {vehicle['model']} "
        f"({vehicle['year']}) | "
        f"VIN: {vehicle['vin']}"
    )



print(
    "\nRepair Orders:"
)

for order in workshop_data["repair_orders"]:

    print(
        f"Order: {order['repair_order_number']} | "
        f"Status: {order['status']}"
    )