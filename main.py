import add_row
import delete_row
import display
import user_prompt

def main():
    """Entry point for the Personal Password Manager CLI application."""
    print("\nPersonal Password Manager")

    while True:
        # Show main menu options
        print(
            "\nMain Menu:"  
            "\n1. Create Account"
            "\n2. Login"
            "\n3. Exit"
        )
        choice = input("\nEnter an option: ").strip()

        if choice == '1':
            # Handle new user creation
            user_prompt.create_user()

        elif choice == '2':
            # Attempt user login
            if user_prompt.login():
                print("\nLogin successful!")
                input("Hit any key to continue: ")

                # Show submenu
                while True:
                    print(
                        "\nPassword Manager Options:"
                        "\n1. Add Password"
                        "\n2. Delete Password"
                        "\n3. Display Passwords"
                        "\n4. Logout"
                    )
                    sub_choice = input("\nEnter your choice: ").strip()

                    if sub_choice == '1':
                        # Gather new credential details
                        site_name = input("Enter the website name: ")
                        username  = input("Enter your username: ")
                        password  = input("Enter your password: ")
                        add_row.add_password_row(site_name, username, password)

                    elif sub_choice == '2':
                        # Gather deletion criteria
                        site_name = input("Enter site name to delete: ")
                        username  = input("Enter username to delete: ")
                        delete_row.delete_password_row(site_name, username)

                    elif sub_choice == '3':
                        # Display all stored credentials
                        display.display_row()

                    elif sub_choice == '4':
                        # Logout and return to main menu
                        print("Logging out...")
                        break

                    else:
                        # Handle invalid submenu input
                        print("Invalid choice. Please enter a number 1-4.")
                        input("Hit any key to continue: ")
            else:
                # Login failed, nothing happens user returns to main menu
                pass

        elif choice == '3':
            # Exit the application
            print("Goodbye!")
            break

        else:
            # Handle invalid main menu input
            print("Invalid input. Please enter a number 1-3.")
            input("Hit any key to continue: ")


if __name__ == "__main__":
    main()
