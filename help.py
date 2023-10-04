# Ano ang requirements ng program? (Review pdf)
# what do you need for that requirement?

# 1. Variable named security pin initialized into none
# 2. Create a function that prints main menu
def menu():
    
    print(" Menu ")
    print(" 0 - Exit program ")
    print(" 1 - Unlock secret message ")
    print(" 2 - Change Security Pin ")
    print("")

    x = int(input("Enter a number: "))
    return x

def secret_message(securityPin):
    if securityPin == None:
        while(True):
            securityPin = input("Enter New Pin: ")
            if len(securityPin) == 4 and securityPin.isalnum():
                break
        print("Successfully created a new pin")
    else:
        choice = input("Enter PIN: ")
        if securityPin == choice:
            print("Secret Message")
        else:
            print("Wrong Pin!")
    
    return securityPin

def manage_pin(securityPin):
    if securityPin == None:
        while(True):
            securityPin = input("Enter New Pin: ")
            if len(securityPin) == 4 and securityPin.isalnum():
                break
        print("Successfully created a new pin")
    else:
        oldPin = input("Enter PIN:")
        if oldPin == securityPin:
            while(True):
                securityPin = input("Enter New Pin: ")
                if len(securityPin) == 4 and securityPin.isalnum():
                    break
            print("Successfully created a new pin")                
        else:
            print("Invalid")

    return securityPin


# 3. Get input once menu is printed. Depending on the value of input do the following
# 4. Function - prints secret message
# 5. Function for managing the PIN (create or change)
securityPin = None
while (True):
    choice = menu()
    if choice == 0:
        break
    elif choice == 1:
       securityPin = secret_message(securityPin)
    elif choice == 2:
        securityPin = manage_pin(securityPin)
    else:
        print("i")

df