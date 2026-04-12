import pandas as pd
import matplotlib.pyplot as plt


years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
rohit = [0, 300, 600, 1000, 1300, 1800, 1400, 1500, 1900, 0]
plt.plot(years, kohli, color="red", linestyle="--", label="Kohli")
plt.plot(years, sehwag, color="green", linestyle="-.", label="sehwag")
plt.plot(years, rohit, color="Blue", label="Rohit")
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()