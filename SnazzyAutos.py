print ("Are you interested to buy a car?")
while True:
    try:
        buy = int(input("Type 1 for 'Yes' and Type 2 for 'No': "))
        if buy == 1 or buy == 2:
            break
        else:
            print("Wrong Choice Entered. Enter again!")
    except ValueError:
        print("Invalid input. Please enter a number.")


# user decides to buy a car
if (buy==1):
    print("\n---------------------------------------------------")
    print ("WELCOME TO SNAZZY AUTOS")
    print("---------------------------------------------------\n")
    print("Which car model are you interested to buy?")
    print('''
                MODEL         PRICE
            1. Hatchback    Rs. 5.35 lakh
            2. Saloon       Rs. 4.95 lakh
            3. Estate       rs. 6.25 lakh
    ''') 
    while(True): 
        try:
            car = int(input("Type 1 for 'Hatchback', 2 for 'Saloon' and 3 for 'Estate'"))
            if car==1 or car==2 or car==3: break
            else: print("Wrong Choice Entered. Enter again!")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("\n---------------------------------------------------\n")
    print("Which add-on feature are  you interested to use?")
    print(''' 
            OPTIONAL EXTRA           PRICE
        1. Set of Luxury Seats      Rs 45000
        2. Satellite Navigation     Rs 5500
        3. Parking Sensors          Rs 10000
        4. Bluetooth Connectivity   Rs 350
        5. Sound System             Rs 1000
          ''')
    while(True):
        try:
            print('''
                Type 1 for 'Luxury Seats', 2 for 'Satellite Navigation', 3 for 'Parking Sensors', 
                4 for 'Bluetooth Connectivity', 5 for 'Sound System' and 6 for 'None' ''')
            add_on = int(input())
            if add_on>=1 or add_on<=6 : break
            else: print("Wrong Choice Entered. Enter again!")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Existing Member
    print("\n---------------------------------------------------\n")
    print("Are you an Existing Member?")
    while(True):
        try:
            exmem = int(input("Type 1 for: Yes(Eligible for 10% Discount) and 2 for: No(Eligible for 5% Discount)"))
            if exmem==1 or exmem==2: break
            else: print("Wrong Choice Entered. Enter again!")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Old Car Excahnge 
    print("\n---------------------------------------------------\n")
    print("Do you have an old car for exchange?")
    while(True):
        try:
            excar = int(input("Type 1 for: Yes and 2 for: No"))
            if excar==1 or excar==2: break
            else: print("Wrong Choice Entered. Enter again!")
        except ValueError:
            print("Invalid input. Please enter a number.")
#Old Car Price
    if excar==1:
        print("Enter the value of old car: ")
        print("Note: 'The value of car evaluated after depriciation lies in the range of Rs 10000 to Rs 100000")
        while(True):
            try:
                ocprice=int(input())
                if 10000<=ocprice<=100000: break
                else: print("Car price is wrongly evaluated. Enter Again!")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    print("\n---------------------------------------------------\n")
    print("Kindly enter your payment option: ")
    print('''
            Type 1 for 'Full Amount at 1% cashback or chosen optional add-ons free'
            Type 2 for 'Equal Monthly payments for four years at no charge'
            Type 3 for 'Equal Monthly payments for seven year at interest of 5% on total price of car'
    ''') 
    while(True): 
        try:
            payop = int(input())
            if payop==1 or payop==2 or payop==3: break
            else: print("Wrong Choice Entered. Enter again!")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Finalising the car model selected and its price
    if car==1: 
        fmodel="Hatchback" 
        fprice= 535000
    elif car==2: 
        fmodel="Saloon" 
        fprice= 495000
    else: 
        fmodel="Estate" 
        fprice= 625000

    if add_on == 6:
        faprice=0 
        
        print("The model of the car is '",fmodel,"',worth Rs ",fprice," with no addon feature.")

