from db import get_connection

def display_row():
    """Fetch and display all saved site credentials in a neatly formatted table."""
    try:
        # Establish a connection to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Retrieve all password entries
        cursor.execute(
            "SELECT site_name, username, password FROM passwords"
        )
        rows = cursor.fetchall()

        # If no entries are found, notify the user
        if not rows:
            print("No entries found in the password manager.")
        else:
            # Determine column widths based on headers and data
            w_site = max(len("Site"), *(len(r[0]) for r in rows))
            w_user = max(len("Username"), *(len(r[1]) for r in rows))
            w_pwd  = max(len("Password"), 8)

            # Print table header
            header = f"{'Site':<{w_site}}  {'Username':<{w_user}}  {'Password':<{w_pwd}}"
            separator = "-" * (w_site + w_user + w_pwd + 4)

            print(header)
            print(separator)

            # Print each row of site credentials
            for site, user, pwd in rows:
                print(f"{site:<{w_site}}  {user:<{w_user}}  {pwd:<{w_pwd}}")

        # Pause to let the user review results
        input("\nHit any key to continue: ")

    except Exception as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        conn.close()