'''
Visualisation of forecasted values for biomass production
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gekko import GEKKO

ASPECT = 0.75
COLOUR = 'jet'
DOTSIZE = 17
NO_HARVS = 2417
NO_DEPOTS = 25
CAP_DEPOT = 20000
NO_REFS = 5
CAP_REF = 100000
YEAR = 1 # 0 for 2018, 1 for 2019

# Functions for drawing the refineries and depots
def draw_refinery(x, y):
    plt.scatter(x,y, marker="^",alpha=0.875, c='white', s=60,edgecolors='black') # type: ignore

def draw_depot(x, y):
    plt.scatter(x,y, marker='o',alpha=0.875, c='white', s=60,edgecolors='black') # type: ignore

#**********READ IN DATA**********
# Read in the historical biomass data
df = pd.read_csv('data/Biomass_History.csv', header=0, dtype="float32")
# Convert to numpy array
hist_array = df.to_numpy()

# Read in distance data
df = pd.read_csv('data/Distance_Matrix.csv', header=0, dtype="float32")
# Convert to numpy array
dist_array = df.to_numpy()

# Read in forecast data
df = pd.read_csv('forecast.csv', header=0, dtype="float32")
# Convert to numpy array
fcst_array = df.to_numpy()

#**********CREATE VISUALS**********
# Create a figure with subplots
fig = plt.figure(figsize=(10,10),layout="tight") 

# Plot 2018 forecast
fcst18 = plt.subplot(2,2,1, box_aspect=ASPECT)
fcst18.scatter(hist_array[:,2], hist_array[:,1], c=(fcst_array[:,0]), cmap='jet', vmin=100,vmax=700,s=DOTSIZE)
draw_refinery(70,20)
draw_depot(73,22)
fcst18.set_title('2018 forecast')

# Plot 2019 forecast
fcst19 = plt.subplot(2,2,3, box_aspect=ASPECT)
fcst19.scatter(hist_array[:,2], hist_array[:,1], c=(fcst_array[:,1]), cmap='jet', vmin=100,vmax=700,s=DOTSIZE)
fcst19.set_title('2019 forecast')

#**********HISTORICAL PLOTS**********
plt10 = fig.add_subplot(4,4,3, box_aspect=ASPECT)
plt10.scatter(hist_array[:,2], hist_array[:,1], c=(hist_array[:,3]), cmap=COLOUR, vmin=100,vmax=700,s=DOTSIZE)
plt10.set_title('2010')

plt11 = fig.add_subplot(4,4,4, box_aspect=ASPECT)
plt11.scatter(hist_array[:,2], hist_array[:,1], c=(hist_array[:,4]), cmap=COLOUR, vmin=100,vmax=700,s=DOTSIZE)
plt11.set_title('2011')

plt12 = fig.add_subplot(4,4,7, box_aspect=ASPECT)
plt12.scatter(hist_array[:,2], hist_array[:,1], c=(hist_array[:,5]), cmap=COLOUR, vmin=100,vmax=700,s=DOTSIZE)
plt12.set_title('2012')

plt13 = fig.add_subplot(4,4,8, box_aspect=ASPECT)
plt13.scatter(hist_array[:,2], hist_array[:,1], c=(hist_array[:,6]), cmap=COLOUR, vmin=100,vmax=700,s=DOTSIZE)
plt13.set_title('2013')

plt14 = fig.add_subplot(4,4,11, box_aspect=ASPECT)
plt14.scatter(hist_array[:,2], hist_array[:,1], c=(hist_array[:,7]), cmap=COLOUR, vmin=100,vmax=700,s=DOTSIZE)
plt14.set_title('2014')

plt15 = fig.add_subplot(4,4,12, box_aspect=ASPECT)
plt15.scatter(hist_array[:,2], hist_array[:,1], c=(hist_array[:,8]), cmap=COLOUR, vmin=100,vmax=700,s=DOTSIZE)
plt15.set_title('2015')

plt16 = fig.add_subplot(4,4,15, box_aspect=ASPECT)
plt16.scatter(hist_array[:,2], hist_array[:,1], c=(hist_array[:,9]), cmap=COLOUR, vmin=100,vmax=700,s=DOTSIZE)
plt16.set_title('2016')

plt17 = fig.add_subplot(4,4,16, box_aspect=ASPECT)
plt17.scatter(hist_array[:,2], hist_array[:,1], c=(hist_array[:,10]), cmap=COLOUR, vmin=100,vmax=700,s=DOTSIZE)
plt17.set_title('2017')

plt.show()
fig.savefig('forecast_visual.png')


