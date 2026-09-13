
from inside_menu.employees import employees_menu
from inside_menu.membership import membership_plan
from inside_menu.customers import adding_customer, view_customer
from inside_menu.services import services

def menu():
    while True:
     
     print("GYM - Tracker")
     input("press any key to get into the GYM tracker:")

     print("=" * 35)
     print("        MENU OF GYM _TRACKER            ")
     print("=" * 35)
     print("| 1.      MEMBERSHIP               | ")
     print("| 2.      EMPLOYEES                | ")
     print("| 3.      VIEW CUSTOMERS           | ")
     print("| 4.      ADD CUSTOMERS            | ")
     print("| 5.      SERVICES                 | ")
     print("| 6.      EXIT                     | ")

     option = input("choose the number you want to go to:")
     if option == "1":
        membership_plan()
     elif option == "2":
        employees_menu()
     elif option == "3":
        view_customer()  
     elif option == "4":
        adding_customer() 
     elif option == "5":
        services()          
     elif option == "6":
        print("Thank you for using gym tracker...")   
        break
     else:
        print("invalid number")

      
       

menu()
