from datetime import datetime
from sfppweb.sfppApp.Models import Food, Data, Predictions
from sfppweb.sfppApp.Database import databse
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
import pandas as pd
from sklearn.preprocessing import StandardScaler


class Prediction:

    def map_price_to_data(self, priceList, dataList):
        date = []
        price = []
        precipitation = []
        tempMax = []
        tempMin = []
        diesel = []
        kerosene = []
        exRate = []
        for data in dataList:
            if data.month in priceList:
                date.append(data.month)
                price.append(priceList[data.month])
                precipitation.append(data.precipitation)
                tempMax.append(data.maxTemp)
                tempMin.append(data.minTemp)
                diesel.append(data.dieselPrice)
                kerosene.append(data.petrolPrice)
                exRate.append(data.exRate)
        mapList = {'date': date, 'price': price, 'Precipitation': precipitation, 'TempMax': tempMax,
                   'TempMin': tempMin, 'Diesel': diesel, 'Kerosene': kerosene, 'ExRate': exRate}
        return mapList

    def predict_price(self):
        foodName = 'Maize (white)'
        location = 'Addis Ababa'
        food = Food(foodName, location)
        priceList = food.price
        data = Data(None, 'Addis Ababa')
        dataList = data.get_data()
        mappedList = self.map_price_to_data(priceList, dataList)

        df = pd.DataFrame(
            {'Date': mappedList['date'],
             'Price': mappedList['price'],
             'Precipitation': mappedList['Precipitation'],
             'TempMax': mappedList['TempMax'],
             'TempMin': mappedList['TempMin'],
             'Diesel': mappedList['Diesel'],
             'Kerosene': mappedList['Kerosene'],
             'ExRate': mappedList['ExRate']
             })
        df.index = pd.to_datetime(mappedList['date'], format='%m/%d/%Y')

        df['Seconds'] = df.index.map(pd.Timestamp.timestamp)

        train_dates = pd.to_datetime(df.index)

        cols = list(df)[1:9]

        df_for_training = df[cols].astype(float)

        scaler = StandardScaler()
        scaler = scaler.fit(df_for_training)
        df_for_training_scaled = scaler.transform(df_for_training)
        trainx = []
        trainy = []

        n_future = 1
        n_past = 10

        for i in range(n_past, len(df_for_training_scaled) - n_future + 1):
            trainx.append(df_for_training_scaled[i - n_past:i, 0:df_for_training.shape[1]])
            trainy.append(df_for_training_scaled[i + n_future - 1:i + n_future, 0])

        trainx, trainy = np.array(trainx), np.array(trainy)

        model = Sequential()
        model.add(LSTM(64, activation='relu', input_shape=(trainx.shape[1], trainx.shape[2]), return_sequences=True))
        model.add(LSTM(32, activation='relu', return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(trainy.shape[1]))

        model.compile(optimizer='adam', loss='mse')
        model.summary()

        trainX, trainY = trainx[:len(trainx)-6], trainy[:len(trainy)-6]
        testX, testY = trainx[len(trainx)-6:], trainy[len(trainy)-6:]

        model.fit(trainX, trainY, epochs=5, batch_size=16, validation_split=0.2, verbose=1)

        n_past = 7
        n_months_for_prediction = 6

        predict_period_dates = pd.date_range(list(train_dates)[-n_past], periods=n_months_for_prediction,
                                             freq="MS").tolist()

        prediction = model.predict(testX)

        prediction_copies = np.repeat(prediction, 8, axis=-1)
        y_pred_future = scaler.inverse_transform(prediction_copies)[:, 0]
        print(y_pred_future)

        actual_copies = np.repeat(testY, 8, axis=-1)
        y_actual_future = scaler.inverse_transform(actual_copies)[:, 0]

        forecast_dates = []
        for time_i in predict_period_dates:
            forecast_dates.append(time_i.date())

        month = forecast_dates[0].month - 2
        year = forecast_dates[0].year + month // 12
        month = month % 12 + 1
        day = 15
        month = datetime(year=year, month=month, day=day)
        lastFood, err = databse.getFoodPriceMonth(foodName, location, month)
        lastPrice = lastFood.price[month]
        prediction = Predictions(location, foodName, forecast_dates[0], y_pred_future, y_pred_future[0]/lastPrice)
        res = self.addPrediction(prediction)
        print(res)
        return None

    def addPrediction(self, prediction):
        res = prediction.add_prediction()
        return res


p = Prediction()
p.predict_price()
