from get_data import get_data
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as pyplot

def main():
    df = get_data()
    #dev-note: x needs to be 2D array to pass into model, achieved with reshape(-1,1)
    x = df["n-transactions-total"].values.reshape(-1,1)
    y = df["market-price"].values
    
    
    # Linear regression model
    model = LinearRegression()
    model.fit(x, y)

    # Plot model
    pyplot.scatter(x,y)
    pyplot.ylabel("Bitcoin price")
    pyplot.xlabel("Feature: Number of transactions")
    pyplot.plot(x, model.predict(x), color = "orange")
    pyplot.show()
    

if __name__ == "__main__":
    main()


