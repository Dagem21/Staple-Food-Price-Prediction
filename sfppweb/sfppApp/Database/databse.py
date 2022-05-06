from datetime import datetime
import psycopg2
from ..Models import User, Predictions, Data, Food


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
            return None, "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        query = "SELECT * FROM users WHERE phone_number = %s;"
        curr.execute(query, (str(phone_number),))
        rows = curr.fetchall()
        if len(rows) == 0:
            return None, "User not found!"
        for row in rows:
            user = User.User(row[1], row[2], row[3], row[4], row[5], row[0])
            return user, None
        close(conn)
    except Exception as e:
        return None, e


def getUsers():
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        query = "SELECT * FROM users;"
        curr.execute(query, )
        rows = curr.fetchall()
        usersList = []
        for row in rows:
            user = User(row[0], row[1], row[2], row[3], row[4], row[5])
            usersList.append(user)
        close(conn)
        return usersList, None
    except Exception as e:
        return None, e


def addUser(phone_number, username, password, user_type):
    try:
        conn, err = connect()
        if err is not None:
            return False, "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        if phone_number is None or username is None or password is None or user_type is None:
            return False, "All fields must be provided!"
        else:
            query = "INSERT INTO users (phone_number, username, password, user_role, created_at) VALUES ( %s, %s, %s, " \
                    "%s, %s); "
            now = datetime.now()
            createdAt = now.strftime("%d/%m/%Y %H:%M:%S")
            curr.execute(query, (str(phone_number), str(username), str(password), int(user_type), createdAt,))
            conn.commit()
        conn.close()
        return True, None
    except psycopg2.IntegrityError:
        return False, "This phone numbers is already registered."
    except Exception as e:
        return False, e


def addFoodPrice(food_name, location, month, price):
    try:
        conn, err = connect()
        if err is not None:
            return False, "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        if food_name is None or location is None or month is None or price is None:
            return False, "All fields must be provided!"
        else:
            query = "INSERT INTO foodprice (month, location, food, price) VALUES ( %s, %s, " \
                    "%s, %s); "
            curr.execute(query, (str(month), str(location), str(food_name), float(price),))
            conn.commit()
        close(conn)
        return True, None
    except Exception as e:
        return False, e


def getFoodPrice(food_name, location):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while processing Your request! Please try again."
        if location is None or food_name is None:
            return None, "All fields must be provided!"
        curr = conn.cursor()
        query = "SELECT * FROM foodprice WHERE food = %s AND location = %s;"
        curr.execute(query, (food_name, location,))
        rows = curr.fetchall()
        price = {}
        for row in rows:
            price[row[1]] = row[3]
        foodPrice = Food(food_name, location, price)
        close(conn)
        return foodPrice, None
    except Exception as e:
        return None, e


def updatePassword(phone_number, password):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        if phone_number is None or password is None:
            return False, "All fields must be provided!"
        else:
            query = "UPDATE users SET password = %s WHERE phone_number = %s;"
            curr.execute(query, (password, str(phone_number),))
        conn.commit()
        close(conn)
        return True, None
    except Exception as e:
        return False, e


def addWeatherData(location, month, value):
    try:
        conn, err = connect()
        if err is not None:
            return False, "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        if location is None or month is None or value is None:
            return False, "All fields must be provided!"
        else:
            query = "INSERT INTO data (month , location, precipitation) VALUES ( %s, %s, %s) ON CONFLICT (month, " \
                    "location) DO UPDATE SET precipitation = %s; "

            curr.execute(query, (month, location, float(value), float(value),))
            conn.commit()
        conn.close()
        return True, None
    except Exception as e:
        return False, e


def addFuelData(month, location, fuel_type, value):
    try:
        conn, err = connect()
        if err is not None:
            return False, "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        if fuel_type is None or month is None or location is None or value is None:
            return False, "All fields must be provided!"
        else:
            query = "INSERT INTO data (month , location, %s) VALUES ( %s, %s, %s) ON CONFLICT (month, " \
                    "location) DO UPDATE SET %s = %s; "

            curr.execute(query, (fuel_type, month, location, float(value), fuel_type, float(value),))
            conn.commit()
        conn.close()
        return True, None
    except Exception as e:
        return False, e


