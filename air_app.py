#THE BUNDLE MENU

#send money
# ---
#account
#-- check balance --- >> kutapa balance -- airtime --> airmoney -->
# my pin --->> change pin
# make payments-- escom -- water -- gotv
# bundles -->>
# deposit -->>
# withdrawel -->>




account_info={
  "balance":0,
  "air_time":0,
  "pin":"",
  "loan":0,
  "has_already_borrowed":False
}

def Kutapa():

  print("1.k 100 with interest: k 20")
  print("2.k 500 with interest: k 100")
  print("3.k 1000 with interest: k 200")
  print("4.k 2000 with interest: k 400")
  print("00.Previous menu")
  print("<<---------------------------------->>")

  while True:
    option=input("Choose from 1-4")

    if option == "1" and not account_info["has_already_borrowed"]:

       account_info["has_already_borrowed"]=True
       account_info["air_time"]=account_info["air_time"]+100
       account_info["loan"]=120
       print(f"\n Current airtime balance :k {account_info['air_time'] }")
       print(f"\n Current kutapa balance :k 120")

    elif option == "2"and not account_info["has_already_borrowed"]:
       account_info["has_already_borrowed"]=True
       account_info["air_time"]=account_info["air_time"]+500
       account_info["loan"]=600

       print(f"\n Current airtime balance :k {account_info['air_time']}")
       print(f"\n Current kutapa balance :k 600")

    elif option == "3" and not account_info["has_already_borrowed"]:
       account_info["has_already_borrowed"]=True
       account_info["air_time"]=account_info["air_time"]+1000
       account_info["loan"]=1200

       print(f"\n Current airtime balance :k {account_info['air_time']}")
       print(f"\n Current kutapa balance :k 1200")

    elif option == "4" and not account_info["has_already_borrowed"]:
       account_info["has_already_borrowed"]=True
       account_info["air_time"]=account_info["air_time"]+2000
       account_info["loan"]=2400

       print(f"\n Current airtime balance :k {account_info['air_time']}")
       print(f"\n Current kutapa balance :k 2400")

    elif option == "00":
          break

    else:
       print("Please Enter a valid choice")







def withDrawel ():
  print("Please withdrawel amount that is greater than 100")
  if account_info["balance"]:
   try:
      agnet_code=int(input("Enter the Agent code: "))
      amount=int(input("Enter amount to withdrawel: "))

      if account_info["balance"] >= amount and amount >= 100:
        varification=input("Enter pin to continue: ")
        if varification == account_info["pin"]:

           sent=20/100*amount
           print(f"You have withdrawel {amount-sent} and 20% cut")
           account_info["balance"]=amount-sent
           print(f"\nTransiaction successful.You sent K {amount} to {agnet_code}. Current balance :k {account_info['balance']-sent}")
      else:
        print("Not enough funds. Transaction failed")
   except :
       print("Error please abid by the rules")


def deposit():
  print("Deposit must be greater than k_80 ")
  try:
     deposit=int(input("Enter amount to deposit: "))
     if deposit >= 80:
       account_info["balance"]=deposit
       print(f"\nTransiaction successful.You recieved k {deposit}. Current balance :k {account_info['balance']}")

  except :
     print("Error please abid by the rules")

def check_balance():

  print(f"Active Airtime {account_info['air_time']}")
  print(f"Current Money avalable {account_info['balance']}")
  if account_info["has_already_borrowed"]:
    print(f"Current kutapa balance k{account_info['loan']}")

def bundle_inventory():
  choice=input("1.Buy bundles 2.Buy Airtime: ")
  while True:
   if choice == "1":



           print("\n1.Daliy 1GB :k 1000")
           print("\n2.weekly 2GB :k 1500")
           print("\n3.weekly 5GB :k 5000")
           print("\n4.monthly 20GB :k 20000")

           print("\n<<---------bundle package------------->>")

           bundle_choice=input("Enter bundle option from (1-4): ")

#______________________________________________________
           if bundle_choice == "1":
                payment=input("1.Pay using Airtel money 2.Pay using Airtime: ")

                if payment == "1":
                  varification=input("Enter your pin to continue: ")
                  if varification == account_info["pin"] and account_info["pin"]:
                    if account_info["balance"] >= 1000 :
                       account_info["balance"]-=1000
                       print(f"\nTransiaction successful. Current balance :k {account_info['balance']}")
                       print(f"\nDaily 1GB bundle purchased successfully")
                    else:
                      print("\nTransiaction Falied. Insufficient Funds")
                  else:
                    print("Wrong pin")

                elif payment == "2":
                  if account_info["air_time"] >= 1000 :
                    account_info["air_time"]-= 1000

                    print(f"\nDaily 1GB bundle purchased successfully")
                  else:
                    print("Not enough airtime. please borrow using kutapa")


#______________________________________________________

           elif bundle_choice == "2":

                payment=input("1.Pay using Airtel money 2.Pay using Airtime: ")

                if payment == "1":
                  varification=input("Enter your pin to continue: ")
                  if varification == account_info["pin"] and account_info["pin"]:
                    if account_info["balance"] >= 1500 :
                       account_info["balance"] -= 1500
                       print(f"\nTransiaction successful. Current balance :k {account_info['balance']}")
                       print(f"\nWeekly 2GB bundle purchased successfully")

                    else:
                      print("\nNot enough airtime. please borrow using kutapa")
                  else:
                    print("\nWrong pin")


                elif payment == "2":
                  if account_info["air_time"] >= 1500 :
                    account_info["air_time"]-=1500
                    print(f"\nCurrent airtime balance :k {account_info['air_time']}")
                    print(f"\nWeekly 2GB bundle purchased successfully")

                  else:
                     print("\nNot enough airtime or money. please borrow using kutapa")

