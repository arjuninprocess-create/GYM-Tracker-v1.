
from inside_menu.employees import employees_menu
from inside_menu.membership import membership_plan



def menu():
    while True:
     
     print("GYM - Tracker")
     input("press any key to get into the GYM tracker:")

     print("=" * 35)
     print("        MENU OF GYM _TRACKER            ")
     print("=" * 35)
     print("| 1.      MEMBERSHIP               | ")
     print("| 2.      EMPLOYEES                | ")
     print("| 3.      EQUIPMENTS               | ")
     print("| 4.      SERVICES                 | ")
     print("| 5.      CUSTOMERS                | ")
     print("| 6.      EXIT                     | ")

     option = input("choose the number you want to go to:")
     if option == "1":
        membership_plan()
     elif option == "2":
        employees_menu()
     elif option == "6":
        print("Thank you for using gym tracker...")   
        break
     else:
        print("invalid number")

      
       

menu()
