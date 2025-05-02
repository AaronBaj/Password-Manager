from db import get_connection

def add_password_row(site_name, username, password):
    """Insert a new credential record into the passwords table."""
    try:
        # Open a database connection and cursor
        conn = get_connection()
        cursor = conn.cursor()

        # Define the INSERT statement for a new password entry
        insert_sql = (
            """
            INSERT INTO passwords (site_name, username, password)
            VALUES (%s, %s, %s)
            """
        )

        # Execute the statement with provided parameters
        cursor.execute(insert_sql, (site_name, username, password))

        # Commit the transaction to save changes
        conn.commit()

        # Notify the user of success
        print("New account successfully added!\n")
        input("Enter any key to continue: ")

    except Exception as err:
        # Print any errors encountered during insertion
        print(f"Error: {err}")

    finally:
        # Always close cursor and connection to free resources
        cursor.close()
        conn.close()
