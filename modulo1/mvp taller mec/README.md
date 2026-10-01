# Automotive Repair Shop Management System (MVP)

## Project Overview

The Automotive Repair Shop Management System is a Python-based MVP designed to organize and manage the main operational processes of an automotive repair business.

The system focuses on improving customer management, vehicle identification, appointment coordination, repair order tracking, and information organization.

The project was developed using Object-Oriented Programming principles to create a modular, maintainable, and scalable software structure.

---

# Business Problem

Automotive repair shops handle multiple entities simultaneously:

- Customers
- Vehicles
- Appointments
- Repair orders
- Service advisors
- Repair history

Without a structured system, common problems may occur:

- Loss of customer information
- Vehicle identification errors
- Difficulty tracking repair progress
- Duplicate records
- Poor organization of repair history

This MVP addresses these challenges by creating relationships between objects and maintaining controlled information flow.

---

# Solution Description

The system allows the workshop to:

- Register customers
- Classify customers by type
- Register vehicles
- Associate vehicles with customers
- Schedule appointments
- Perform vehicle check-in
- Create repair orders
- Track repair status
- Store repair history
- Save information using JSON persistence

---

# System Architecture

The project follows an Object-Oriented architecture where each class represents a real-world entity or system responsibility.


                Workshop
                   |
    --------------------------------
    |              |               |
Customer       Vehicle       RepairOrder
    |              |               |
    |              |               |
Individual     Repair History   Repair Lines
Commercial
Dealer

ServiceAdvisor
|
|
Creates Repair Orders

Appointment
|
|
Connects Customer + Vehicle

    
---

# Class Structure

## Customer

Represents the customer entity.

### Attributes

- customer_id
- name
- phone
- email
- customer_type
- current_vehicles


### Responsibilities

- Store customer information
- Manage associated vehicles
- Update contact information


---

## IndividualCustomer

Child class of Customer.

Uses inheritance to represent personal vehicle owners.

Additional behavior:

- Individual customer classification


---

## CommercialCustomer

Child class of Customer.

Represents business customers.

Additional attributes:

- company_name


---

## Vehicle

Represents vehicles registered in the workshop.

### Attributes

- make
- model
- year
- color
- mileage
- VIN
- license_plate
- usage_type
- repair_history


Responsibilities:

- Store vehicle identity
- Maintain repair history


---

## Appointment

Represents scheduled customer visits.

Responsibilities:

- Associate customer and vehicle
- Control appointment status
- Handle vehicle check-in


---

## ServiceAdvisor

Represents the employee responsible for customer intake.

Responsibilities:

- Check-in vehicles
- Create repair lines
- Generate repair orders


---

## RepairOrder

Represents the repair process.

Attributes:

- repair_order_number
- customer
- vehicle
- service_advisor
- repair_lines
- status
- timestamps


Responsibilities:

- Track repair progress
- Store repair information
- Update completion status


---

## Workshop

Acts as the central management system.

Responsibilities:

- Store customers
- Store vehicles
- Store repair orders
- Search information
- Prevent duplicated records


---

# Object-Oriented Programming Implementation

## Encapsulation

Encapsulation was implemented by protecting internal system data.

Examples:

- Repair order status
- Completion timestamps
- Repair history

These values are controlled through methods instead of direct modification.

Example:

complete_repair_order()

changes the repair status safely.


---

## Inheritance

Inheritance is implemented using Customer as the parent class.

Structure:

         Customer

    /              \
Individual       Commercial

Both child classes inherit:

- name
- phone
- email
- customer information

while adding specialized behavior.

---

## Polymorphism

Different customer classes respond differently to the same method.

Example:

get_customer_category()


Returns:

Individual Customer

or

Commercial Customer


The same method produces different behavior depending on the object type.

---

# Data Structures Used

## Dictionaries

Used in Workshop.

Example:

customers = {
customer_id : Customer object
}


Advantages:

- Fast searching
- Organized key-value relationship
- Efficient data access


---

## Sets

Used to prevent duplicated information.

Examples:

- Registered emails
- License plates


Benefits:

- Avoid duplicate records
- Faster validation


---

## Lists

Used for information that can grow dynamically.

Examples:

- Customer vehicles
- Repair history
- Repair lines


Benefits:

- Flexible quantity management
- Easy modification


---

# Program Workflow

START

|
|
Create Workshop

