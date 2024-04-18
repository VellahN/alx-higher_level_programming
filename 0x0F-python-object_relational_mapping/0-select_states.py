#!/usr/bin/python3
import sys
import MySQLdb

def list_states(username, password, database_name):
    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )
        
        # Create a cursor object using cursor() method
        cursor = db.cursor()
        
        # SQL query to select all states sorted by states.id
        sql_query = "SELECT * FROM states ORDER BY id ASC"
        
        # Execute SQL query
        cursor.execute(sql_query)
        
        # Fetch all rows
        states = cursor.fetchall()
        
        # Display results
        for state in states:
            print(state)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)

