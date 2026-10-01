from class_customer import Customer



# Represents an individual customer.
# Inherits common customer information from Customer.
# Adds behavior specific to personal vehicle ownership.

class IndividualCustomer(Customer):



    def __init__(
        self,
        customer_id,
        name,
        phone,
        email
    ):


        # Initializes inherited customer information.

        super().__init__(
            customer_id,
            name,
            phone,
            email,
            "Individual"
        )



    # Returns customer category information.

    def get_customer_category(self):

        return "Individual Customer"



    # Provides a specific message for individual customers.

    def display_customer_summary(self):

        base_summary = super().display_customer_summary()


        return (
            f"{base_summary}\n"
            f"Category: Individual Customer"
        )