from car import Car
from services import Service, Invoice

def main():

    print("My Car App")

    # car object #1
    toyota_supra = Car('red', 'toyota', 'supra', 'YYYY')
    print(toyota_supra.color, toyota_supra.brand, toyota_supra.model)

    # car object #2
    ford_f150 = Car('black', 'ford', 'F150', 'XXXX')
    print(ford_f150.color, ford_f150.brand, ford_f150.model)

    # service object #1
    tire_rotation = Service(
        name='tire_rotation',
        service_type='quicklube',
        price=50,
        service_time=15
    )

    # service object #2
    oil_change = Service(
        name='oil_change',
        service_type='quicklube',
        price=70,
        service_time=20
    )

    # each car, take an action
    print(toyota_supra.accelerate())
    print(toyota_supra.brake())

    # invoice #1
    invoice_supra = Invoice(toyota_supra, oil_change, '787-787-7878')
    print(invoice_supra.print_invoice())

    # invoice #2
    invoice_f150 = Invoice(ford_f150, tire_rotation, '939-939-9393')
    print(invoice_f150.print_invoice())

    return


if __name__ == "__main__":
    main()