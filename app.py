import dbcreds
import mariadb

def get_all_sales_person():
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute('CALL get_all_sales_person()')
        result = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Something went wrong. The appropriate person has been notified.")

    for person in result:
        print("\n", person)

    user_selection = input("\nWho do you pick? Chose from 1, 2 or 3.")
    user_id = int(user_selection)
    return user_id

def buy_item(sales_person_id):
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute('CALL get_all_items()')
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Something went wrong. The appropriate person has been notified.")

    for item in result:
        print(item)

    item_picked = input("\nWhat item you wanna buy?")
    item_id = int(item_picked)

    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute('CALL insert_item(?,?)', [sales_person_id, item_id])
        cursor.close()
        conn.close()
    except:
        print("Something went wrong. The appropriate person has been notified.")

def run_app():
    while(True):
        print("1. Run the app.")
        print("2. Quit the app.")
        user_input = input("1 or 2?\n")

        if(user_input == '1'):
            id = get_all_sales_person()
            buy_item(id)
        else:
            return

run_app()