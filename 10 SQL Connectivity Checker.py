from mysql.connector import connect

host = input('\nPlease enter below the required details for MYSQL CONNECTIVITY\n\nEnter host name (Leave blank for DEFAULT=localhost) :')
if not host:
    host = "localhost"

user = input('Enter username (Leave blank for DEFAULT=root) :')
if not user:
    user = "root"

passw = input('Enter password (Leave blank for DEFAULT=1234) :')
if not passw:
    passw = "1234"

try:
    db = connect(
        host = host,
        user = user,
        password = passw
    )
    print('\nConnection successful, connector object made.')
    print(db)

except:
    print("\nConnection Failed, please try again.")