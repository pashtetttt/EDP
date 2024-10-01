# Relationship between solar radio flux F10.7 and sunspot number
# Team members:
# 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime

file_path = "data_group1.txt"
data = pd.read_csv(file_path, delim_whitespace=True)

data.columns = ["year", "month", "radio flux", "number"]


date = []
for i in range(len(data["month"])):
    year_month = datetime.date(data["year"][i], data["month"][i], 1)
    
    date.append(year_month)


# x=range(0,len(data['month']))
# ax = plt.axes()

plt.rcParams["figure.facecolor"]="white"
plt.plot(date, data['radio flux'], color='r',linewidth=0.5)
plt.plot(date, data['number'],linewidth=0.5)

plt.xlabel('Data')
plt.ylabel('Solar activity indicators')
plt.legend(labels=['Monthly solar radio flux F0.7','Monthly sunspot Numbers'])
plt.show()


