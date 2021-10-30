# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style= "white")
# %%
df= pd.read_csv ("ulabox_orders_with_categories_partials_2017.csv")
df[["total_items", "discount%","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]]
# %%
df[["total_items", "discount%","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].info()
# %%
df[["total_items", "discount%","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].max()
# %%
df[["total_items", "discount%","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].min()
# %%
df[["total_items", "discount%","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].mean()
# %%
df[["total_items", "discount%","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].median()
# %%
df[["total_items", "discount%","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].std()
# %%
f = plt.figure(figsize=(15, 8))
sns.heatmap(df[["total_items", "discount%","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].corr(), annot=True, linewidths=0.5, )

# %%
