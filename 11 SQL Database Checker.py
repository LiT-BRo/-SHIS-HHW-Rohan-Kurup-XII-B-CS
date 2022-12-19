from mysql.connector import connect

host = "localhost"
user = "root"
password = "1234"

db = connect(host=host,user=user,password=password)

cursor = db.cursor()

inp = input('''\nSelect a function:
1 : To view all current databases and select one 
=> ''')
if inp == '1':
    cursor.execute("SHOW DATABASES;")

    print("Choose database to select")
    databases = []
    for i, j in enumerate(cursor):
        databases.append(j[0])
        print('\t', i+1, ':=>', j[0], sep=' ')
    d_no = int(input('=> '))
    try:
        db = connect(host=host, user=user, password=password, database=databases[d_no])
        print('\nConnection successful, database selected.')
    except:
        print('\nConnection failed, try again.')