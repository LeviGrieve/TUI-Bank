accounts = {
    "1": {"name": "Levi", "pin": "1234", "balance": 1000, "born": "24/10/2010"},
    "2": {"name": "Sam", "pin": "0001", "balance": 550, "born": "11/3/2006"},
    "3": {"name": "Liam", "pin": "0101", "balance": 1500, "born": "3/2/2014"} 
}

choice = input("What would you like to do? \n 1- Login \n 2- Quit\n  -").lower().strip()

if choice in ("login", "1"):
    login_details = input("\nProcessing... Would you like to 1- Login or 2- Sign Up?").lower().strip()

    if login_details in ("login", "1"):
        print

    elif login_details in ("sign up", "2"):
        print

    else:
        print("\nInvalid option/ Please resart and type either 'login' or 'quit'")
    
    

elif choice in ("quit", "2"):
    print("Thanks for visiting The Bank")

else:
    print("\nInvalid option/ Please resart and type either 'login' or 'quit'")
