import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data frame generation
dataframe = pd.DataFrame(np.random.normal(1, 100, size=(1000, 2)))
dataframe.columns = ["X", "Y"]

# Visualization of jointplot
sns.jointplot(
    x=dataframe["X"],
    y=dataframe["Y"],
    fill=True,
    color="green",
    kind="kde")
plt.savefig("Favourite_plot.png")
