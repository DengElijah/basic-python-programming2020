def register_user(users):
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please choose a different one.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print("User registered successfully!")


def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
    else:
        print("Invalid username or password.")


def main():
    users = {}

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            register_user(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