def addExchangeRateData(month, location, value):
    try:
        conn, err = connect()
        if err is not None:
            return False, "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        if location is None or month is None or value is None:
            return False, "All fields must be provided!"
        else:
            query = "INSERT INTO data (month , location, exchange_rate) VALUES ( %s, %s, %s) ON CONFLICT (month, " \
                    "location) DO UPDATE SET exchange_rate = %s; "

            curr.execute(query, (month, location, float(value), float(value),))
            conn.commit()
        conn.close()
        return True, None
    except Exception as e:
        return False, e


def getData(location):
    try:
        conn, err = connect()
        if err is not None:
            return [], "An error occurred while processing Your request! Please try again."
        if location is None:
            return [], "Location must be provided!"
        curr = conn.cursor()
        query = "SELECT * FROM data WHERE location = %s;"
        curr.execute(query, (location,))
        rows = curr.fetchall()
        dataList = []
        for row in rows:
            data = Data(row[1], row[2], row[3], row[4], row[5], row[6], row[0])
            dataList.append(data)
        close(conn)
        return dataList, None
    except Exception as e:
        return [], e


def getData(location, month):
    try:
        conn, err = connect()
        if err is not None:
            return None, "An error occurred while processing Your request! Please try again."
        if location is None or month is None:
            return None, "All fields must be provided!"
        curr = conn.cursor()
        query = "SELECT * FROM data WHERE location = %s AND month = %s;"
        curr.execute(query, (location, month,))
        rows = curr.fetchall()
        for row in rows:
            data = Data(row[1], row[2], row[3], row[4], row[5], row[6], row[0])
            close(conn)
            return data, None
    except Exception as e:
        return None, e


def addPredictions(food_name, location, start_month, percent_change, m1, m2, m3, m4, m5, m6):
    try:
        conn, err = connect()
        if err is not None:
            return False, "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        if location is None or food_name is None or start_month is None or percent_change is None \
                or m1 is None or m2 is None or m3 is None or m4 is None or m5 is None or m6 is None:
            return False, "All fields must be provided!"
        else:
            query = "INSERT INTO predictions (location, food, start_month, m1_price, m2_price, m3_price, m4_price," \
                    " m5_price, m6_price, percent_change) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT " \
                    "(location, food) DO UPDATE SET start_month = %s, m1_price = %s, m2_price = %s, m3_price = %s," \
                    " m4_price = %s, m5_price = %s, m6_price = %s, percent_change = %s; "

            curr.execute(query, (location, food_name, start_month, m1, m2, m3, m4, m5, m6, percent_change, start_month,
                                 m1, m2, m3, m4, m5, m6, percent_change,))
            conn.commit()
        conn.close()
        return True, None
    except Exception as e:
        return False, e


def getPredictions():
    try:
        conn, err = connect()
        if err is not None:
            return [], "An error occurred while processing Your request! Please try again."
        curr = conn.cursor()
        query = "SELECT * FROM predictions;"
        curr.execute(query, )
        rows = curr.fetchall()
        predictionsList = []
        for row in rows:
            prediction = Predictions(row[1], row[2], row[3], [row[4], row[5], row[6], row[7], row[8], row[9]], row[10], row[0])
            predictionsList.append(prediction)
        close(conn)
        return predictionsList, None
    except Exception as e:
        return [], e


def getPrediction(food_name):
    try:
        conn, err = connect()
        if err is not None:
            return [], "An error occurred while processing Your request! Please try again."
        if food_name is None:
            return [], "Food name must be provided!"
        curr = conn.cursor()
        query = "SELECT * FROM predictions WHERE food = %s;"
        curr.execute(query, (food_name,))
        rows = curr.fetchall()
        predictionsList = []
        for row in rows:
            prediction = Predictions(row[1], row[2], row[3], [row[4], row[5], row[6], row[7], row[8], row[9]], row[10],
                                     row[0])
            predictionsList.append(prediction)
        close(conn)
        return predictionsList, None
    except Exception as e:
        return [], e


def getPredictionLocation(location):
    try:
        conn, err = connect()
        if err is not None:
            return [], "An error occurred while processing Your request! Please try again."
        if location is None:
            return [], "Food name must be provided!"
        curr = conn.cursor()
        query = "SELECT * FROM predictions WHERE location = %s;"
        curr.execute(query, (location,))
        rows = curr.fetchall()
        predictionsList = []
        for row in rows:
            prediction = Predictions(row[1], row[2], row[3], [row[4], row[5], row[6], row[7], row[8], row[9]], row[10],
                                     row[0])
            predictionsList.append(prediction)
        close(conn)
        return predictionsList, None
    except Exception as e:
        return [], e


if __name__ == '__main__':
    users, err = getUsers()
    print(len(users))
