from mysql.connector import connect, Error

db = connect(
    host="localhost", 
    user="root", 
    password="1234"
)
cursor = db.cursor()
inp = input('''\nSelect a function:

1 : Create a database
=> ''')
if inp == '1':
    while True:
        name = input('\nChoose a name for new database: ').lower()
        try:
            cursor.execute(f'CREATE DATABASE {name};')
            db = connect(host="localhost", user="root", password="1234", database=name)
            print('\nConnection successful, database selected.')
            break
        except Error as err:

            if err.errno == 1064:
                print("\nInappropriate name, choose a different name.")

            if err.errno == 1007:
                print("\nName used, choose a different name.")