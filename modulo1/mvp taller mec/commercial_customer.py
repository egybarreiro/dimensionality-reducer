from class_customer import Customer



# Represents a commercial customer.
# Inherits common customer information from Customer.
# Adds behavior specific to business vehicle owners.

class CommercialCustomer(Customer):



    def __init__(
        self,
        customer_id,
        name,
        phone,
        email,
        company_name
    ):


        # Initializes inherited customer information.

        super().__init__(
            customer_id,
            name,
            phone,
            email,
            "Commercial"
        )



        # Stores commercial customer information.

        if not company_name or not company_name.strip():

            raise ValueError(
                "Company name is required."
            )


        self.company_name = company_name.strip()



    # Returns customer category information.

    def get_customer_category(self):

        return "Commercial Customer"



    # Provides a specific message for commercial customers.

    def display_customer_summary(self):

        base_summary = super().display_customer_summary()


        return (
            f"{base_summary}\n"
            f"Category: Commercial Customer\n"
            f"Company: {self.company_name}"
        )