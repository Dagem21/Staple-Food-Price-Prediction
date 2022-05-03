import psycopg2


# from ..Models import User

def close(conn):
    if conn is not None:
        conn.close()


def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5433",
            database="sfpp_db",
            user="postgres",
            password="postgres")

        return conn, None

    except (Exception, psycopg2.DatabaseError) as error:
        return None, error


def getUser(phone_number):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
        query = "SELECT * FROM users WHERE phone_number = %s;"
        curr.execute(query, (phone_number,))
        rows = curr.fetchall()
        if len(rows) == 0:
            return None, None
        for row in rows:
            return
            # user = User(row[0], row[1], row[2], row[3], row[4], row[5])
            # return user, None
    except Exception as e:
        print(e)
        return None, e


def getUsers():
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
        query = "SELECT * FROM users;"
        curr.execute(query, )
        rows = curr.fetchall()
        if len(rows) == 0:
            return None, None
        users = []
        for row in rows:
            return
            # user = User(row[0], row[1], row[2], row[3], row[4], row[5])
            # users.append(user)
        # return user, None
    except Exception as e:
        return None, e


def addUser(phone_number, username, password, user_type):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def addFoodPrice(food_name, location, month, price):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def updatePassword(phone_number, password):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def getPredictions():
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def getPrediction():
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def addWeatherData(location, month, value):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def addFuelData(month, fuel_type, value):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def addExchangeRateData(month, value):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def getData(location, month):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def addPredictions(food_name, location, m1, m2, m3, m4, m5, m6):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def getPredictions():
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def getPrediction(food_name):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


def getPredictionLocation(location):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while connecting to the database!"
        curr = conn.cursor()
    except Exception as e:
        return e


if __name__ == '__main__':
    getUsers()
