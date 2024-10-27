import os
from dotenv import load_dotenv
import pyodbc
import mariadb

# Load environment variables from .env file
load_dotenv()

# Retrieve database credentials from environment variables
filemaker_dsn = os.getenv("FILEMAKER_DSN")
filemaker_user = os.getenv("FILEMAKER_USER")
filemaker_password = os.getenv("FILEMAKER_PASSWORD")

mariadb_host = os.getenv("MARIADB_HOST")
mariadb_user = os.getenv("MARIADB_USER")
mariadb_password = os.getenv("MARIADB_PASSWORD")
mariadb_db = os.getenv("MARIADB_DB")

# Step 1: Connect to FileMaker
def filemaker_connection():
    try:
        connection_string = f'DSN={filemaker_dsn};UID={filemaker_user};PWD={filemaker_password};'
        conn = pyodbc.connect(connection_string)
        print("Connected to FileMaker successfully!")

        return conn

    except Exception as e:
        print("Error connecting to FileMaker:", e)
        return None


# Step 2: Connect to MariaDB
def mariadb_connection():
    try:
        conn = mariadb.connect(
            host=mariadb_host,
            user=mariadb_user,
            password=mariadb_password,
            database=mariadb_db
        )
        print("Connected to MariaDB successfully!")
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None

# Step 3: Transfer Data to MariaDB
def data_transfer():
    fm_conn = filemaker_connection()
    mdb_conn = mariadb_connection()

    if fm_conn and maria_conn:
        try:
            with fm_conn.cursor() as fm_cursor, mdb_conn.cursor() as mdb_cursor:
                fm_query = "SELECT * FROM table_name"
                print (f"Executing query: {fm_query}")
                fm_cursor.execute(fm_query)
                rows = fm_cursor.fetchall()

                # Insert data into MariaDB
                insert_query = """
                INSERT INTO your_table_name (column1, column2, column3, column4) 
                VALUES (%s, %s, %s, %s)
                """  # Adjust as needed
                for row in rows:
                    data = tuple(row)
                    mdb_cursor.execute(insert_query, data)
                    print(f"Inserting into: {your_table_name}")
                
                mdb_cursor.commit()
                print("Data transferred to MariaDB successfully")

        except Exception as e:
            print(f"Error inserting data into MariaDB: {e}")
            maria_conn.rollback()
        finally:
            fm_conn.close()
            maria_conn.close()
            server.stop()
            logging.info("MariaDB Connection closed")


if __name__ == "__main__":
    data_transfer()