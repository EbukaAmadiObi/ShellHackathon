# ShellHackathon Project
Unfinished project for [Shell.ai Hackathon 2023](https://www.shell.com/content/shell/corporate/global/en_gb/energy-and-innovation/digitalisation/digital-and-ai-competitions/shell-ai-hackathon-for-sustainable-and-affordable-energy/_jcr_content/root/main/section/simple/simple/call_to_action/links/item0.stream/1689930670046/ffd0dc218e58bf39a13cd70bc306c81d3a1fb9a1/detailed-problem-statement.pdf)

In this hackathon, participants get chance to design a sustainable and efficient agricultural waste collection network for the state of Gujarat, India, by predicting the waste generation potential in the given area.

We are given a time-series of biomass availability in the state of Gujarat from year 2010 to 2017, formatted as a matrix fo 2147 equisized harvesting sites sorted by latitude and longitude.

## prediction.py
this script takes account of each harvesting site's previous history, then uses ARIMA Time series forecasting to predict the biomass production for 2018 and 2019.
The prediction is written to a csv file as formatted below:

|2018|2019|
| ----------- | ----------- |
|8.777786594599442438e+00|6.870675147947206796e+00|
|3.598092978369389527e+01|3.420881786644399369e+01|
|4.226849587240195660e+01|6.748220092125960434e+01|
|5.016229129296738165e+01|7.029747919428999126e+01|
|1.215570862668064045e+01|2.452884211394681557e+01|

## visualise.py
Reads in the 2010 to 2017 data as well as the 2018 and 2019 forecast data and presents it as a series of easily readable heatmaps using matplotlib.


![forecast_visual](https://github.com/EbukaAmadiObi/ShellHackathon/assets/53743864/d3b1c8f8-2e38-4588-a217-449359db2a9a)

## What's Left?
The other half of the hackathon's problem description was to place depots and refineries around the map to collect and process the biomass effectively. Distance and depot capacity are taken into account to find the best locations for each structure. I found this part of the project quite difficult and unfortunately couldn't finish it within the time limit.

## Update: Accuracy Calculation
Since the hackathon's conclusion, the actual values for the biomass production have been released. Using these values it can be calculated that the time-series forecasting model achieved 79.3% accuracy for 2018 and 91.8% accuracy for 2019.

