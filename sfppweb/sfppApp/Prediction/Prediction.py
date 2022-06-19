import calendar
import datetime
from ..Models import Food, Data, Predictions, Notification
from ..Database import databse
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import tensorflow_docs as tfdocs
import tensorflow_docs.modeling


class Prediction:
    def __init__(self):
        return
    current_date = datetime.datetime(year=2021, month=4, day=15)
# map staple food price with the corresponding data(precipitaion, temprature...)
    def map_price_to_data(self, priceList, dataList, first_month):
        date = []
        date_pre = []
        price = []
        price_pre = []
        precipitation = []
        precipitation_pre = []
        tempMax = []
        tempMax_pre = []
        tempMin = []
        tempMin_pre = []
        diesel = []
        diesel_pre = []
        kerosene = []
        kerosene_pre = []
        exRate = []
        exRate_pre = []
# get months for prediction
        months = [(self.add_months(first_month, 1)).strftime('%Y-%m-%d %H:%M:%S'),
                  (self.add_months(first_month, 2)).strftime('%Y-%m-%d %H:%M:%S'),
                  (self.add_months(first_month, 3)).strftime('%Y-%m-%d %H:%M:%S'),
                  (self.add_months(first_month, 4)).strftime('%Y-%m-%d %H:%M:%S'),
                  (self.add_months(first_month, 5)).strftime('%Y-%m-%d %H:%M:%S'),
                  (self.add_months(first_month, 6)).strftime('%Y-%m-%d %H:%M:%S')]

        for data in dataList:
            if data.month > datetime.datetime.strptime(months[-1], '%Y-%m-%d %H:%M:%S'):
                continue
            # collect data for prediction
            if str(data.month) in months:
                date_pre.append(data.month)
                price_pre.append(0)
                precipitation_pre.append(data.precipitation)
                tempMax_pre.append(data.maxTemp)
                tempMin_pre.append(data.minTemp)
                diesel_pre.append(data.dieselPrice)
                kerosene_pre.append(data.petrolPrice)
                exRate_pre.append(data.exRate)
                continue
            # collect data for training
            if data.month in priceList:
                date.append(data.month)
                price.append(priceList[data.month])
                precipitation.append(data.precipitation)
                tempMax.append(data.maxTemp)
                tempMin.append(data.minTemp)
                diesel.append(data.dieselPrice)
                kerosene.append(data.petrolPrice)
                exRate.append(data.exRate)
        # map list for training
        mapList = {'date': date, 'price': price, 'Precipitation': precipitation, 'TempMax': tempMax,
                   'TempMin': tempMin, 'Diesel': diesel, 'Kerosene': kerosene, 'ExRate': exRate}
        # map list for prediction
        mapListForPre = {'date': date_pre, 'price': price_pre, 'Precipitation': precipitation_pre,
                         'TempMax': tempMax_pre, 'TempMin': tempMin_pre, 'Diesel': diesel_pre, 'Kerosene': kerosene_pre,
                         'ExRate': exRate_pre}
        return mapList, mapListForPre

    def predict_price(self, foodName, location):
        food = Food(foodName, location)
        priceList = food.price
        # there must be atleast 30 rows to start prediction for a specific food
        if len(priceList) < 30:
            return
        # get data for the given location
        data = Data(None, location)
        dataList = data.get_data()
        mappedList, mappedListForPre = self.map_price_to_data(priceList, dataList, self.current_date)
        
        # create a dataframe with the data
        df = pd.DataFrame(
            {'Price': mappedList['price'],
             'Precipitation': mappedList['Precipitation'],
             'TempMax': mappedList['TempMax'],
             'TempMin': mappedList['TempMin'],
             'Diesel': mappedList['Diesel'],
             'Kerosene': mappedList['Kerosene'],
             'ExRate': mappedList['ExRate']
             })
        # add second as an independent variable for the model
        df['Seconds'] = pd.to_datetime(mappedList['date'], format='%m/%d/%Y').map(pd.Timestamp.timestamp)

        # create a dataframe for the prediction
        dfForPre = pd.DataFrame(
            {'Price': mappedListForPre['price'],
             'Precipitation': mappedListForPre['Precipitation'],
             'TempMax': mappedListForPre['TempMax'],
             'TempMin': mappedListForPre['TempMin'],
             'Diesel': mappedListForPre['Diesel'],
             'Kerosene': mappedListForPre['Kerosene'],
             'ExRate': mappedListForPre['ExRate']
             })
        dfForPre['Seconds'] = pd.to_datetime(mappedListForPre['date'], format='%m/%d/%Y').map(pd.Timestamp.timestamp)
        
        # get mean, standard deviation...
        ts = df.describe()
        ts = ts.transpose()
        
        # split the data into training and validation
        train_data, val_data = train_test_split(df, test_size=0.15)
        
        # reduce the data values into a smaller range(eg: from 100 to 5000-> -3 to 3)
        def norm(x):
            return (x - ts['mean']) / ts['std']
        
        # convert the reduced data back to original
        def denorm(x):
            return (x * ts['std']['Price']) + ts['mean']['Price']

        # apply the function and normalize the data
        ntrd = norm(train_data)
        nvad = norm(val_data)
        nfpr = norm(dfForPre)

        train_labels = ntrd.pop('Price')
        val_labels = nvad.pop('Price')
        _ = nfpr.pop('Price')

        def build_model():
            # initialize the model
            model = Sequential()
            # add a layer with 32 nuerons
            model.add(Dense(32, input_shape=(ntrd.shape[1],)))
            # add a layer with 64 nuerons and an activation function relu
            model.add(Dense(64, 'relu'))
            model.add(Dense(64, 'relu'))
            model.add(Dense(1))

            optimizer = Adam(learning_rate=0.001)
            model.compile(loss='mse', optimizer=optimizer, metrics=['mae', 'mse', 'mape'])
            return model

        model = build_model()
        # save the best model
        ckpt_path = r'.\models\price_predictions.ckpt'
        ckpt_callback = tf.keras.callbacks.ModelCheckpoint(filepath=ckpt_path, monitor='val_loss', save_best_only=True,
                                                           save_weights_only=True, verbose=0, )
        EPOCHS = 50
        batch_size = 32

        # fit the training and validation data into the model
        history = model.fit(ntrd, train_labels, batch_size=batch_size, epochs=EPOCHS, verbose=0, shuffle=True,
                            steps_per_epoch=int(ntrd.shape[0] / batch_size), validation_data=(nvad, val_labels),
                            callbacks=[tfdocs.modeling.EpochDots(), ckpt_callback])
        
        # predict price with the data prepared for prediction
        pr = model.predict(nfpr)
        # convert the predicted price back to original range
        pred = denorm(pr).flatten()

        # add the predictions to database
        first_month = self.add_months(self.current_date, 1)
        last_price = Food(foodName, location, month=self.current_date).get_price_month()
        percentChange = pred[0]/last_price
        prediction = Predictions(location, foodName, first_month, pred, percentChange)

        res = self.addPrediction(prediction)
        # send notification to users if the percent change is greater than 1.2 or less than 0.8
        if percentChange > 1.2 or percentChange < 0.8:
            today = datetime.datetime.today()
            today = datetime.date(today.year, today.month, today.day)
            notification = Notification(location, foodName, first_month, pred,
                                        percentChange, today.strftime('%Y-%m-%d %H:%M:%S'))
            res = notification.add_notification()
            if res:
                notification.send_notification()
        return res

    # function to add month to a given date
    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return datetime.datetime(year=year, month=month, day=day)

    def predictForEach(self):
        # get each unique food name and location from the database
        items, err = databse.getNamesAndLocations()
        if err is not None:
            return False
        for item in items:
            # for each unique food name and location predict the future price 
            self.predict_price(item[0], item[1])
        return True

    def addPrediction(self, prediction):
        # add the given prediction to database
        res = prediction.add_prediction()
        return res

