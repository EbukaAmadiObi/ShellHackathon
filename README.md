# ShellHackathon
Unfinished submission for [Shell.ai Hackathon 2023](https://www.shell.com/content/shell/corporate/global/en_gb/energy-and-innovation/digitalisation/digital-and-ai-competitions/shell-ai-hackathon-for-sustainable-and-affordable-energy/_jcr_content/root/main/section/simple/simple/call_to_action/links/item0.stream/1689930670046/ffd0dc218e58bf39a13cd70bc306c81d3a1fb9a1/detailed-problem-statement.pdf)

In this hackathon, participants get chance to design a sustainable and efficient agricultural waste collection network for the state of Gujarat, India, by predicting the waste generation potential in the given area.

we are given a time-series of biomass availability in the state of Gujarat from year 2010 to 2017, formatted as a matrix fo 2147 harvesting sites sorted by latitude and longitude.

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
Reads in the 2010 to 2017 data as well as the 2018 and 2019 forecast data and presents it as an easily readable heatmap using matplotlib.

<img width="556" alt="2018" src="https://github.com/EbukaAmadiObi/ShellHackathon/assets/53743864/b3837a28-1ad3-4ba1-8f73-8e5568683840">


