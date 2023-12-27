from tabulate import tabulate #using tabulate to form tables
import sys, subprocess #clearing
import time #using time delay for effects somewhere in the program
import sys, time, os #for another effect >:D

#clearing the screen so its not clutterred
subprocess.run ("cls", shell= True)
def clear(): #placing it in a function so its easier to call
    operating_system = sys.platform
    if operating_system == "win32":
        subprocess.run("cls", shell= True) 

#function to handle items stock 
def stock_system(item, quantity):
    item["Stock"] -= quantity

#title of the machine
print ("""
░█████╗░░█████╗░███████╗███████╗ ██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░ ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝ ██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░ ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
██║░░╚═╝███████║█████╗░░█████╗░░ ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░ ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
██║░░██╗██╔══██║██╔══╝░░██╔══╝░░ ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗ ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
╚█████╔╝██║░░██║██║░░░░░███████╗ ░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝ ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝ ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░ ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝ """)
#fancy title for fancy font

user_money = 0 #machine has no money whatsoever

#list of items (8 coffees and 8 cakes and muffins)
coffee_drinks = {
    "A1": {"Name": "Frappuccino", "Price": 10, "Stock": 5},
    "A2": {"Name": "Latte", "Price": 10, "Stock": 5},
    "A3": {"Name": "Swiss Mocha", "Price": 10, "Stock": 5},
    "A4": {"Name": "Espresso", "Price": 10, "Stock": 5},
    "B1": {"Name": "Cafè Machiatto", "Price": 10, "Stock": 5},
    "B2": {"Name": "Cappuccino", "Price": 10, "Stock": 5},
    "B3": {"Name": "Americano", "Price": 10, "Stock": 5},
    "B4": {"Name": "Iced Coffee", "Price": 10, "Stock": 5}
}

sweet_snacks = {
    "C1" : {"Name" : "Strawberry Cheesecake", "Price" : 7, "Stock" : 3},
    "C2" : {"Name" : "Honey Cake", "Price" : 7, "Stock" : 3},
    "C3" : {"Name" : "Vanilla Fruit Cake", "Price" : 7, "Stock" : 3},
    "C4" : {"Name" : "Red Velvet Cake", "Price" : 7, "Stock" : 3},
    "D1" : {"Name" : "Chocolate Muffin", "Price" : 5, "Stock" : 4},
    "D2" : {"Name" : "Blueberry Muffin", "Price" : 5, "Stock" : 4},
    "D3" : {"Name" : "Almonds and Cream Muffin", "Price" : 5, "Stock" : 4},
    "D4" : {"Name" : "Cheddar Muffin", "Price" : 5, "Stock" : 4}
}

#separating the headers since tabulate printed the keys instead >:(
drinks_headers = ["Code", "Name", "Price", "Stock"]
snacks_headers = ["Code", "Name", "Price", "Stock"]

#start of the machine
while True:
    start = input("Welcome to Cafe Vending Machine, Would you like to get started?: ").upper()
    if start == "NO":
        print ("""
░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝""")
        print ("""
▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █▀ █ █▄░█ █▀▀   █▀█ █░█ █▀█   █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   █▄█ ▄█ █ █░▀█ █▄█   █▄█ █▄█ █▀▄   ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄""")
        break
    elif start != "YES":
        print ("Please enter Yes/No")
        continue #repeats the whole thing again >:D (eheheh)
    
    clear() #cleans the screen :)

    #new screen, new output
    def menu():
        print ("""
▒█▀▀▄ ▒█▀▀█ ▀█▀ ▒█▄░▒█ ▒█░▄▀ ▒█▀▀▀█ 
▒█░▒█ ▒█▄▄▀ ▒█░ ▒█▒█▒█ ▒█▀▄░ ░▀▀▀▄▄ 
▒█▄▄▀ ▒█░▒█ ▄█▄ ▒█░░▀█ ▒█░▒█ ▒█▄▄▄█""") #display of drinks
    #this part took soo many modifications. I wanted to cry so badly :*(
        print(tabulate([[drink_h] + list(drink_i.values()) 
            for drink_h, drink_i in coffee_drinks.items()], headers = drinks_headers, tablefmt = "fancy_grid"))
        print ("""
▒█▀▀▀█ ▒█▄░▒█ ░█▀▀█ ▒█▀▀█ ▒█░▄▀ ▒█▀▀▀█ 
░▀▀▀▄▄ ▒█▒█▒█ ▒█▄▄█ ▒█░░░ ▒█▀▄░ ░▀▀▀▄▄ 
▒█▄▄▄█ ▒█░░▀█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▒█▄▄▄█""") #display of snacks
        print(tabulate([[snack_h] + list(snack_i.values()) 
            for snack_h, snack_i in sweet_snacks.items()], headers = snacks_headers, tablefmt = "fancy_grid"))
    
    menu() #show the menu

