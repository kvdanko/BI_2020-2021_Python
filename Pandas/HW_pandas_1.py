import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

df = pd.read_csv("/home/katerina/PycharmProjects/pandas_data/train.csv", na_values="NaN")

df.plot(x="pos", y=["A", "G", "T", "C"], kind="bar", stacked=True, cmap="Set3")
plt.title("Nucleotide distribution per position")
plt.xlabel("Position")
plt.ylabel("Count")
plt.xticks(fontsize=5)
plt.legend(frameon=False)
plt.savefig("HW_pandas_1.png")