from class_individual_customer import IndividualCustomer
from class_commercial_customer import CommercialCustomer



print("\nOOP Test")
print("--------")



# -------------------------------
# Individual Customer
# -------------------------------

individual_customer = IndividualCustomer(
    customer_id=1,
    name="Maria Lopez",
    phone="787-555-9999",
    email="maria@email.com"
)


print("\nIndividual Customer")
print("-------------------")

print(individual_customer)

print(
    individual_customer.get_customer_category()
)



# -------------------------------
# Commercial Customer
# -------------------------------

commercial_customer = CommercialCustomer(
    customer_id=2,
    name="Rodriguez Transport LLC",
    phone="787-555-5678",
    email="contact@rodrigueztransport.com",
    company_name="Rodriguez Transport LLC"
)


print("\nCommercial Customer")
print("-------------------")

print(commercial_customer)

print(
    commercial_customer.get_customer_category()
)



# -------------------------------
# Polymorphism
# -------------------------------

print("\nPolymorphism Test")
print("-----------------")


customers = [
    individual_customer,
    commercial_customer
]


for customer in customers:

    print(
        customer.get_customer_category()
    )
    