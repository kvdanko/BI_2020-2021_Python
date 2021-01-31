import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data frame generation
dataframe = pd.DataFrame(np.random.randint(1, 100, size=(100, 2), dtype=int))
dataframe.columns = ["X", "Y"]
dataframe.drop_duplicates("X", inplace=True)
dataframe.sort_values("X", inplace=True)

# Line plot visualization
plt.plot(dataframe["X"], dataframe["Y"])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line plot")
plt.savefig("Lineplot_1.png")
