import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Loading the penguins dataset 
penguins_dataset = sns.load_dataset('penguins')
# print(penguins.head(7))

# Drawing a dist plot
sns.set_style('whitegrid')

# # Drawing a distplot with kde and histogram plot
# sns.distplot(penguins_dataset['bill_depth_mm'])

# # Showing the rug plot as well with kde and histogram
# sns.distplot(penguins_dataset['bill_depth_mm'], rug=True)

# # Removing the kde plot
# sns.distplot(penguins_dataset['bill_depth_mm'], kde=False)

# # Removing the histogram plot
# sns.distplot(penguins_dataset['bill_depth_mm'], hist=False)

# # Setting the number of bins
# sns.distplot(penguins_dataset['bill_depth_mm'], bins=5)

# # Setting the bin values by an array
# sns.distplot(penguins_dataset['bill_depth_mm'], bins=[12, 17, 20])

# # giving style to rugplot by using 'run_kws' parameter
# sns.distplot(penguins_dataset['bill_depth_mm'], rug=True, rug_kws={'color': 'green', 'height':0.20})

# giving style to histogram plot by using 'hist_kws' parameter
# sns.distplot(penguins_dataset['bill_depth_mm'], kde = False, hist_kws={'color':'orange', 'histtype':'step', 'alpha': 0.7})
# sns.distplot(penguins_dataset['bill_depth_mm'], kde = False, hist_kws={'color':'orange', 'histtype':'stepfilled', 'alpha': 0.7})

# Giving style to kde plot. 'lw' is linewidth 
sns.distplot(penguins_dataset['bill_depth_mm'], hist = False, kde_kws={'color':'orange', 'lw':9, 'alpha': 0.7})


# Showing the plot
plt.show()