import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env file
load_dotenv()

def get_connection():
    """
    Establish and return a psycopg2 database connection.

    Reads the following environment variables (with defaults):
      - PG_HOST (default: "localhost")
      - PG_PORT (default: 5432)
      - PG_USER
      - PG_PASSWORD
      - PG_DB
      - PG_SSLMODE (default: "disable")
    """
    # Fetch connection parameters from environment, applying defaults where needed
    host     = os.getenv("PG_HOST", "localhost")
    port     = int(os.getenv("PG_PORT", 5432))
    user     = os.getenv("PG_USER")
    password = os.getenv("PG_PASSWORD")
    dbname   = os.getenv("PG_DB")
    sslmode  = os.getenv("PG_SSLMODE", "disable")

    # Return a new database connection using psycopg2
    return psycopg2.connect(
        host     = host,
        port     = port,
        user     = user,
        password = password,
        dbname   = dbname,
        sslmode  = sslmode
    )
