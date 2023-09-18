#Imports the method Random so that I may use it in my code.
import random
from typing import List
#Takes the input on which chatbot the user would like to use, and only accepts integers.
chatbot=int(input("Which chatbot would you like to use?(1,2, or 3)? "))
#A list a random responses each chatbot will use if the given questions aren't met.
randomAnswerList=["I see.","Oh!","Uh huh","Now that is interesting.","I didn't know.","Ok"]

##Office chatbot
#If the Chatbot input equal 1, the code for the office chatbot is initiated.
if(chatbot==1):
  print("Welcome to Rob's Financial Institution chatbot, how may I be of service.")
  #A list of all the customers that are present at the financial institution.
  customerList=[]
  #A list of all the accounts each customer has.
  accountList=[]
  #A list of the money in each account.
  accountBalanceList=[]
  #A list of all the products the office sells.
  officeProducts=["Staplers","Scotch Tape","2pack of 20 #2 Pencils"]
  #A list of the prices of each product.
  officeProductPrices=[1.99,1.25,3.99]
  #A list of all the services the office provides.
  officeServices=["Banking","Insurance","Financial Advisory","Mutual Funds","Wealth Management","Checking Accounts","Debit Cards","Credit Cards",]
  #Continuously loops the code until a condition is met to break the loop.
  while True:
    #Allows the user to ask any question they want.
    customerResponse=input("")
    #Creates an account for a customer at the store as long as the account doesn;t already exist. Then it allows the customer to add money to the account.
    #Takes in the list of customers, the list of that customer's accounts, and the list of balances for each account.
    def createAccount(customerList,accountBalanceList,accountList):
      customerName=input("What name is the account under?")
      #If the customer name isn't in the customer list, it adds their name to the customer list and the account list.
      if(customerName not in customerList):
        #adds the customer name to the customer list and the account list
        customerList.append(customerName)
        accountList.append(customerName)
        #If the account list isn't in the customer list, It adds the accountlist to the customer list.
        if(accountList not in customerList):
          customerList.append(accountList)
      accountName=input("What is the name of your account?")
      #If the account name is intheaccount list, it recalls the method, forcing the user to start over
      if(accountName in accountList):
        print("You already have an account under that name")
        createAccount(customerList,accountBalanceList,accountList)
      #Else, the account list is added and it checks for how much money is added to the account and adds that to the balance List
      else:
        accountList.append(accountName)
        addedMoney=float(input("How much money will you be adding?"))
        accountBalanceList.append(addedMoney)
        #loops through the account list and looks for the account name.
        for i, name in enumerate(accountList):
          #If the account name is in the aaccount list, it adds the amount of money stated above to the balance list for that account. Then prints the result.
          if (name==accountName):
            accountAmount=accountBalanceList[(i-1)]
            print(f"Your account {accountList[i]} has been created {accountList[0]}")
            print(f"Your balance is {accountAmount}")
    #A method that removes money of the amount the user requests. Has a paramater of the current balance. 
    def withdraw(balance):
      removeMoney=float(input("How much money would you like to withdraw?"))
      #If the user doesn't enter an integer or float or if the number they enterd is more than the balance, the method is called again.
      if(removeMoney>balance or not float(removeMoney) or not int(removeMoney)):
        print("That is not an acceptable value")
        withdraw(balance)
      #Else,add money to the balance and return the new balance.
      else:
        balance-=removeMoney
        return balance
    #A method that adds money to an account, and has the paramaters of the balance of that account.
    def deposit(balance):
      addMoney=float(input("How much money would you like to add?"))
      #If the user doesn't enter an integer or float, the method is called again.
      if(not float(addMoney) or not int(addMoney)):
        print("That is not an acceptable value")
        deposit(balance)
      #Else,add money to the balance and return the new balance.
      else:
        balance+=addMoney
        return balance  
    #A method that finds the customers account, and causes different actions depening on what they requested.
    #Takes in the paramaters of the customer list, the balance list and the requested change
    def findAccount(customerList,balanceList,change):
      findingCustomerName=input("What name is the account under?")
      #If the requested customer isn't in the customer list, the method is recalled. 
      if(findingCustomerName not in customerList):
        print("There doesn't seem to be an account under that name")
        findAccount(customerList,balanceList,change)
      #Else, the method loops through the customers in the customer list.
      else:
        for i,accounts in enumerate(customerList):
          #If the customer in the customer list is the same as the inputed customer name, then the listof that persons accounts are pulled up from the customer list.
          if accounts==findingCustomerName:
            currentAccountList=customerList[i+1]
            #Allowsthe userto input hich account they wantto find.
            findAccountName=input("What's the name of the account? ")
            #If the requested account name isn't in the account list, the method is recalled.
            if(findAccountName not in currentAccountList):
              print("I'm sorry that's not in my databse, you'll have to start over.")
              findAccount(customerList,balanceList,change)
            #Else, loops through the names of the accounts in the account list.
            else:
              for a, names in enumerate(currentAccountList):
                #If the name of the account is the same as the requested account, sets the balance as the balanceof that account at thatinterval in the price list.  
                if(names==findAccountName):
                  balance=balanceList[a-1]
                  #Else,if the change equals "subtract". Addsmoney to the account
                  if(change=="subtract"):
                    #Calls the withraw function,taking in the current balance. The account loses money of the user's choosing, updates and prints the new total.
                    balance=withdraw(balance)
                    balanceList[a-1]=balance
                    print(f"Your new balance is {balance}")
                  #Else,if the change equals "add". Addsmoney to the account
                  elif(change=="add"):
                    #Calls the deposit function,taking in the current balance. The account gains money of the user's choosing, updates and prints the new total.
                    balance=deposit(balance)
                    balanceList[a-1]=balance
                    print(f"Your new balance is {balance}")
                  #Else,if the change equals "Transfer". Transfers the money from the first accoun into a new account through user input.
                  elif(change=="Transfer"):
                    transferAccount=input("What account will you transfer into? ")
                    #While the account the user is transfering into isn't in the account list, the code loops until it is an account in that list..
                    while(transferAccount not in currentAccountList):
                      print("That's not an option")
                      transferAccount=input("What account will you transfer into? ")
                    #Loop through all the accounts in the account list.
                    for x, accounts in enumerate(currentAccountList):
                      #If the account in the account list is the account the user wants to transfer from. It removes money fromone account and adds it to this account.
                      if(accounts==transferAccount):
                        #Takes the balance of this account and depositsthe balance from the old account into it, then updates the new balance.
                        newBalance=balanceList[x-1]
                        newBalance=deposit(balance)
                        balanceList[x-1]=newBalance
                        #Takes the previose account and allows the user to withdraw money from that account.  Then it updates the old account and prints the balance of the new account.
                        balance=withdraw(balance)
                        balanceList[a-1]=balance
                        print(f"Your transfer is complete., your account now read ${newBalance}")
                  #Else, the current balance is returned
                  else:
                    return(balance)
    #If the customer says "Stop", the loop breaks and the chatbot ends.
    if (customerResponse=="Stop"):
      print("Have a Nice day")
      break
    #Else, if the customer requests to create an account. Then, it calls the createAccount method.
    elif(customerResponse=="I'd like to create an account"):
      #Takes in the customer list, the account balance list, and the account list.
      createAccount(customerList,accountBalanceList,accountList)
    #Else, if the user requests to check their account balance. Then the findAccount function is called with the change being "0".
    elif(customerResponse=="I'd like to check my account balance"):
      #Takes in the paramaters of the customer list, the account balance list, and no change.
      balance=findAccount(customerList,accountBalanceList,"0")
      print(f"Your balance is {balance}")
    #Else, if the user requests to remove money from an account. Then the findAccount function is called with the change being "subtract".
    elif(customerResponse=="I'd like to make a withdrawl"):
      change="subtract"
       #Takes in the paramaters of the customer list, the account balance list, and the change of "subtract".
      findAccount(customerList,accountBalanceList,change)
    #Else, if the user requests to add money to an account. Then the findAccount function is called with the change being "add".
    elif(customerResponse=="I'd like to make a deposit"):
      change="add"
      #Takes in the paramaters of the customer list, the account balance list, and the change of "add".
      findAccount(customerList,accountBalanceList,change)
      #Else, if the user requests to transfer money. Then the findAccount function is called with the change being "Transfer".
    elif(customerResponse=="I'd like to transfer money between my accounts"):
      change="Transfer"
      #Takes in the paramaters of the customer list, the account balance list, and the change of "Transfer".
      findAccount(customerList,accountBalanceList,change)
    #Else, if the customer asks what the service are. Then the code loops through the services the the office products list and their prices from the price list, and then prints them out.
    elif(customerResponse=="What are your available products?"):
      for p, product in enumerate(officeProducts):
        print(f"{product} ${officeProductPrices[p]}")
    #Else, if the customer asks what the service are. Then the code loops through the services the the office services list, and prints them out.
    elif(customerResponse=="What are your services?"):
      print("Our services include:")
      for service in officeServices:
        print(f"-{service}")
    else:
      #If the question isn't one of the questions listed above, then the computer will print a random response from the response list.  
      print(randomAnswerList[random.randint(0,4)])
    print("")