#Finalising the car addon selected and its price     
    
    else:
        if add_on==1:
            faddon="Set of Luxury Seats"
            faprice=45000
        elif add_on==2:
            faddon="Satellite Navigation"
            faprice=5500
        elif add_on==3:
            faddon="Parking Sensors"
            faprice=10000
        elif add_on==4:
            faddon="Bluetooth Connectivity"
            faprice=350
        elif add_on==5:
            faddon="Sound System"
            faprice=1000
    print("\n---------------------------------------------------")
    print("Final Pricing")
    print("---------------------------------------------------\n")
    if add_on==6: 
        print("\nThe model of the car is '",fmodel,"',worth Rs",fprice,".")
    else:
        print("\nThe model of the car is '",fmodel,"',worth Rs",fprice," with add-on feature of '",faddon,"',worth Rs",faprice)



    #FINAL PRICE
    fpay = fprice+faprice

    #Checking Membership
    if exmem==1:
        #10% Discount
        fpay -= (0.1*fpay)
        print("\n(The discount is of 10% Discount as you are an Old Customer)") 
        
    elif exmem==2: 
        #5% Discount
        fpay -= (0.05*fpay)
        print("\n(The discount is of 5% Discount as you are a New Customer)") 
    
    if excar==1: 
        print("\nThe evaluated value of your old car is",ocprice)
    else:
        ocprice=0
    
    fpay -= ocprice
    print("The total price of the car is ",fpay)

    #Payment
    if payop==1:
        if add_on==6:
            print("No add-ons chosen")
            cback = 0.01*fpay
            npay = fpay-cback
            print("Net Amount to be paid is Rs",npay)

        else:
            pmode="Full Amount at 1% cashback or chosen optional add-ons free"
        
            print("\nThe option of method chosen is '",pmode,"'.")
            #Net Price
            cback = 0.01*fpay
            np1=fpay-cback
            np2=fpay-faprice

            if np1<np2: 
                print("\nThe best value obtained when 1% cashback is chosen. Rs",np1,".")
                print("The alternative value obtained when free add-ons is chosen. Rs",np2,".")
            elif np1>np2:
                print("\nThe best value obtained when free add-ons is chosen. Rs",np2,".")
                print("The alternative value obtained when 1% cashback is chosen. Rs",np1,".")
            else:
                print("\Both values are same i.e., any option can be chosen. Rs",np1)

            print("\nKindly enter the value you choose: ")
            while(True): 
                fchose = int(input("Type 1 for 1% cashback is chosen and 2 for free add-ons"))
                if fchose==1 or fchose==2: break
                else: print("Wrong Choice Entered. Enter again!")
            
            if (fchose==1): 
                cback = 0.01*fpay
                npay=np1
                print("Net Amount to be paid is Rs",npay)
            elif (fchose==2) or (fchose==3):
                cback = 0
                npay=np2
                print("Net Amount to be paid is Rs",npay)
        

    elif payop==2:
        pmode="Equal Monthly payments for four years at no charge"
        npay=fpay
        print("\nThe option of method chosen is '",pmode,"'.")
        #Net Price
        print("Net Amount to be paid is Rs ",npay)
        print("\nNumber of installments(in months) and amount of each installment is 48 months Rs ",npay/48," respectively.")
        cback=0


    elif payop==3:
        pmode="Equal Monthly payments for seven year at interest of 5% on total price of car"
        npay = fpay+(0.05*fpay)
        print("\nThe option of method chosen is '",pmode,"'.")
        #Net Price
        print("Net Amount to be paid is Rs ",npay)
        print("\nNumber of installments(in months) and amount of each installment is 84 months Rs ",npay/84," respectively.")
        cback=0

    print("\nThe amount of cashback is ",cback)
    print("\n---------------------------------------------------")
    print("\nThank You For Your Time!")
    print("---------------------------------------------------\n")

# user doesn't want to buy a car
else: 
    print("Thank You for Visiting")