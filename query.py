import sqlite3 as sqli

connection = sqli.connect("database/data.db")

cursor = connection.cursor()

command = None

while(command != 'q'):
    command=str(input("=>"))
    try:
        if command != (None or "q"):
            cursor = connection.cursor()
            cursor.execute(command)
            print("=>",cursor.fetchone())
    except:
        print("=>error in execution")