#If the userinputs a 3, it loads the retail store chatbot.     
#Retail store chatbot
if(chatbot==3):
  print("Welcome to Richards Retail Store chatbot, What is your question?")
  #Defines a list of responses the chatbot may publish for different questions.
  retailAnwerList=["I'm sorry, I don't know that one.","I believe you may have the wrong department.","Hm, that question isn't in my database. \nCould you have mispelled it?","I'm sorry to hear that, I'll get someone on that right away."]
  #Defines a list of locations the retail store could be at.
  retailPlaceList=["3333, Weiss Lane","3654, History Drive","1897, Undead Avenue"]
  #Loops the code infinitely until the user says stop.
  while True:
    #Allows the user to input whatever they want.
    help=input("")
    #If the user inputs "Stop", the loop breaks and the chatbot stops.
    if(help=="Stop"):
      print("Have a nice day.")
      break          
    #Else, if the user asks for the store inventory. Then, a long print staatement will print the inventory. 
    elif(help=="What's in your store inventory?"):
      print("Our current inventory consists of:")
      print("1 Stapler: $12\n1 Stack of 64 sheets of paper: $2.50\n1 HZP CopyPrinter: $25.99\n3 Pack of 135 staple refil: $5.75")
    #Else if the user asks where the store is located, then the program chooses a random location from the location list and prints it out.
    elif (help=="Where's your store located?"):
      randomPlace=retailPlaceList[random.randint(0,2)]
      print(f"Our nearest store is located on {randomPlace}.")
    #Else, if the user asks what the stores hours are. Then a long print statement of the store hurs.
    elif(help=="What are your store hours?"):
        print("Our store hours are\nMonday-Friday: 8:00AM-9:00PM\nSaturday & Sunday: 9:00AM-8:00PM")
    #Else if the user inputs anything ending with a question mark, it answers with a random answer from the retail answer list.
    elif(help.endswith("?")):
      print(retailAnwerList[random.randint(0,3)])
    else:
      #If the question isn't one of the questions listed above, then the computer will print a random response from the response list.  
      print(randomAnswerList[random.randint(0,4)])
    print("")

    
