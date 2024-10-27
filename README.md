# FileMaker-to-MariaDB
Data migration from FileMaker to MariaDB using Python

This guide provides a structured approach to transfer data from FileMaker to MariaDB using Python. The steps include setting up a virtual environment for dependency management, installing necessary packages (pyodbc for FileMaker, mariadb for MariaDB), and using a .env file to securely store connection credentials.

Key Highlights
Environment Setup: Create a virtual environment to isolate dependencies and ensure reproducibility.
Installing Packages: Install pyodbc and mariadb packages to facilitate connections.
Connection:  MariaDB direct connection.
Data Transfer Script: Includes a Python script to connect to FileMaker, retrieve data, and insert it into MariaDB.
Dependency Management: Use pip freeze > requirements.txt to document dependencies, enabling easy environment setup for collaborators.


.env File Content
Create a .env file in your project directory to securely store database connection details:


# FileMaker credentials
FILEMAKER_DSN=your_dsn_name
FILEMAKER_USER=your_username
FILEMAKER_PASSWORD=your_password

# MariaDB credentials
MARIADB_HOST=your_mariadb_host
MARIADB_USER=your_mariadb_username
MARIADB_PASSWORD=your_mariadb_password
MARIADB_DB=your_mariadb_database
