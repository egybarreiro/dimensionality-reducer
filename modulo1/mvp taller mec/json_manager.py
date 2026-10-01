import json
import os



# Handles reading and writing workshop information
# using a JSON file as persistent storage.


class JsonManager:



    def __init__(
        self,
        filename="workshop_data.json"
    ):


        # Creates a stable file path
        # based on this project folder.

        self.filename = os.path.join(
            os.path.dirname(__file__),
            filename
        )



    # Saves workshop information into JSON file.

    def save_workshop(
        self,
        workshop
    ):


        if workshop is None:

            raise ValueError(
                "Workshop information is required."
            )



        data = {

            "customers": [],

            "vehicles": [],

            "repair_orders": []

        }



        # Save customers.

        for customer in workshop.customers.values():

            data["customers"].append({

                "customer_id": customer.customer_id,

                "name": customer.name,

                "phone": customer.phone,

                "email": customer.email,

                "customer_type": customer.customer_type

            })



        # Save vehicles.

        for vehicle in workshop.vehicles.values():

            data["vehicles"].append({

                "make": vehicle.make,

                "model": vehicle.model,

                "year": vehicle.year,

                "color": vehicle.color,

                "mileage": vehicle.mileage,

                "vin": vehicle.vin,

                "license_plate": vehicle.license_plate,

                "usage_type": vehicle.usage_type

            })



        # Save repair orders.

        for order in workshop.repair_orders.values():

            data["repair_orders"].append({

                "repair_order_number": order.repair_order_number,

                "customer_id": order.customer.customer_id,

                "vin": order.vehicle.vin,

                "status": order.get_status()

            })



        # Writes information into JSON file.

        with open(
            self.filename,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(

                data,

                file,

                indent=4

            )



        return "Workshop data successfully saved."





    # Loads workshop information from JSON file.

    def load_workshop(self):


        try:

            with open(

                self.filename,

                "r",

                encoding="utf-8"

            ) as file:


                return json.load(file)



        except FileNotFoundError:


            return {

                "customers": [],

                "vehicles": [],

                "repair_orders": []

            }