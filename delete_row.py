from db import get_connection

def delete_password_row(site_name_to_delete, username_to_delete):
    """Delete a specific site credential based on site name and username."""
    try:
        # Connect to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Prepare and execute the DELETE statement
        delete_sql = (
            """
            DELETE FROM passwords
            WHERE site_name = %s AND username = %s
            """
        )
        cursor.execute(delete_sql, (site_name_to_delete, username_to_delete))

        # Persist changes
        conn.commit()

        # Inform user of successful deletion
        print("Account successfully deleted!\n")
        input("Enter any key to continue: ")

    except Exception as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        conn.close()