|
|
Register Customer

|
|
Register Vehicle

|
|
Associate Vehicle -> Customer

|
|
Create Appointment

|
|
Vehicle Check-In

|
|
Create Repair Order

|
|
Track Repair Status

|
|
Complete Repair

|
|
Save Information

|
|
END

---

# File Management

The system includes JSON persistence.

Class:

JsonManager


Responsibilities:

- Save workshop information
- Load stored information


Stored data:

- Customers
- Vehicles
- Repair Orders


---

# Validation and Error Handling

The system includes input validation using exceptions.

Examples:

- Missing customer information
- Duplicate customers
- Duplicate vehicles
- Invalid vehicle data
- Invalid repair order states


This prevents inconsistent data.


---

# Testing

The project includes:

## Integration Test

Validates complete workflow:

Customer creation

↓

Vehicle registration

↓

Appointment

↓

Check-in

↓

Repair Order

↓

Completion


---

## OOP Test

Validates:

- Inheritance
- Polymorphism


---

## JSON Read Test

Validates stored information retrieval.


---

# Scalability Considerations

The current version is an MVP designed for demonstration and learning purposes.

However, the architecture was created considering future scalability.

Possible future improvements:

- Database integration
- User authentication
- Role permissions
- Mobile application
- Real barcode/VIN scanner integration
- Cloud storage
- Customer notifications
- Inventory management
- Check Out/Shopping Cart
- API's


---

# Conclusion

This MVP demonstrates how Object-Oriented Programming can be applied to solve a real business problem.

Through proper class design, relationships between objects, validation, and structured data management, the system provides a foundation for a future professional automotive management platform.

# Simplified UML Diagram

                         +----------------------+
                         |       Customer       |
                         +----------------------+
                         | - customer_id        |
                         | - name               |
                         | - phone              |
                         | - email              |
                         | - customer_type      |
                         | - current_vehicles[] |
                         +----------------------+
                         | + register_vehicle() |
                         | + remove_vehicle()   |
                         | + update_contact()   |
                         | + display_summary()  |
                         +----------------------+
                                   ^
                                   |
                  --------------------------------
                  |                              |
                  |                              |
+----------------------------+     +----------------------------+
|   IndividualCustomer       |     |   CommercialCustomer       |
+----------------------------+     +----------------------------+
|                            |     | - company_name             |
+----------------------------+     +----------------------------+
| + get_customer_category()  |     | + get_customer_category()  |
+----------------------------+     +----------------------------+


                         1
                         |
                         |
                         | owns
                         |
                         *
                 +----------------+
                 |    Vehicle     |
                 +----------------+
                 | - make         |
                 | - model        |
                 | - year         |
                 | - color        |
                 | - mileage      |
                 | - VIN          |
                 | - license_plate|
                 | - usage_type   |
                 | - repair_history|
                 +----------------+
                 | + add_repair_order() |
                 | + get_repair_history()|
                 +----------------+
                         |
                         |
                         *
                 +----------------+
                 | RepairOrder    |
                 +----------------+
                 | - order_number |
                 | - status       |
                 | - timestamps   |
                 | - repair_lines |
                 +----------------+
                 | + complete_repair() |
                 | + get_status()      |
                 +----------------+
                         |
                         |
                         *
                 +----------------+
                 |  RepairLine    |
                 +----------------+
                 | - description  |
                 +----------------+



+----------------+
| Appointment    |
+----------------+
| - appointment_id|
| - date          |
| - concern       |
| - status        |
+----------------+
| + check_in()    |
| + cancel()      |
+----------------+
        |
        |
        | connects
        |
Customer + Vehicle



+----------------------+
|   ServiceAdvisor     |
+----------------------+
| - advisor_id         |
| - name               |
| - last_name          |
+----------------------+
| + check_in_vehicle() |
| + add_repair_line()  |
| + create_repair_order()|
+----------------------+
            |
            |
            | creates
            |
            v

       +----------------+
       | RepairOrder    |
       +----------------+



+-----------------------------+
|          Workshop           |
+-----------------------------+
| - customers{}               |
| - vehicles{}                |
| - repair_orders{}           |
| - registered_emails{}       |
| - registered_plates{}       |
+-----------------------------+
| + register_customer()       |
| + register_vehicle()        |
| + register_repair_order()   |
| + find_customer()           |
| + find_vehicle()            |
+-----------------------------+
