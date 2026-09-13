# GYM Tracker v1

A Python-based Gym Management System that manages memberships, employees, customers, and gym services.

## Features

- Membership Plan Management
- Employee Information System
- Customer Management
- Service Catalog
- JSON Data Storage
- Menu-Driven Interface

## Installation

1. Clone the repository:

```bash
git clone https://github.com/arjuninprocess-create/GYM-Tracker.git
```

2. Navigate to the project folder:

```bash
cd GYM-Tracker
```

3. Run the application:

```bash
python3 Main.py
```

## Example Usage

```text
GYM - Tracker

1. Membership
2. Employees
3. Customers
4. Services
5. Exit

Choose the number you want to go to: 3
```

Adding a Customer:

```text
Create an ID: 1
Add the Customer's full name: Arjun
Add the Age of the customer: 20
Which membership the Customer prefers?: Premium

Customer is added to the Gym Tracker!
```

Viewing Customers:

```text
============================================================
ID   Name           Age          Membership
============================================================
1    Arjun          20           Premium
============================================================
```

## Key Features

### Membership Management
- Regular Plan
- Plus Plan
- Premium Plan
- Elite Plan

### Employee Management
- Managers
- Trainers
- Cleaners
- Massage Therapists

### Customer Management
- Add Customer
- View Customer
- JSON Data Storage

### Services
- Sauna
- Cold Plunge
- Massage Therapy
- Nutrition Guide

## Project Structure

```text
GYM-Tracker/
│
├── Main.py
├── customer.json
│
├── inside_menu/
│   ├── membership.py
│   ├── employees.py
│   ├── customers.py
│   └── services.py
│
├── .gitignore
└── README.md
```

## Files Description

### Main.py
Controls navigation throughout the application.

### membership.py
Displays membership plans and benefits.

### employees.py
Stores employee categories and profile information.

### customers.py
Handles customer creation, storage, and viewing.

### services.py
Displays the service catalog.

### customer.json
Stores customer records permanently.

## Future Improvements

- Equipment Management
- Search Customer by ID
- Delete Customer
- Update Customer Membership
- Membership Statistics Dashboard
- Payment Tracking

## Author

Arjun Kareparambil Sunil
