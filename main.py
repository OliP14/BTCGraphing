import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
Outline:
• Objective: Create custom graphical representations of Bitcoin data.

• Use matplotlib to create graphs
• Use pandas to convert BTC data into DataFrame to be graphed
• Try and turn into website to make making custom graphs easier
• Potentially implement ML to "read" graphs, etc.?
"""

# Prepping data from Excel file to be graphed

price_data_excel_path = "/Users/oliverpasquesi/vscode/Python/BTCGraphing/BTC Data/BTC Data.xlsx"

df = pd.DataFrame(pd.read_excel(price_data_excel_path))

####################################

# Here are a collection of methods that manipulate the data.
# We can change the data that is displayed by inserting the method into the plt.plot() function.

def log_price(y):
    return np.log(y)


def log_reg_line():  # Creates a logarithmic regression line from the price data presented
    df["Log Price"] = [np.log(x) for x in df["Price USD"]]
    


def price_error(): #((price - log(price))/log(price)) * 100
    price_error_adjusted_data = [np.abs((((x - np.log(x)) / np.log(x)) * 100)) for x in df["Price USD"]]  # Using list comprehension to iterate and modify data of "Price USD" column
    #print(price_error_adjusted_data)

    df["Price Error"] = price_error_adjusted_data  # Creates a new column with modified price data
    print(df)

####################################

# Creating graph

x = df.loc[:, "Date"]
y = df.loc[:, "Price USD"]

plt.plot(x, y)
plt.xlabel("Date")
plt.ylabel("Price USD")
plt.title("BTC Price Data")
plt.show()


# TO DO: Create some preset graphs that you can just call and then it will print that graph.  Also have a different, custom graph function.
