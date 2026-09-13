#there will be 4 member ship plan and those plans will be linked to the members or the customres


def membership_plan():
    plans = {"Regular": "15 Euro/month\n"
                        "Access: Gym equipment, Locker room, gym access",
             "Plus": "20 Euro/month\n"
                     "Access: Regular membership + Sauna + Group coaching",
             "Premium": "28 Euro/month\n"
                        "Access: Plus membership + Personal Trainer + Nutrition Guide",
             "Elite": "56 Euro/month\n"
                      "Access: Premium membership + Exclusice Gym area Access"}
   
   
    while True:
        print("-"* 22)
        print("|  Membership plans  |")
        print("-"* 22)
        print("|1. Regular          |")
        print("-"* 22)
        print("|2. Plus             |")
        print("-"* 22)
        print("|3. Premium          |")
        print("-"* 22)
        print("|4. Elite            |")
        print("-"* 22)
        print("|5. EXIT             |")
        print("-"* 22)
        choose = input("number you are planing to enter:")

        if choose == "1":
            print(plans["Regular"])
            input("\nPress Enter to continue...")
        elif choose == "2":
            print(plans["Plus"])
            input("\nPress Enter to continue...")
        elif choose == "3":
            print(plans["Premium"])
            input("\nPress Enter to continue...")
        elif choose == "4":
            print(plans["Elite"])
            input("\nPress Enter to continue...")
        elif choose == "5":
            return
        else:
            print("invalid value")
            
                    