#______________________________________________________
           elif bundle_choice == "3":
               payment=input("1.Pay using Airtel money 2.Pay using Airtime: ")

               if payment == "1":
                 varification=input("Enter your pin to continue: ")
                 if varification == account_info["pin"] and account_info["pin"]:
                   if account_info["balance"] >= 5000:
                      account_info["balance"] -= 5000
                      print(f"\nTransiaction successful. Current balance :k {account_info['balance']}")
                      print(f"\nWeekly 5GB bundle purchased successfully")

                 else:
                   print("Wrong pin")


               elif payment == "2":
                   if account_info["air_time"] >= "3":
                     account_info["air_time"] -= 5000
                     print(f"\nCurrent airtime balance :k {account_info['air_time']}")
                     print(f"\nWeekly 5GB bundle purchased successfully")

                   else:
                     print("\nNot enough airtime or money. please borrow using kutapa")


#______________________________________________________
           elif bundle_choice == "4":
             payment=input("\n1.Pay using Airtel money 2.Pay using Airtime: ")
             if payment == "1":
                varification=input("\nEnter your pin to continue: ")
                if varification == account_info["pin"] and account_info["pin"]:
                   if account_info["balance"] >= 20000:
                      account_info["balance"] -= 20000
                      print(f"\nTransiaction successful. Current balance :k {account_info['balance']}")
                      print(f"\nWeekly 20GB bundle purchased successfully")

                else:
                    print("Wrong pin")

             elif payment == "2":
                   if account_info["air_time"] >= 20000:
                     account_info["air_time"]-=20000
                     print(f"\nCurrent airtime balance :k {account_info['air_time']}")
                     print(f"\nWeekly 20GB bundle purchased successfully")

                   else:
                     print("Not enough airtime or money. please borrow using kutapa")


#______  ______________________________________________






   elif choice == "2":
     attempts=0


     amount_of_airtime=int(input("Amount of Airtime: "))
     if amount_of_airtime > 20 :

               varification=input("Enter your pin to confirm purchuse: ")
               attempts +=1

               if varification == account_info["pin"]:

                    account_info["air_time"]+=amount_of_airtime
                    print("\npurchuse successful.")

                    if account_info["has_already_borrowed"]:
                       account_info["air_time"]-=account_info["loan"]

                       if account_info["loan"] == 0:
                          account_info["has_already_borrowed"]=False
                          print("\nYour Kutapa balance is no more")

                       else:
                         print("Your Kutapa is still pending")


def my_pin () :
  print("1.myPin")
  print("2.Change pin")
  print("<<-------------------->>")
  tries=0
  choice = input("Enter choice: ")
  isOk=True
  if choice == "2":
    while tries < 4 and isOk :
      if account_info["pin"] :
         current_pin = input("Enter your current pin: ")
         if current_pin == account_info["pin"]:
             new_pin=input("Enter new pin: ")
             account_info["pin"]=new_pin
             print("Pin changed sussefully")
             break
         else:
             print("Incorrect pin.")
      else:
          new_pin=input("Create pin: ")
          account_info["pin"]=new_pin
          print("Pin created succesfully")
          break

      tries +=1
  if choice == "1":
    if account_info["pin"]:
     print(f"\nYour pin is {account_info['pin']}")
    else:
      print("\nYou don't have pin create one.")
  elif tries == 4:
     print("Account blocked")
     isOk=False

def send_money ():
  reciepient=input("Reciepient Number: ")
  if account_info["balance"] > 0:
    amount=int(input("Enter amount to send: "))
    if amount >= account_info["balance"]:
       account_info["balance"]=account_info["balance"]-amount
       print(f"\nTransiaction successful.You sent k {amount} to {reciepient}  Current balance :k {account_info['balance']}")
    else:
      print("\nNot enough funds")
  else:
     print("\nYou account is very low to run transaction")

def my_airtel_app():
  print("you have received 200MB free")


while True:
  code=input("Enter USSD code: ")
  if code == "*211#":
    print("\n1.Buy Bundle")
    print("\n2.myPin")
    print("\n3.Kutapa")
    print("\n4.Check Balance")
    print("\n5.Send money")
    print("\n6.WithDrawel")
    print("\n 7.Deposit")
    print("\n 8.Downlaod myAirtel app(200 mb free) ")
    print("\n00. Exit")
    print("\n<<------------menu--------------->>")
    menu=input("Choose from the menu 1-8 : ")

    if menu == "1":
      print(bundle_inventory())
    elif menu == "2":
      print(my_pin())
    elif menu == "3":
      print(Kutapa())
    elif menu == "4":
      print(check_balance())
    elif menu == "5":
      print(send_money())
    elif menu == "6":
      print(withDrawel())
    elif menu == "7":
      print(deposit())
    elif menu == "8":
      print(my_airtel_app())
    elif menu == "00":
      break
    else:
      print("Choose the correct menu")
  else:
    print("USSD code ERROR!!")
