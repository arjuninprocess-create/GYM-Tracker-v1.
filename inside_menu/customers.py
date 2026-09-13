import json

def adding_customer():
    customer_id = input("create an ID:")
    name = input("Add the Customers full name:")
    age = input("Add the Age of the customer:")
    membership = input("Which membership the Customer prefers?:")

    customer= {"ID": customer_id,
                "Name": name,
                "Age": age,
                "Membership": membership}
    with open("customer.json", "r") as file:
        customers = json.load(file)
    customers.append(customer) 
    with open("customer.json", "w") as file:
        json.dump(customers, file, indent=4)
    print("Customer is added to the Gym Tracker!")      

def view_customer():
    with open("customer.json","r") as file:
        customers = json.load(file)
    print("="* 60)
    print(f"{'ID':<5} {'Name':<15} {'Age':<13} {'Membership':<15}")
    print("="* 60)

    for customer in customers:
        print(f"{customer['ID']:<5}"
              f"{customer['Name']:<15}"
              f"{customer['Age']:<13}"
              f"{customer['Membership']:<15}")    
    print("="* 60)
