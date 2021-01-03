import psycopg2

db_settings = {}
try:
    with open("resources/db_settings", "r") as settings:
        for line in settings:
            (key, val) = line.split()
            db_settings[key] = str(val)
except ValueError:
    print("Please provide values in resources/db_settings")
    exit(100)
conn = psycopg2.connect(host=db_settings['host:'], database=db_settings['database:'], user=db_settings['user:'],
                        password=db_settings['password:'])
cur = conn.cursor()


def store_password(username, email, password, website):
    pubkey = open("resources/pubkey.asc", "r").read()
    data = (username, email, password, pubkey, website)
    SQL = "INSERT INTO password (username,email,pw,website) VALUES (%s,%s,pgp_pub_encrypt(%s,dearmor(%s)),%s)"
    cur.execute(SQL, data)
    conn.commit()


def delete_password(username, email, website):
    data = (username, email, website)
    SQL = "DELETE FROM password where username = %s AND email = %s and website = %s"
    cur.execute(SQL, data)
    conn.commit()


def find_by_mail(pw: str, email: str):
    private_key = open("resources/privkey.asc", 'r').read()
    data = (private_key, pw, email)
    format = ('Username: ', 'Email: ', 'Password: ', 'App/Site name: ')
    SQL = "SELECT username,email,pgp_pub_decrypt(pw :: bytea,dearmor(%s),%s),website FROM password WHERE email = %s"
    cur.execute(SQL, data)

    result = cur.fetchall()
    if not result:
        print("No entry found")
    else:
        for row in result:
            print()
            for i in range(0, len(row)):
                print(format[i] + row[i])


def find_by_website(pw: str, website: str):
    private_key = open("resources/privkey.asc", 'r').read()
    data = (private_key, pw, website)
    format = ('Username: ', 'Email: ', 'Password: ', 'App/Site name: ')
    SQL = "SELECT username,email,pgp_pub_decrypt(pw :: bytea,dearmor(%s),%s),website FROM password WHERE website = %s"

    cur.execute(SQL, data)
    result = cur.fetchall()
    if not result:
        print("No entry found")
    else:
        for row in result:
            print()
            for i in range(0, len(row)):
                print(format[i] + row[i])


def find_by_website_and_email(pw: str, website: str, email: str):
    private_key = open("resources/privkey.asc", 'r').read()
    data = (private_key, pw, website, email)
    SQL = "SELECT username,email,pgp_pub_decrypt(pw :: bytea,dearmor(%s),%s),website FROM password WHERE website = %s AND email = %s"

    cur.execute(SQL, data)
    result = cur.fetchone()
    if result is None:
        print("No entry found")
    else:
        print("Username: " + result[0])
        print("Password: " + result[2])
