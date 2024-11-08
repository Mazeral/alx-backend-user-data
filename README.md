# Personal Data Management

This repository contains tasks that involve handling personal data securely, including logging, database interactions, and password encryption. The goal is to implement best practices in protecting sensitive data (PII) while performing operations like logging and accessing databases.

## Table of Contents
- [Installation](#installation)
- [Tasks](#tasks)
  - [0. Regex-ing](#0-regex-ing)
  - [1. Log Formatter](#1-log-formatter)
  - [2. Create Logger](#2-create-logger)
  - [3. Connect to Secure Database](#3-connect-to-secure-database)
  - [4. Read and Filter Data](#4-read-and-filter-data)
  - [5. Encrypting Passwords](#5-encrypting-passwords)
  - [6. Check Valid Password](#6-check-valid-password)
- [Usage](#usage)
- [License](#license)

## Installation

### Prerequisites
- Python 3.x
- `mysql-connector-python` package
- `bcrypt` package
- MySQL server

To install the necessary Python packages, run:
```bash
pip3 install mysql-connector-python bcrypt
```

## Tasks

### 0. Regex-ing

Write a function called `filter_datum` that takes in:
- `fields`: A list of strings representing all fields to obfuscate.
- `redaction`: A string to replace the field value.
- `message`: The log line that contains the fields.
- `separator`: A character separating the fields in the log line.

The function uses regex to replace the field values and obfuscates the sensitive information.

#### Example:
```python
fields = ["password", "date_of_birth"]
message = "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
print(filter_datum(fields, 'xxx', message, ';'))
# Output: "name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;"
```

### 1. Log Formatter

Implement the `RedactingFormatter` class, which filters values of specific fields in log records. This class uses the `filter_datum` function to redact sensitive information in the logs.

#### Example:
```python
message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
formatter = RedactingFormatter(fields=["email", "ssn", "password"])
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
print(formatter.format(log_record))
# Output: "[HOLBERTON] my_logger INFO 2023-10-22 10:45:00: name=Bob; email=***; ssn=***; password=***;"
```

### 2. Create Logger

Implement a `get_logger` function that returns a logger named `"user_data"` with the following specifications:
- Logs up to `INFO` level.
- Does not propagate messages to other loggers.
- Includes a `StreamHandler` with `RedactingFormatter` using fields defined in a tuple `PII_FIELDS`.

### 3. Connect to Secure Database

Implement a `get_db` function that connects to a MySQL database using credentials stored in environment variables:
- `PERSONAL_DATA_DB_HOST`
- `PERSONAL_DATA_DB_USERNAME`
- `PERSONAL_DATA_DB_PASSWORD`
- `PERSONAL_DATA_DB_NAME`

The function returns a `mysql.connector.connection.MySQLConnection` object.

### 4. Read and Filter Data

Create a `main` function that retrieves all rows from the `users` table in the database and logs each row in a filtered format using the logger created in Task 2. Fields like `name`, `email`, `phone`, `ssn`, and `password` should be redacted.

### 5. Encrypting Passwords

Implement a `hash_password` function that hashes a password using `bcrypt` and returns the salted, hashed password as a byte string.

#### Example:
```python
password = "MyAmazingPassw0rd"
hashed_password = hash_password(password)
print(hashed_password)
# Output: A hashed password in the form of a byte string
```

### 6. Check Valid Password

Implement an `is_valid` function that checks if a provided password matches a hashed password using `bcrypt`.

#### Example:
```python
password = "MyAmazingPassw0rd"
hashed_password = hash_password(password)
print(is_valid(hashed_password, password))
# Output: True
```

## Usage

1. **Setting Environment Variables**:
   Ensure you set the appropriate environment variables for your MySQL database:
   ```bash
   export PERSONAL_DATA_DB_HOST=localhost
   export PERSONAL_DATA_DB_USERNAME=root
   export PERSONAL_DATA_DB_PASSWORD=root_password
   export PERSONAL_DATA_DB_NAME=my_db
   ```

2. **Running the Main Program**:
   After setting up the database and environment variables, run the main script:
   ```bash
   python3 filtered_logger.py
   ```

3. **Password Encryption**:
   For password-related tasks, run:
   ```bash
   python3 encrypt_password.py
   ```

## License

This project is licensed under the MIT License.
