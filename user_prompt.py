import getpass
from db import get_connection
import psycopg2
import bcrypt

def ensure_tables_exist():
    """Create users and passwords tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Create a table to store application users
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # Create a table to store site-specific credentials
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS passwords (
                id SERIAL PRIMARY KEY,
                site_name VARCHAR(100) NOT NULL,
                username VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.commit()
        print("Database tables initialized.")
        return True

    except psycopg2.Error as e:
        # Log database errors if table creation fails
        print(f"Database error: {e}")
        return False

    finally:
        cursor.close()
        conn.close()


def create_user():
    """Prompt for new account details, hash the password, and save the user."""
    # Ensure necessary tables are available before proceeding
    if not ensure_tables_exist():
        print("Failed to initialize database tables.")
        input("Hit any key to continue: ")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Only allow one user per device for this application
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]

        if user_count > 0:
            print("\nAn account already exists; only one user per device is allowed.")
            input("Hit any key to continue: ")
            return

        # Collect and normalize username
        username = input("Enter your username: ").strip().lower()
        # Securely collect password without echoing
        password = getpass.getpass("Enter your password: ")

        # Hash the password for secure storage
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, hashed_pw)
        )

        conn.commit()
        print("\nUser created successfully!")
        input("Hit any key to continue: ")

    except psycopg2.Error as e:
        # Handle errors during user creation
        print(f"\nDatabase error: {e}")
        input("Hit any key to continue: ")

    finally:
        cursor.close()
        conn.close()


def login():
    """Authenticate existing user credentials against stored data."""
    # Check or create necessary tables first
    if not ensure_tables_exist():
        print("Failed to initialize database tables.")
        input("Hit any key to continue: ")
        return False

    try:
        # Prompt for login credentials
        username = input("Enter your username: ").strip().lower()
        password = getpass.getpass("Enter your password: ")

        conn = get_connection()
        cursor = conn.cursor()

        # Retrieve the stored hash for the given username
        cursor.execute(
            "SELECT password FROM users WHERE username = %s",
            (username,)
        )
        result = cursor.fetchone()

        if result and bcrypt.checkpw(password.encode(), result[0].encode()):
            # Credentials match: login successful
            cursor.close()
            conn.close()
            return True

        # Credentials did not match
        print("\nUsername or password incorrect.")
        input("Hit any key to continue: ")
        cursor.close()
        conn.close()

        return False

    except psycopg2.Error as e:
        # Handle database errors during login
        print(f"\nDatabase error: {e}")
        input("Hit any key to continue: ")
        return False
