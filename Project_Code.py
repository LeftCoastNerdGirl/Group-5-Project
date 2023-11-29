#This is the master documentation for all code for Project One
#Place imports/other tools and data sets here (dependencies)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#Q1, Slide 4, Lori: "Average Temperature and Milk Production by Month (2000 – 2020)"
    #x-axis is the month/year, y-axis plots both average temperature and milk production


#Q1, Slide 5, Lori: "Average Precipitation and Milk Production by Month (2000 – 2020)"
    #x-axis is the month/year, y-axis plots both average precipiation and milk production


#Q1, Slide 6, Celestee:



#Q2, Slide 8, Celestee


#Q2, Slide 9, Betul


#Q2, Slide 10, Betul


#Q3, Slide 12, Elizabeth: "Relative Average Temperature and Bovine Product Yields (2000-2020)"
    #x-axis should be relative average temperature (), y-axis should have combined cow product yields in $
slope, intercept = np.polyfit(x, y, 1)
plt.scatter(x, y, label='Data Points')
plt.plot(x, slope * x + intercept, color='red', label='Linear Regression Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Regression Scatter Plot')
plt.legend()
plt.show()

#Q3, Slide 13, Priya