#the money input
    while True:
        insert_money = float(input("Enter amount: $"))
        if insert_money < 0:
            print ("Amount Error. Please insert money!")
            continue
        else:
            user_money += insert_money #updates the money inside the machine
            print (f"Your balance: ${user_money}")
            break

#choosing of items using while loop again
    while True:
        choose = input(f"Enter the item code: ").upper()
        all_items = {**coffee_drinks, **sweet_snacks}
        chosen_item = all_items.get(choose) #fetches the item

        if chosen_item:
            while chosen_item ["Stock"] == 0:
                print (f"Sadly the {chosen_item['Name']} is currently out of stock")
                choose = input(f"Enter the item code: ").upper()
                chosen_item = all_items.get(choose)

            while user_money < chosen_item["Price"]: #too add more money if its lacking
                print ("Your balance is insufficient..")
                insert_money_again = float(input("Please insert money: $"))
                user_money += insert_money_again
            print (f"Your updated balance: ${user_money}")

            user_money -=chosen_item["Price"]
            stock_system(chosen_item, 1) #removes 1 from the stock

            #new screen w/ updated stock
            clear ()
            menu()
            print (f"You have purchased {chosen_item['Name']} for ${chosen_item['Price']}")
            time.sleep(2) #small effect
            print ("""

█ ▀█▀ █▀▀ █▀▄▀█   █▀▄ █ █▀ █▀█ █▀▀ █▄░█ █▀ █▀▀ █▀▄
█ ░█░ ██▄ █░▀░█   █▄▀ █ ▄█ █▀▀ ██▄ █░▀█ ▄█ ██▄ █▄▀
                   """)
            print (f"Please collect your purchase of {chosen_item['Name']}!.")
            print (f"Your balance: ${user_money}")

            #option for user to buy more items and spend their money >:D
            buy_more = input("Would you like to buy more? (Yes/No): ").upper()
            if buy_more == "YES":
                continue
            elif buy_more == "NO": #ending animation
                print (f"You will be exited shortyly...")
            break
            
        else: 
            print ("Error: Item not found")
            continue
        break    
     #final animation for the item dispensing and exit
    print (f"Your change is ${user_money}")
    time.sleep(1) 
    print ("""
█▀▀ █░█ ▄▀█ █▄░█ █▀▀ █▀▀   █▀▄ █ █▀ █▀█ █▀▀ █▄░█ █▀ █▀▀ █▀▄
█▄▄ █▀█ █▀█ █░▀█ █▄█ ██▄   █▄▀ █ ▄█ █▀▀ ██▄ █░▀█ ▄█ ██▄ █▄▀""")
    time.sleep(4)
    clear()
    time.sleep(1)
    print ("""
█▀▀ ▀▄▀ █ ▀█▀ █ █▄░█ █▀▀
██▄ █░█ █ ░█░ █ █░▀█ █▄█""")
    exit_animation = """
▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄"""
    for exit in exit_animation: #text effects like a typewriter
        sys.stdout.write(exit)
        sys.stdout.flush()
        time.sleep(0.2)
    clear()
    time.sleep(1)
    print (""" 
░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝""")#final message YAY!!
    print ("""
▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █▀ █ █▄░█ █▀▀   █▀█ █░█ █▀█   █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   █▄█ ▄█ █ █░▀█ █▄█   █▄█ █▄█ █▀▄   ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄""")
    break
#end of the machine
#this took approximately 1 week because i kept procrastinating ;)