#If the user input the number 2, it loads up the restaraunt chatbot
#Restaraunt chatbot
if(chatbot==2):
  print("Welcome to Fa-ZA-Ra's Pizzaria chatbot, What is your question? ")
  #The function sets up the users reservation for the restaraunt for AM or PM, and adds their name for the reservation.
  def reservation():
    #I didn't have time to set times for multiple reservations, or reservations at times that aren't at single hour value's. I will create more over time.
    #Time takes the users input for the hour the user wants their reservation to be at.
    time=int(input("What time would you like your reservation to be?"))
    #If the time is in the list for reservations in the AM or PM, then the time is rendered invalid and the function is called again.
    if(time in reservationTimeAM or reservationTimePM):
        print("I'm sorry, that time is already reserved.")
        reservation()
    #Else If the time is over 12 or under 1 then the time is rendered invalid, and the function is called again.
    elif(time>12 or time<1):
      print("I'm sorry that is not an appropriate time.")
      reservation()
    #Finally, if neither statement above is true, the user is then moved to a function to track if the time is in AM or PM.
    else:
      timeFrameSet(time)
  #The function sets up which time frame the persons reservation is put in.
  def timeFrameSet(time):
    timeFrame=input("Is that AM or PM?")
    #If the user inputs AM, they get a reservation in the AM reservation time list, and AM reservation name list.
    if(timeFrame=="AM"):
      reservationTimeAM.append(time)
      name=input("What name will that be under? ")
      reservationNameAM.append(name)
    #Else If the user inputs PM, they get a reservation in  the PM reservation time list, and PM reservation name list.
    elif(timeFrame=="PM"):
      reservationTimePM.append(time)
      name=input("What name will that be under? ")
      reservationNamePM.append(name)
    #If the User didn't enter AM or PM, then their time is invalid, and the function loops over.
    else:
      print("That is not an appropriate time, please try again.\n")
      timeFrameSet(time)
  #Causes the function to loop infinitely. 
  while True:
    help=input("")
    #List for names of people who made a reservation AM.
    reservationNameAM=[]
    #List for names of people who made a reservation PM.
    reservationNamePM=[]
    #List of times for peoples reservation for AM
    reservationTimeAM=[]
    #List of times for peoples reservation for PM
    reservationTimePM=[]
    # If the user enters Stop, the loop break and the chatbot is stopped.
    #List of Meals on sale in the restaraunt.
    restarauntMeal=["XL 16in Pizza","Large 14in Pizza","Medium 12in Pizza","Small 10in Pizza","7in Personal Pizza"]
      #List of Prices for the different Meals
    restarauntPriceMeal=[10.99,8.99,6.99,5.99,4.99]
    #List of Sides on sale in the restaraunt.
    restarauntSide=["2pc Garlic Bread","BreadSticks","Mozzarella Cheesesticks"]
      #List of Prices for the different Sides
    restarauntPriceSide=[2.99,1.50,2.25]
    #List of Drinks on sale in the restaraunt.
    restarauntDrink=["Sprite","Coke","Diet Coke","Fanta","Root Beer","Lemonade","Water","Dr Pepper"]
      #List of Prices for the different Drinks
    restarauntPriceDrink=[0.75,0.99,1.15,1.25,0.50]
    #List of sizes for the drinks
    restarauntDrinkSize=["Small","Medium","Large","XL","Kids"]
    if(help=="Stop"):
      print("Have a nice day.")
      break          
    #If the User asks to make a reservation, the reservation function is called.
    elif(help=="I'd like to make a reservation"):
      reservation()
      print(f"ok, your reservation has been made.")
    #If the user asks to see the menu, the menu will be printed.
    elif(help=="I'd like to see the menu"):
      #Prints the Entree's including it's price by taking the numerical value of the item in the list, and the price at the same numerical value in the price list.
      print("Here is our menu")
      print("\nEntree's:")
      for number,item in enumerate(restarauntMeal):
        item=restarauntMeal[number]
        price=restarauntPriceMeal[number]
        print(f"{item} : ${price}")
      #Prints the Sides, including price. It oes so by looping through the number of items in the restaraunt side list, and prints out the side with the price.
      print("\nSides:")
      for number,item in enumerate(restarauntSide):
        item=restarauntSide[number]
        price=restarauntPriceSide[number]
        print(f"{item} : ${price}")
      #Prints the Drinks, including price.
      print("\nDrinks:")
      #sep found in Sparkbyexampls 
      print(*restarauntDrink, sep=",")
      #Loops through the list of drink sizes, then prints out the drink size, aling with the price of thaat size.
      for number,item in enumerate(restarauntDrinkSize):
        item=restarauntDrinkSize[number]
        price=restarauntPriceDrink[number]
        print(f"{item} : ${price}")
    #Else, if the user requests to place an order. It begins the process of placing an order, and sets the current price to zero
    elif(help=="I'd like to place an order"):
      price=0.0
      #List of the prices of different items
      priceList=[]
      #List of the different items ordered.
      orderList=[]
      #Takes the order for the main course. Paramaters of price, the request input, the list of items, and the list of items price.
      #Adds the subtotal price to the total price
      def orderItem(price,item,itemPrice,orderListToAdd):
        request=input("What would you like to order?")
        #If your request is not in the list of items, calls the function again.
        if(request not in item):
          print("That's not in the menu.")
          orderItem(price,item,itemPrice,orderListToAdd)
        #Else, it takes the price of the item and adds it to the total.
        else:
          #loops through the item list, including the numerical value of each ite in the list.
          for number, items in enumerate(item):
            #If the item is the same as the request, get the price,and add it to the total
            if(items==request):
              subPrice=itemPrice[number]
              price.append(subPrice)
          orderListToAdd.append(request)
      def orderSide(price,item,itemPrice,orderListToAdd):
        request=input("What would you like to order?")
        #If your request is not in the list of items, calls the function again.
        if(request not in item):
          print("That's not in the menu.")
          orderSide(price,item,itemPrice,orderListToAdd)
        #Else, it takes the price of the item and adds it to the total.
        else:
          #loops through the item list, including the numerical value of each ite in the list.
          for number, items in enumerate(item):
            #If the item is the same as the request, get the price,and add it to the total
            if(items==request):
              subPrice=itemPrice[number]
              price.append(subPrice)
          orderListToAdd.append(request)
      #Takes the size order for the users drink, adds price to total. The adds the drink and size to the order list
      
      #Has the User order a drink, then gets the drink size and adds it to the total
      def orderDrink(price,drink,sizeList,drinkPrice,orderList):
        #Establishes a method to set the drink size of the users order.
        #Has parameters of the current price, the list of drink sizes, the list of the prices of the sizes, and the list of orders.
        def orderDrinkSize(price,sizeList,drinkPrice,drink,orderListToAdd):
          size=input("What size drink would you like?")
        #If the drink size isn't in the list, calls the function again. 
          if(size not in sizeList):
            print("That's not an option")
            orderDrinkSize(price,sizeList,drinkPrice,drink,orderListToAdd)
        #Else it loops through the size list until it matches the order, then adds the price to the total and the drink with the size to the total order.
          else:
            #Loops through the different sizes in the size list.
            for value, sizes in enumerate(sizeList):
              #If the size in the size list is the same as the size the user request, The price list gains the drink price of that drink size and prints out the result.
              if(sizes==size):
                subTotal=drinkPrice[value]
                price.append(subTotal)
            #Adds the ordered drink plus the size to the orer list.
            orderedDrink=f"{size} {drink}"
            orderListToAdd.append(orderedDrink)        
        drink_type=input("What drink would you like?")
        #if the the drink you ordered isn't on the menu, it calls the function again.
        if(drink_type not in drink):
          print("That drink's not in our menu")
          #Calls the order Drink Function. It inserts the orderList, current pricelist, the drink size list, and the drink price list.
          orderDrink(price,drink,sizeList,drinkPrice,orderList)
        #Else, it asks for the drink size
        else:
          #Calls the function to order the sizes of the drinks.
          #Takes in the price list, the list of drink sizes, the list of drink prices per size, the current drink you ordered, and the order list.
          orderDrinkSize(price,sizeList,drinkPrice,drink_type,orderList)
      #Loops the code infinitely until the user says "That's All"
      while True:
        userOrder=input("Say Yes to continue ordering(Say That's All to stop) ")
        #If the user inputs "That's All", it breaks the loop and the program moves on.
        if(userOrder=="That's All"):
          #Takes the sum of all the items in the price list, and print out the result.
          #geeksgeeks for sum[float(i) for i in list]
          price=sum([float(i)for i in priceList])
          print(f"Ok, your price is {price}")
          print("\nYour order consists of:")
          #Loops through the items in the ordr list, and prints them out. Then it ends the loop.
          for food in orderList:
            print(food)
          break
        #Else if the user responds "yes to continue ordering, It takes the order f the users main meal, side, and drink."
        elif(userOrder=="Yes"or userOrder=="yes"):
          #Calls the orderItem function to get the users meal order.
          #Takes in the price list, the list of restaraunt meals, the list of prices per meal, and the order list.
          orderItem(priceList,restarauntMeal,restarauntPriceMeal,orderList)
          #Asks theuser if they would like a side.
          sides=input("Would you like to order a side?")
          #If the user says they want a side, it initiates the orderSide function
          if(sides=="Yes"or sides=="yes"):
            #Takes in the parameters of the price list, the restaraunt side list the list of prices per side, and the order list.
            orderSide(priceList,restarauntSide,restarauntPriceSide,orderList)
          #Asks the user if they'd like to order a drink
          drink=input("Would you like to order a drink?")
          #If the user decides they want a drink, the order drink function is called.
          if(drink=="Yes"or drink=="yes"):
            #Takes in the paramaters of the price list, the list of restaraunt drinks, the list of drink sizes, the list of prices per drink size, and the order list. 
            orderDrink(priceList,restarauntDrink,restarauntDrinkSize,restarauntPriceDrink,orderList)
        else:
          print("I'm sorry, I didn't get that")
    #If the question isn't one of the questions listed above, then the computer will print a random response from the response list.  
    else:
      print(randomAnswerList[random.randint(0,4)])
    print("")