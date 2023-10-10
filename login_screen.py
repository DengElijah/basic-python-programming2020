def login_screen():
    print("Welcome to the Login Screen!")
    print("---------------------------")
    username = input("Username: ")
    password = input("Password: ")
    print("---------------------------")
    print("Logging in...")
    # Add your authentication logic here
    if username == "deng" and password == "deng":
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Call the login_screen function to display the login screen
login_screen()
