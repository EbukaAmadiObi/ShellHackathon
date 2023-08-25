'''
Prediction 2018 and 2019 values for biomass production
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

YEARS = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

# Read in the data
df = pd.read_csv('data/Biomass_History.csv', header=0)
#print(df.tail())

# Convert to numpy array
array = df.to_numpy()

# Create a figure with subplots
fig, plt1 = plt.subplots(nrows=1, ncols=1)

#**********PREDICTION LOOP**********
i = 0
forecast = np.zeros((len(array),2))
# loop through each co-ordinate
for co_ord in array:

    
    # fit model
    model = ARIMA(co_ord[3:], order=(1, 0, 1))
    model_fit = model.fit()
    # make prediction for 2018
    yhat = model_fit.predict(8,8)
    # append to forecast list
    forecast[i,0] = yhat

    # add to co-ordinate history
    co_ord = np.append(co_ord, yhat)

    # fit model again
    model = ARIMA(co_ord[3:], order=(1, 0, 1))
    model_fit = model.fit()
    # make prediction for 2019
    yhat2 = model_fit.predict(9,9)
    # append to forecast list
    forecast[i,1] = yhat2

    print('forecasted value for index' + str(i))
    i+=1

print(forecast)
# save to csv
np.savetxt("forecast.csv", forecast, delimiter=",", header='2018, 2019')

'''
#**********FORECAST PLOT**********
# choose random co-ordinate
co_ord = array[np.random.randint(0, len(array))]
# fit model
model = ARIMA(co_ord[3:], order=(1, 0, 1))
model_fit = model.fit()

# make prediction for 2018
yhat = model_fit.predict(8,8)

co_ord = np.append(co_ord, yhat)

# fit model again
model = ARIMA(co_ord[3:], order=(1, 0, 1))
model_fit = model.fit()

# make prediction for 2019
yhat2 = model_fit.predict(9,9)

# plot data
plt1.plot(YEARS, co_ord[3:11])
plt1.plot([2018, 2019], [yhat,yhat2], 'ro')
plt1.grid()
plt1.set_title('Biomass Prediction for ' +'lat: '+ str(co_ord[1]) + ' long: ' + str(co_ord[2]))
plt.show()'''