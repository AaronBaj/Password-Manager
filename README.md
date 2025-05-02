# Password-Manager

A simple command-line password manager that stores website credentials securely in a PostgreSQL database. This application allows users to create an account, log in, and manage their website passwords.

## Features

- User authentication with bcrypt password hashing
- Store website credentials (site name, username, password)
- View all stored passwords
- Delete stored credentials
- Single-user design for personal use

## Prerequisites

- Python 3.11+
- PostgreSQL 17+
- pip

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/personal-password-manager.git
cd personal-password-manager
```

### 2. Install PostgreSQL

#### On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

#### On macOS (using Homebrew):
```bash
brew install postgresql
brew services start postgresql
```

#### On Windows:
- Download the installer from [PostgreSQL official website](https://www.postgresql.org/download/windows/)
- Run the installer and follow the instructions

### 3. Create a PostgreSQL database

Log in to PostgreSQL:

```bash
# On Linux/macOS (as postgres user)
sudo -u postgres psql

# On Windows (after installation)
psql -U postgres
```

Create a database and user:

```sql
CREATE DATABASE pwdmgr;
CREATE USER pwduser WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE pwdmgr TO pwduser;
\q
```

### 4. Install Python dependencies

```bash
pip install psycopg2-binary python-dotenv bcrypt
```

### 5. Set up environment variables

Create a `.env` file in the project root directory:

```
PG_HOST=localhost
PG_PORT=5432
PG_USER=pwduser
PG_PASSWORD=your_password
PG_DB=pwdmgr
```

## Usage

Run the application:

```bash
python main.py
```

### First-time setup:

1. Choose option `1` to create a login
2. Enter a username and password for your account
3. Log in with your new credentials

### Managing passwords:

After logging in, you can:
- Add new website credentials
- Delete existing credentials
- View all stored passwords
- Log out

## Security Notes

- Currently, website passwords are stored in plaintext in the database
- The master user password is properly hashed using bcrypt
- For better security, consider enhancing the application to encrypt the stored website passwords
- This application is designed for personal use on a secure local machine

## Project Structure

- `main.py` - Main application entry point
- `user_prompt.py` - User authentication functions
- `db.py` - Database connection management
- `add_row.py` - Functions to add password entries
- `delete_row.py` - Functions to delete password entries
- `display.py` - Functions to display password entries

## Future Improvements

- Encrypt stored website passwords
- Add password generation functionality
- Implement password strength checking
- Add search functionality for stored passwords
- Add export/import functionality
- Implement password categories/tags
