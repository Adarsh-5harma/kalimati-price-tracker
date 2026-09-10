import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.read_csv("potato_prices.csv")

dataframe.plot(x="date", y="avg_price", kind="line", title="Potato Prices Over Time")
 
plt.savefig("potato_prices_plot.png")
plt.show()      